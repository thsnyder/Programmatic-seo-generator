from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(__file__))

# Import content generation functions
try:
    from content_with_ai import (
        generate_content_brief, 
        generate_article_title, 
        generate_full_article, 
        generate_meta_title, 
        generate_meta_description
    )
except ImportError as e:
    print(f"Error importing content functions: {e}")
    # Fallback functions if import fails
    def generate_content_brief(keyword, product="Files.com"):
        return f"Content brief for '{keyword}' for {product}: Create a comprehensive guide covering fundamentals, best practices, and actionable tips."
    
    def generate_article_title(keyword, product="Files.com"):
        return f"The Complete Guide to {keyword}: Everything You Need to Know"
    
    def generate_full_article(keyword, title, product="Files.com", content_length="medium"):
        return f"# {title}\n\n## Introduction\n\n{keyword} is an essential topic that every professional should understand."
    
    def generate_meta_title(keyword, product="Files.com"):
        return f"{keyword} - Complete Guide, Tips & Best Practices"
    
    def generate_meta_description(keyword, product="Files.com"):
        return f"Learn everything about {keyword} with our comprehensive guide. Discover best practices and expert tips."

app = Flask(__name__)
CORS(app)

@app.route('/api/health', methods=['GET', 'OPTIONS'])
def health():
    """Health check endpoint"""
    if request.method == 'OPTIONS':
        return '', 200, {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type'
        }
    
    return jsonify({
        'status': 'healthy',
        'message': 'Server is running'
    })

@app.route('/api/generate_content', methods=['POST', 'OPTIONS'])
def generate_content():
    """Generate all content in one step"""
    if request.method == 'OPTIONS':
        return '', 200, {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type'
        }
    
    try:
        data = request.get_json()
        
        if not data or 'keyword' not in data:
            return jsonify({'error': 'Keyword is required'}), 400
        
        keyword = data['keyword'].strip()
        product = data.get('product', 'Files.com').strip()
        content_length = data.get('contentLength', 'medium').strip()
        
        if not keyword:
            return jsonify({'error': 'Keyword cannot be empty'}), 400
        
        print(f"🚀 API Call: /generate_content for keyword: '{keyword}' for product: '{product}' with length: '{content_length}'")
        
        # Generate all content in one step
        article_title = generate_article_title(keyword, product)
        full_article = generate_full_article(keyword, article_title, product, content_length)
        meta_title = generate_meta_title(keyword, product)
        meta_description = generate_meta_description(keyword, product)
        
        print(f"✅ API Response: Successfully generated all content for '{keyword}' for {product}")
        
        return jsonify({
            'article_title': article_title,
            'full_article': full_article,
            'meta_title': meta_title,
            'meta_description': meta_description
        })
        
    except Exception as e:
        print(f"❌ Error in generate_content: {e}")
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

@app.route('/api/generate_article', methods=['POST', 'OPTIONS'])
def generate_article():
    """Generate article with custom title and brief"""
    if request.method == 'OPTIONS':
        return '', 200, {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type'
        }
    
    try:
        data = request.get_json()
        
        if not data or 'keyword' not in data:
            return jsonify({'error': 'Keyword is required'}), 400
        
        keyword = data['keyword'].strip()
        title = data.get('title', '').strip()
        brief = data.get('brief', '').strip()
        product = data.get('product', 'Files.com').strip()
        
        if not keyword:
            return jsonify({'error': 'Keyword cannot be empty'}), 400
        
        print(f"🚀 API Call: /generate_article for keyword: '{keyword}' for product: '{product}'")
        
        # Generate all content
        full_article = generate_full_article(keyword, title, product)
        meta_title = generate_meta_title(keyword, product)
        meta_description = generate_meta_description(keyword, product)
        
        print(f"✅ API Response: Successfully generated article for '{keyword}' for {product}")
        
        return jsonify({
            'full_article': full_article,
            'meta_title': meta_title,
            'meta_description': meta_description
        })
        
    except Exception as e:
        print(f"❌ Error in generate_article: {e}")
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

@app.route('/api/generate_brief_title', methods=['POST', 'OPTIONS'])
def generate_brief_title():
    """Generate content brief and title"""
    if request.method == 'OPTIONS':
        return '', 200, {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type'
        }
    
    try:
        data = request.get_json()
        
        if not data or 'keyword' not in data:
            return jsonify({'error': 'Keyword is required'}), 400
        
        keyword = data['keyword'].strip()
        product = data.get('product', 'Files.com').strip()
        
        if not keyword:
            return jsonify({'error': 'Keyword cannot be empty'}), 400
        
        print(f"🚀 API Call: /generate_brief_title for keyword: '{keyword}' for product: '{product}'")
        
        # Generate brief and title
        content_brief = generate_content_brief(keyword, product)
        article_title = generate_article_title(keyword, product)
        
        print(f"✅ API Response: Successfully generated brief and title for '{keyword}' for {product}")
        
        return jsonify({
            'content_brief': content_brief,
            'article_title': article_title
        })
        
    except Exception as e:
        print(f"❌ Error in generate_brief_title: {e}")
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
