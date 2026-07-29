from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2:1b"
)

response = llm.invoke("Introduce yourself in one sentence.")

print(response.content)