import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env.local (for local development)
# Vercel will use environment variables directly
if os.path.exists('.env.local'):
    load_dotenv('.env.local')

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(__file__))

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

# Import content generation functions directly
try:
    from content_with_ai import (
        generate_content_brief,
        generate_article_title,
        generate_meta_title,
        generate_meta_description,
        generate_full_article
    )
except ImportError as e:
    print(f"Error importing content functions: {e}")
    # Define fallback functions if import fails
    def generate_content_brief(keyword, product="Files.com"):
        return f"Content brief for '{keyword}': Create a comprehensive guide covering fundamentals and best practices."
    
    def generate_article_title(keyword, product="Files.com"):
        return f"The Complete Guide to {keyword}: Everything You Need to Know"
    
    def generate_meta_title(keyword, product="Files.com"):
        return f"{keyword} - Complete Guide, Tips & Best Practices"
    
    def generate_meta_description(keyword, product="Files.com"):
        return f"Learn everything about {keyword} with our comprehensive guide. Discover best practices and expert tips."
    
    def generate_full_article(keyword, title, brief, product="Files.com"):
        return f"# {title}\n\n## Introduction\n\n{keyword} is an essential topic that every professional should understand."

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'

# Enable CORS for all routes
CORS(app)

@app.route('/api/health', methods=['GET'])
def health_check():
    """Simple health check endpoint"""
    return jsonify({'status': 'healthy', 'message': 'Server is running'})

@app.route('/api/generate_brief_title', methods=['POST'])
def generate_brief_title():
    """Generate content brief and article title for a keyword"""
    try:
        data = request.get_json()
        
        if not data or 'keyword' not in data:
            return jsonify({'error': 'Keyword is required'}), 400
        
        keyword = data['keyword'].strip()
        product = data.get('product', 'Files.com').strip()
        
        if not keyword:
            return jsonify({'error': 'Keyword cannot be empty'}), 400
        
        print(f"🚀 API Call: /generate_brief_title for keyword: '{keyword}' for product: '{product}'")
        
        # Generate content using functions
        content_brief = generate_content_brief(keyword, product)
        article_title = generate_article_title(keyword, product)
        
        print(f"✅ API Response: Successfully generated brief and title for '{keyword}' for {product}")
        
        return jsonify({
            'content_brief': content_brief,
            'article_title': article_title
        })
        
    except Exception as e:
        print(f"❌ API Error in /generate_brief_title: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/generate_content', methods=['POST'])
def generate_content():
    """Generate all content in one step"""
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
        print(f"❌ API Error in /generate_content: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/generate_article', methods=['POST'])
def generate_article():
    """Generate full article with meta data (legacy endpoint)"""
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
        full_article = generate_full_article(keyword, title, brief, product)
        meta_title = generate_meta_title(keyword, product)
        meta_description = generate_meta_description(keyword, product)
        
        print(f"✅ API Response: Successfully generated article for '{keyword}' for {product}")
        
        return jsonify({
            'full_article': full_article,
            'meta_title': meta_title,
            'meta_description': meta_description
        })
        
    except Exception as e:
        print(f"❌ API Error in /generate_article: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    """Serve the React app"""
    if path and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 