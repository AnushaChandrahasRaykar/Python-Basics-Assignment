# Import required libraries
import os
from groq import Groq

# Get API key from environment variable
api_key = os.getenv("GROQ_API_KEY")

# Create Groq client
client = Groq(api_key=api_key)

# Define prompt
prompt = "What is Machine Learning?"

# Send request to Groq API
response = client.chat.completions.create(
    messages=[
        {"role": "user", "content": prompt}
    ],
    model="llama-3.3-70b-versatile"
)

# Print the response
print("Groq Response:")
print(response.choices[0].message.content)