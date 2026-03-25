# Import required libraries
import os
from openai import OpenAI

# Retrieve OpenAI API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Create OpenAI client object using API key
client = OpenAI(api_key=api_key)

# Define prompt for AI model
prompt = "Explain Artificial Intelligence."

# Send request to OpenAI Chat Completion API
response = client.chat.completions.create(
    model="gpt-4o-mini",  # Model used for response generation
    messages=[{"role":"user","content":prompt}]
)

# Print response
print("OpenAI Response:")
print(response.choices[0].message.content)