import os
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()

# ---- Groq ----
from groq import Groq
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def query_groq(prompt):
    try:
        response = groq_client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.1-8b-instant"
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Groq Error: {e}"


# ---- Cohere ----
import cohere
co = cohere.Client(os.getenv("COHERE_API_KEY"))

def query_cohere(prompt):
    try:
        response = co.generate(
            model='command',
            prompt=prompt,
            max_tokens=200
        )
        return response.generations[0].text.strip()
    except Exception as e:
        return f"Cohere Error: {e}"


# ---- Hugging Face ----
def query_huggingface(prompt):
    try:
        API_URL = "https://api-inference.huggingface.co/models/gpt2"
        headers = {
            "Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"
        }

        response = requests.post(API_URL, headers=headers, json={"inputs": prompt})

        if response.status_code == 200:
            return response.json()[0]["generated_text"]
        else:
            return f"HuggingFace Error: {response.status_code}"

    except Exception as e:
        return f"HuggingFace Error: {e}"


# ---- MAIN PROGRAM ----
def main():
    print("\nSelect AI Provider:")
    print("1. Groq")
    print("2. Cohere")
    print("3. Hugging Face")

    choice = input("Enter choice (1-3): ")
    prompt = input("Enter your prompt: ")

    if choice == "1":
        print("\n--- Groq Response ---")
        print(query_groq(prompt))

    elif choice == "2":
        print("\n--- Cohere Response ---")
        print(query_cohere(prompt))

    elif choice == "3":
        print("\n--- Hugging Face Response ---")
        print(query_huggingface(prompt))

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()