import requests

# Ollama API endpoint
url = "http://localhost:11434/api/generate"

# Get user input
prompt = input("Enter your question: ")

# Define the payload
payload = {
    "model": "qwen3:4b",
    "prompt": prompt,
    "stream": False
}

# Send request to local Ollama server
try:
    response = requests.post(url, json=payload)
    response.raise_for_status() # Check for errors
    
    result = response.json()
    
    print("\nModel Response:\n")
    print(result["response"])
    
except requests.exceptions.RequestException as e:
    print(f"Error connecting to Ollama: {e}")
    print("Ensure Ollama is running (ollama serve) and the model is downloaded.")   