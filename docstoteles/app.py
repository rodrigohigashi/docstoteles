import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Docstoteles", page_icon="📚", layout="wide")
st.title("📚 Docstoteles - Simple RAG")

# Selection Sidebar
with st.sidebar:
    st.header("Collections")
    mode = st.radio("Mode:", ["Chat", "Scraping"])
    
    st.divider()
    st.subheader("Available Collections")
    
    collections_dir = "data/collections"    # Folder where scraped files are stored
    if os.path.exists(collections_dir):
        collections = [d for d in os.listdir(collections_dir) # list available collections
                      if os.path.isdir(os.path.join(collections_dir, d))]
        
        for collection in collections:
            col1, col2 = st.columns([3, 1]) 
            with col1:  # Display collection name
                st.write(f"📁 {collection}") 
            with col2:  # Button to select the active collection
                selected = st.session_state.get("collection") == collection
                btn_label = "✅" if selected else "📌"
                if st.button(btn_label, key=f"use_{collection}"):
                    st.session_state.collection = collection
                    st.rerun()

# Session states initialization
if "messages" not in st.session_state:
    st.session_state.messages = []
if "collection" not in st.session_state:
    st.session_state.collection = None

# Render selected page
if mode == "Scraping":
    from presentation import scraping
    scraping.show()
else:
    from presentation import chat
    chat.show() 