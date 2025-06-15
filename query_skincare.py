from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma
import argparse

def load_skincare_db(persist_dir="./skincare_db"):
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma(persist_directory=persist_dir, embedding_function=embedding_function)
    return vectorstore

def query_skincare_products(query, k=3):
    """
    Query the skincare database for similar products.
    
    Args:
        query: User query about skincare needs or products
        k: Number of results to return
    
    Returns:
        List of relevant documents
    """
    vectorstore = load_skincare_db()
    results = vectorstore.similarity_search(query, k=k)
    return results

def print_results(results):
    """Pretty print the search results"""
    if not results:
        print("No results found.")
        return
        
    print(f"\nFound {len(results)} relevant products:\n")
    for i, doc in enumerate(results):
        print(f"Result {i+1}")
        print("-" * 50)
        print(doc.page_content.strip())
        print("-" * 50)
        print(f"Metadata: {doc.metadata}")
        print("\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Query skincare products database")
    parser.add_argument("query", type=str, help="Your skincare question or need")
    parser.add_argument("--num_results", "-n", type=int, default=3, help="Number of results to return")
    args = parser.parse_args()
    
    results = query_skincare_products(args.query, k=args.num_results)
    print_results(results)
