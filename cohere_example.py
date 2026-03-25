# Import libraries
import os
import cohere

# Load API key
api_key = os.getenv("COHERE_API_KEY")

# Check if key loaded
print("API key loaded:", api_key is not None)

# Create Cohere client
co = cohere.Client(api_key)

# Prompt for AI
prompt = "Explain Artificial Intelligence in simple words."

# Send request
response = co.chat(
    model="command-r-plus-08-2024",
    message=prompt
)

# Print response
print("\nCohere API Response:\n")
print(response.text)