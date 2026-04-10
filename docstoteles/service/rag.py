import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader    # load documents
from langchain_community.embeddings import HuggingFaceEmbeddings                 # embeddings integration
from langchain_community.vectorstores import FAISS                              # vector database
from langchain_text_splitters import RecursiveCharacterTextSplitter              # split documents into smaller chunks
from langchain_groq import ChatGroq                                             # Groq API
from langchain.chains import RetrievalQA                                        # retrieval QA chain
from langchain.prompts import PromptTemplate                                    # prompt creation

class RAGService:
    def __init__(self):
        # Inicializar embeddings
        self.embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )
        
        # Initialize LLM
        self.llm = ChatGroq(
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name="llama-3.1-8b-instant"
        )
        
        # Text splitter = smaller chunks
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        
        # Initialize properties
        self.vector_store = None
        self.qa_chain = None
    
    def load_collection(self, collection_name):
        """Loads documents and creates the vector store"""
        collection_path = f"data/collections/{collection_name}"
        
        # Load documents
        loader = DirectoryLoader(
            collection_path,                    # folder path
            glob="**/*.md",                     # load all markdown files
            loader_cls=TextLoader,
            loader_kwargs={'encoding': 'utf-8'}
        )
        
        documents = loader.load()
        
        if not documents:
            return False
        
        # Split into chunks
        texts = self.text_splitter.split_documents(documents)
        
        # Create vector store
        self.vector_store = FAISS.from_documents(texts, self.embeddings)
        
        # Create QA chain
        template = """
            Use the following documents to answer the question.
            If you do not know the answer, say that you do not know.

            {context}

            Question: {question}
            Answer:
        """

        prompt = PromptTemplate(
            template=template,
            input_variables=["context", "question"]
        )
        
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vector_store.as_retriever(search_kwargs={"k": 3}),
            chain_type_kwargs={"prompt": prompt}
        )
        
        return True
    
    def ask_question(self, question):
        """Asks a question using RAG"""
        if not self.qa_chain:               # does the chain exist?
            return "No collection loaded."
        
        try:
            result = self.qa_chain.run(question)
            return result                   # returns the language model answer
        except Exception as e:
            return f"Error while processing the question: {str(e)}"