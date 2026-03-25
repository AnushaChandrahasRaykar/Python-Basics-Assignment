import requests

url = "http://localhost:11434/api/generate"

prompt = input("Enter your prompt: ")

data = {
    "model": "llama3",
    "prompt": prompt,
    "stream": False
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("\n--- Ollama Response ---")
    print(response.json()["response"])
else:
    print("Error:", response.text)