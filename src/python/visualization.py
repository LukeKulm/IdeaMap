import json
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

# Load embeddings from the JSON file
with open("embeddings/embeddings.json", "r") as f:
    embeddings_data = json.load(f)

# Extract filenames and embeddings, ignoring entries with invalid data
filenames = []
valid_embeddings = []

for filename, embedding in embeddings_data.items():
    if embedding and len(embedding) > 0:  # Ensure valid, non-empty embedding
        filenames.append(filename)
        valid_embeddings.append(embedding)

# Convert embeddings to numpy array
embeddings = np.array(valid_embeddings)

perplexity_value = len(valid_embeddings) -2

# Reduce to 2D using t-SNE
if embeddings.shape[0] > 1:  # Ensure there is more than one embedding
    tsne = TSNE(n_components=2, random_state=42, perplexity=perplexity_value)
    embeddings_2d = tsne.fit_transform(embeddings)

    # Plot the embeddings
    plt.figure(figsize=(10, 8))
    plt.scatter(embeddings_2d[:, 0], embeddings_2d[:, 1], c='blue', marker='o')

    # Annotate each point with the filename (or part of the filename)
    for i, filename in enumerate(filenames):
        plt.text(embeddings_2d[i, 0], embeddings_2d[i, 1], filename.split('.')[0], fontsize=9)

    plt.title("2D Visualization of Idea Embeddings")
    plt.xlabel("Dimension 1")
    plt.ylabel("Dimension 2")
    plt.show()
else:
    print("Not enough valid embeddings to visualize. Please add more ideas.")
