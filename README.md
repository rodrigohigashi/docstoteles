# 📚 Docstoteles — Turn Any Documentation into an AI Chat Assistant

Docstoteles is a lightweight RAG app that lets you scrape technical documentation from the web and chat with it using AI.

Built with **Streamlit**, **Firecrawl**, **LangChain**, **FAISS**, **Hugging Face embeddings**, and **Groq LLMs**.

---

## ✨ What it does

With Docstoteles, you can:

- Paste the URL of a documentation website
- Automatically scrape its pages
- Store the content as a local knowledge base
- Ask natural-language questions about that documentation

This makes it useful for exploring and learning tools such as:

- Python docs
- Streamlit docs
- LangChain docs
- React docs
- and more

---

## 🧠 Why this project is useful

Technical documentation is often:

- too long
- fragmented across multiple pages
- hard to search when you don’t know the exact keywords

Docstoteles solves this by combining:

- **Web scraping** → to collect the docs
- **Embeddings** → to represent meaning
- **Retrieval-Augmented Generation (RAG)** → to retrieve relevant chunks
- **LLMs** → to answer based on the retrieved context

In practice, it turns documentation into a searchable AI assistant.

---

## 🚀 Tech Stack

- **[Streamlit](https://streamlit.io/)** — UI
- **[Firecrawl](https://firecrawl.dev/)** — Web scraping
- **[LangChain](https://python.langchain.com/)** — RAG pipeline
- **[FAISS](https://github.com/facebookresearch/faiss)** — Vector store
- **[Hugging Face](https://huggingface.co/)** — Embeddings
- **[Groq](https://console.groq.com/)** — LLM inference

---

## 📂 Project Structure

docstoteles/
├── app.py
├── app_pt.py
├── presentation/
│   ├── chat.py
│   ├── chat_pt.py
│   ├── scraping.py
│   └── scraping_pt.py
├── service/
│   ├── rag.py
│   ├── rag_pt.py
│   ├── scraping.py
│   └── scraping_pt.py
└── .env  # create this locally

⚙️ Installation
1) Clone the repository
git clone https://github.com/YOUR_USERNAME/Docstoteles.git
cd Docstoteles
2) Create and activate a virtual environment
Windows
python -m venv .venv
.venv\Scripts\activate
Mac/Linux
python3 -m venv .venv
source .venv/bin/activate
3) Install dependencies
pip install -r requirements.txt
4) Create a .env file in the project root
GROQ_API_KEY=your_groq_api_key
FIRECRAWL_API_KEY=your_firecrawl_api_key
FIRECRAWL_API_URL=http://localhost:3002

Important: In the Python code, the environment variable must match exactly:
GROQ_API_KEY

▶️ Run the app

### English version
streamlit run docstoteles/app.py

### Portuguese version
streamlit run docstoteles/app_pt.py

Then open the local URL shown in the terminal.

📝 How to use
1) Scraping mode
Open the Scraping tab in the sidebar
Paste a documentation URL
Give your collection a name
Start scraping
2) Chat mode
Switch to the Chat tab
Select your saved collection
Ask questions about the scraped documentation
🌐 Suggested documentation websites to test
https://docs.streamlit.io
https://python.langchain.com/docs
https://docs.python.org/3/tutorial
https://ohmyposh.dev/docs
⚠️ Notes
This is a local educational/project portfolio app
Firecrawl must be properly configured locally
The app currently stores scraped docs locally in data/collections
Depending on the documentation size, response time may vary
💡 Possible Improvements

Some ideas for future versions:

Upload PDFs and files
Multi-collection chat
Better UI/UX
Collection deletion
Source citations in answers
Deploy to the cloud
🧑‍💻 Author

Built as a hands-on AI/RAG project to explore how documentation can be transformed into a conversational assistant.

If you want, feel free to fork, adapt, or expand it.