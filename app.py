from flask import Flask, render_template, request, jsonify
from query_skincare import query_skincare_products

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query', '')
    num_results = int(request.form.get('num_results', 3))
    
    if not query:
        return jsonify({'error': 'No query provided'})
    
    results = query_skincare_products(query, k=num_results)
    
    # Format results for JSON response
    formatted_results = []
    for doc in results:
        formatted_results.append({
            'content': doc.page_content.strip(),
            'metadata': doc.metadata
        })
    
    return jsonify({'results': formatted_results})

if __name__ == '__main__':
    app.run(debug=True)
