AI API Integration Project

Student Details

- Name: Anusha Chandrahas Raykar
- Course: MCA
- Intern: GENAI Intern

---

About the Project

In this project, I have worked on integrating different AI APIs using Python.
The main idea is to give a prompt and get responses from different AI tools.

I have used:

- Groq
- Cohere
- Hugging Face
- Ollama (for local model)

---

Objective

- To learn how AI APIs work
- To connect multiple APIs in one project
- To understand how responses are generated

---

Technologies Used

- Python
- APIs
- Requests library
- Ollama

---

Project Files

src folder contains:

- groq_example.py
- cohere_example.py
- huggingface_example.py
- ollama_example.py
- multi_api_query.py

---

 API Setup

I created a ".env" file to store API keys safely.

Example:

GROQ_API_KEY=your_key
COHERE_API_KEY=your_key
HUGGINGFACE_API_KEY=your_key

---

How to Run

Step 1: Install libraries
pip install groq cohere requests python-dotenv

Step 2: Run files
python src/groq_example.py
python src/cohere_example.py
python src/huggingface_example.py

Step 3: Run main program
python src/multi_api_query.py

---

Ollama

Ollama is used to run AI locally.

Steps:

1. Install Ollama
2. Run command:

ollama run llama3

3. Run file:
   python src/ollama_example.py

---

Output

I have added screenshots of outputs in the screenshots folder.

---

Conclusion

This project helped me understand how different AI APIs work and how to use them in Python.