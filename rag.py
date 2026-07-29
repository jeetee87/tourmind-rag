from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import ChatOllama

# Embedding model
embeddings = OllamaEmbeddings(
    model = "nomic-embed-text"
)

# Bestaande database openen
vector_store = Chroma(
    collection_name = "tourmind",
    embedding_function = embeddings,
    persist_directory = "chroma_db",
)

# Maakt retriever - met 1 resultaat 
retriever = vector_store.as_retriever(
    search_kwargs = {"k": 1}
)

# LLM - en welke versie
llm = ChatOllama(
    model = "qwen2.5:3b",
    temperature=0,
)

# Vraag stellen
query = input("Stel je vraag: ")

results = retriever.invoke(query)

context = "\n\n".join(
    result.page_content for result in results
)

prompt = f"""
Je bent een RAG-assistent voor muziekproducties.

Gebruik uitsluitend de onderstaande context.
Beantwoord de vraag kort en duidelijk op basis van de context.
Verzin geen informatie

Als het antwoord niet in de context staat, antwoord exact met:

"Niet gevonden."

Context:
{context}

Vraag:
{query}

Antwoord:
"""

response = llm.invoke(prompt)
print("\nANTWOORD:")
print(response.content)
