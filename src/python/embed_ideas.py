import os
import json
from transformers import AutoTokenizer, AutoModel
import torch

# Path to the JSON file where ideas are stored
ideas_file_path = os.path.join(os.path.dirname(__file__), "../../data/ideas.json")

# Path to the output JSON file for embeddings
embeddings_file_path = os.path.join(os.path.dirname(__file__), "../../data/embeddings.json")

# Load a pre-trained model and tokenizer for embedding
model_name = "sentence-transformers/all-MiniLM-L6-v2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Function to embed text
def embed_text(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        embeddings = model(**inputs).last_hidden_state.mean(dim=1)  # Mean pooling
    return embeddings.squeeze().numpy().tolist()

# Load all ideas from the JSON file
with open(ideas_file_path, "r") as file:
    ideas = json.load(file)

# Create embeddings for each idea
embeddings = {f"idea_{i + 1}": embed_text(idea) for i, idea in enumerate(ideas)}

# Save embeddings to a JSON file
with open(embeddings_file_path, "w") as f:
    json.dump(embeddings, f, indent=4)

print(f"Embeddings saved to '{embeddings_file_path}'")
