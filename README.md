# Skincare RAG Application

This is a Retrieval Augmented Generation (RAG) application for skincare product recommendations.

## Setup Instructions

1. **Install Dependencies**:
   ```
   python setup.py
   ```
   This will install all required packages including `sentence-transformers`.

2. **Create Vector Database**:
   ```
   python create_skincare_db.py
   ```

3. **Query from Command Line**:
   ```
   python query_skincare.py "products for oily skin with salicylic acid"
   ```

4. **Run Web Application**:
   ```
   python app.py
   ```
   Then open your browser and go to: http://127.0.0.1:5000

## Troubleshooting

If you encounter the error: `ImportError: Could not import sentence_transformers python package`, it means the package isn't installed correctly. Run `python setup.py` to install all dependencies.

If you still have issues, try manually installing with:
```
pip install sentence-transformers
```

## Requirements

- Python 3.7+
- All dependencies listed in requirements.txt
