import subprocess
import sys

def install_dependencies():
    """Install all required dependencies for the RAG application"""
    print("Installing required packages...")
    
    packages = [
        "langchain",
        "sentence-transformers",
        "chromadb",
        "pandas",
        "flask"
    ]
    
    for package in packages:
        print(f"Installing {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
    print("\nAll dependencies installed successfully!")
    print("You can now run the application with 'python create_skincare_db.py'")

if __name__ == "__main__":
    install_dependencies()
