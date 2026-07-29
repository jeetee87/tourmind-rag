from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import ChatOllama

# Maak een loader die alle .md bestanden uit de map 'documents' gaat zoeken.
loader = DirectoryLoader(
    "documents",
    glob = "*.md",
    loader_cls=TextLoader,
)

# Alle gevonden bestanden ingelezen. 
# We krijgen een lijst met LangChain objecten terug
documents = loader.load()

# Textsplitter - grote documenten worden opgesplitst naar kleinere stukken
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500, # maximale grootte
    chunk_overlap = 100, # Aantal tekens dat overlapt
)

# Splits alle documenten in chunks
chunks = text_splitter.split_documents(documents)

# Embedding model - zet de text om naar getallen (vectoren)
embeddings = OllamaEmbeddings(
    model = "nomic-embed-text"
)

# Maak de vector database.
# Iedere chunk krijgt een embedding
# Embedding word opgeslagen
# Alles word opgeslagen lokaal in de map "chroma_db"
Chroma.from_documents(
    documents = chunks,
    embedding = embeddings,
    collection_name = "tourmind",
    persist_directory= "chroma_db",
)

print("Database succesvol opgebouwd.")
print(f"{len(documents)} documenten verwerkt.")
print(f"{len(chunks)} chunks opgeslagen.")