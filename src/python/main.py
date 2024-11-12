import os
import json

# Path to the JSON file where ideas will be saved
ideas_file_path = os.path.join(os.path.dirname(__file__), "../../data/ideas.json")

# Load existing ideas if the JSON file exists, otherwise start with an empty list
if os.path.exists(ideas_file_path):
    with open(ideas_file_path, "r") as file:
        ideas = json.load(file)
else:
    ideas = []

print("Type your ideas below. Type 'quit' to exit.")

while True:
    # Prompt user for input
    idea = input("Enter your idea: ")

    # Check if the user wants to quit
    if idea.lower() == "quit":
        print("Exiting program.")
        break

    # Append the new idea to the list
    ideas.append(idea)

    # Save all ideas to the JSON file
    with open(ideas_file_path, "w") as file:
        json.dump(ideas, file, indent=4)

    print("Idea saved.")
