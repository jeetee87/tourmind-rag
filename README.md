# TourMind

TourMind is een eenvoudig RAG (Retrieval-Augmented Generation) project dat ik heb gebouwd om meer te leren over Python, AI en Large Language Models.

Het project leest Markdown-documenten (`.md` bestanden), zet deze om naar embeddings en slaat deze op in een lokale Chroma vector database. Vervolgens kan een gebruiker vragen stellen over de inhoud van deze documenten.

## Wat doet TourMind?

TourMind kan vragen beantwoorden over informatie die in documenten staat, bijvoorbeeld:

* Tourschema's
* Technische riders
* Hotelinformatie
* Cateringinformatie

Voorbeeld:

> Vraag: "Hoelaat is de soundcheck in Amsterdam?"

Als deze informatie in de documenten staat, probeert TourMind het juiste antwoord te geven. Staat het antwoord niet in de documenten, dan geeft TourMind aan dat het niet gevonden kon worden.

## Hoe werkt het?

Het project bestaat uit twee onderdelen.

### 1. Database opbouwen

Dit script:

* Leest alle `.md` bestanden uit de map `documents`
* Splitst documenten op in kleinere stukken (chunks)
* Maakt embeddings met `nomic-embed-text`
* Slaat alles op in een lokale Chroma database

### 2. Vragen stellen

Dit script:

* Opent de bestaande Chroma database
* Zoekt de meest relevante informatie
* Stuurt deze informatie naar een lokaal LLM via Ollama
* Geeft een antwoord terug aan de gebruiker

## Gebruikte technologieën

* Python
* LangChain
* Ollama
* ChromaDB
* qwen2.5:3b
* nomic-embed-text
* Streamlit (voor toekomstige uitbreiding)

## Installatie

1. Clone deze repository:

```bash
git clone <repository-url>
cd TourMind
```

2. Installeer alle benodigde packages:

```bash
pip install -r requirements.txt
```

3. Download de Ollama modellen:

```bash
ollama pull qwen2.5:3b
ollama pull nomic-embed-text
```

4. Bouw de vector database:

```bash
python build_database.py
```

5. Start de applicatie:

```bash
python ask_question.py
```

## requirements.txt

```text
langchain
langchain-community
langchain-ollama
langchain-text-splitters
langchain-chroma
chromadb
streamlit
pypdf
markdown
python-dotenv
```

## Projectstructuur

```text
TourMind/
│
├── documents/
│   ├── tourschema.md
│   ├── technische_rider.md
│   ├── hotelinformatie.md
│   └── catering.md
│
├── chroma_db/
├── build_database.py
├── ask_question.py
├── requirements.txt
└── README.md
```

## Wat ik heb geleerd

Met dit project heb ik geleerd:

* Werken met LangChain
* Werken met Ollama
* Embeddings maken
* Werken met een vector database
* De basis van RAG-systemen
* Markdown-documenten verwerken
* Lokale LLM's gebruiken

## Toekomstige ideeën

* Een webinterface bouwen met Streamlit.
* PDF-documenten toevoegen.
* Memory toevoegen aan TourMind.
* Ondersteuning voor meerdere gebruikers.
* Een compleet dashboard voor muziekproducties maken.

## Opmerking

Ik ben een beginnende programmeur zonder professionele IT-achtergrond. Dit project is onderdeel van mijn leerproces om meer ervaring op te doen met Python, AI en softwareontwikkeling.
