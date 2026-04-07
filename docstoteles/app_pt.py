import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Docstóteles", page_icon="📚", layout="wide")
st.title("📚 Docstóteles - RAG Simples")

# Sidebar para seleção
with st.sidebar:
    st.header("Coleções")
    mode = st.radio("Modo:", ["Chat", "Scraping"])
    
    st.divider()
    st.subheader("Coleções Disponíveis")
    
    collections_dir = "data/collections"    # onde salvar os arquivos que fazer o webscraping
    if os.path.exists(collections_dir):
        collections = [d for d in os.listdir(collections_dir) # listar o que tem na pasta collections
                      if os.path.isdir(os.path.join(collections_dir, d))]
        
        for collection in collections:
            col1, col2 = st.columns([3, 1]) # 3 partes para esquerda, 1 pra direita
            with col1:  # lista das documentações
                st.write(f"📁 {collection}") 
            with col2:  # qual coleção quer usar
                selected = st.session_state.get("collection") == collection
                btn_label = "✅" if selected else "📌"
                if st.button(btn_label, key=f"use_{collection}"):
                    st.session_state.collection = collection
                    st.rerun()

# Estados de sessão
if "messages" not in st.session_state:
    st.session_state.messages = []
if "collection" not in st.session_state:
    st.session_state.collection = None

# Importar páginas
if mode == "Scraping":
    from presentation import scraping_pt as scraping
    scraping.show()
else:
    from presentation import chat_pt as chat
    chat.show() 