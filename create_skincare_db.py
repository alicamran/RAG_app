from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma
from langchain.docstore.document import Document
import pandas as pd
import os

def create_skincare_db(csv_path="mockup_skincare_products.csv", persist_dir="./skincare_db"):
    # Load the CSV data
    df = pd.read_csv("mockup_skincare_products.csv")
    
    # Create documents
    docs = []
    for i, row in df.iterrows():
        content = f"""
        Product Name: {row['Product Name']}
        Skin Type Suitability: {row['Skin Type Suitability']}
        Ingredients: {row['Ingredients']}
        Benefits: {row['Benefits']}
        Price: {row['Price']}
        Brand: {row['Brand']}
        Category: {row['Category']}
        Reviews: {row['Reviews']}
        """
        metadata = {
            "product_name": row['Product Name'],
            "brand": row['Brand'],
            "category": row['Category'],
            "price": row['Price'],
            "skin_type": row['Skin Type Suitability']
        }
        docs.append(Document(page_content=content, metadata=metadata))

    # Embed and store in Chroma
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # Ensure directory exists
    os.makedirs(persist_dir, exist_ok=True)
    
    # Create and persist the vector database
    vectorstore = Chroma.from_documents(
        docs, 
        embedding_function, 
        persist_directory=persist_dir
    )
    
    vectorstore.persist()
    print(f"Created vector database with {len(docs)} documents")
    return vectorstore

if __name__ == "__main__":
    create_skincare_db()
