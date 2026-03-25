import requests

# New Hugging Face router endpoint for GPT-2 (public model)
API_URL = "https://router.huggingface.co/hf-inference/gpt2"

# No Authorization header needed for public GPT-2
data = {"inputs": "Explain Artificial Intelligence in simple words."}

response = requests.post(API_URL, json=data)

# Safely handle response
try:
    output = response.json()
    print("Output:\n", output)
except ValueError:
    print("Error decoding JSON. Status code:", response.status_code)
    print("Response text:", response.text)