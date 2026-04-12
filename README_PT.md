## ✅ Status Atual

A aplicação está totalmente funcional localmente e também implantada no Streamlit Cloud.

As atualizações recentes focaram em:
- Estabilização de dependências
- Correção de compatibilidade no ecossistema LangChain
- Garantia de um ambiente reproduzível entre local e cloud

## 🧠 O que estou aprendendo

- RAG (Retrieval-Augmented Generation)
- Ecossistema LangChain
- Embeddings e banco vetorial (FAISS)
- Como lidar com conflitos reais de dependências em projetos Python

## 🚧 Próximos passos

- Melhorar desempenho e limites do web scraping
- Adicionar citações de fontes nas respostas
- Melhorar a experiência de interface (UI/UX)
- Suporte a múltiplas coleções simultâneas

# 📚 Docstóteles — Transforme qualquer documentação em um chat com IA
### 🌍 Versão em inglês
👉 Demonstração ao vivo (EN): https://docstoteles-en.streamlit.app/
👉 Demonstração ao vivo (PT): https://docstoteles-pt.streamlit.app/

O Docstóteles é uma aplicação simples de **RAG** que permite fazer **web scraping** de documentações técnicas e depois conversar com esse conteúdo usando IA.

O projeto foi construído com **Streamlit**, **Firecrawl**, **LangChain**, **FAISS**, **embeddings da Hugging Face** e **LLMs da Groq**.

---

## ✨ O que ele faz

Com o Docstóteles, você pode:

- Colar a URL de uma documentação
- Fazer scraping automático das páginas
- Armazenar esse conteúdo localmente
- Fazer perguntas em linguagem natural sobre essa documentação

Isso torna o projeto útil para explorar e estudar documentações como:

- Python
- Streamlit
- LangChain
- React
- entre outras

---

## 🧠 Por que esse projeto é útil

Documentações técnicas costumam ser:

- longas demais
- espalhadas em várias páginas
- difíceis de consultar quando você não sabe exatamente o termo certo

O Docstóteles resolve isso combinando:

- **Web scraping** → para coletar a documentação
- **Embeddings** → para representar significado
- **Retrieval-Augmented Generation (RAG)** → para buscar trechos relevantes
- **LLMs** → para responder com base no contexto recuperado

Na prática, ele transforma documentação em um assistente de IA pesquisável.

---

## 🚀 Tecnologias usadas

- **[Streamlit](https://streamlit.io/)** — Interface gráfica
- **[Firecrawl](https://firecrawl.dev/)** — Web scraping
- **[LangChain](https://python.langchain.com/)** — Pipeline de RAG
- **[FAISS](https://github.com/facebookresearch/faiss)** — Banco vetorial
- **[Hugging Face](https://huggingface.co/)** — Embeddings
- **[Groq](https://console.groq.com/)** — Inferência com LLM

---

## 📂 Estrutura do projeto

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
└── .env.exemplo  # variáveis de ambiente (não subir .env real)

⚙️ Instalação
1) Clone o repositório
git clone https://github.com/SEU_USUARIO/Docstoteles.git
cd Docstoteles
2) Crie e ative um ambiente virtual
Windows
python -m venv .venv
.venv\Scripts\activate
Mac/Linux
python3 -m venv .venv
source .venv/bin/activate
3) Instale as dependências
pip install -r requirements.txt
4) Crie um arquivo .env na raiz do projeto
GROQ_API_KEY=sua_chave_groq
FIRECRAWL_API_KEY=sua_chave_firecrawl
FIRECRAWL_API_URL=http://localhost:3002

Importante: No código Python, o nome da variável deve bater exatamente com:
GROQ_API_KEY

▶️ Como rodar

### Versão em inglês
streamlit run docstoteles/app.py
### Versão em português
streamlit run docstoteles/app_pt.py

Depois, abra no navegador o link local exibido no terminal.

📝 Como usar
1) Modo Scraping
Abra a aba Scraping na barra lateral
Cole a URL de uma documentação
Dê um nome para a coleção
Inicie o scraping
2) Modo Chat
Vá para a aba Chat
Selecione a coleção salva
Faça perguntas sobre a documentação raspada
🌐 Sugestões de documentações para testar
https://docs.streamlit.io
https://python.langchain.com/docs
https://docs.python.org/3/tutorial
https://ohmyposh.dev/docs
⚠️ Observações
Este é um projeto local com foco educacional e de portfólio
O Firecrawl precisa estar corretamente configurado localmente
O app atualmente salva a documentação raspada em data/collections
Dependendo do tamanho da documentação, o tempo de resposta pode variar
💡 Possíveis melhorias

Ideias para versões futuras:

Upload de PDFs e arquivos
Chat com múltiplas coleções
Melhorias de UI/UX
Exclusão de coleções
Citação de fontes nas respostas
Deploy em nuvem

### Versão em inglês
👉 Live app: https://docstoteles-en.streamlit.app/

### Versão em português
👉 Live app: https://docstoteles-pt.streamlit.app/

🧑‍💻 Autor

Projeto construído de forma prática para explorar como documentações podem ser transformadas em assistentes conversacionais com IA.

Se quiser, fique à vontade para adaptar, expandir ou evoluir o projeto.
