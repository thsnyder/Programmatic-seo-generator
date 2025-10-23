from http.server import BaseHTTPRequestHandler
import json
import os
import sys

# Add the current directory to Python path to import content_with_ai
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

try:
    from content_with_ai import generate_article_title, generate_full_article, generate_meta_title, generate_meta_description
except ImportError as e:
    print(f"Error importing content functions: {e}")
    # Fallback functions if import fails
    def generate_article_title(keyword, product="Files.com"):
        return f"The Complete Guide to {keyword}: Everything You Need to Know"
    
    def generate_full_article(keyword, title, product="Files.com", content_length="medium"):
        return f"# {title}\n\n## Introduction\n\n{keyword} is an essential topic that every professional should understand."
    
    def generate_meta_title(keyword, product="Files.com"):
        return f"{keyword} - Complete Guide, Tips & Best Practices"
    
    def generate_meta_description(keyword, product="Files.com"):
        return f"Learn everything about {keyword} with our comprehensive guide. Discover best practices and expert tips."

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            # Read the request body
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            if not data or 'keyword' not in data:
                self.send_error_response(400, 'Keyword is required')
                return
            
            keyword = data['keyword'].strip()
            product = data.get('product', 'Files.com').strip()
            content_length = data.get('contentLength', 'medium').strip()
            
            if not keyword:
                self.send_error_response(400, 'Keyword cannot be empty')
                return
            
            print(f"🚀 API Call: /generate_content for keyword: '{keyword}' for product: '{product}' with length: '{content_length}'")
            
            # Generate all content in one step
            article_title = generate_article_title(keyword, product)
            full_article = generate_full_article(keyword, article_title, product, content_length)
            meta_title = generate_meta_title(keyword, product)
            meta_description = generate_meta_description(keyword, product)
            
            print(f"✅ API Response: Successfully generated all content for '{keyword}' for {product}")
            
            # Send success response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = {
                'article_title': article_title,
                'full_article': full_article,
                'meta_title': meta_title,
                'meta_description': meta_description
            }
            self.wfile.write(json.dumps(response).encode())
            
        except Exception as e:
            print(f"❌ Error in generate_content: {e}")
            self.send_error_response(500, f'Internal server error: {str(e)}')
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def send_error_response(self, status_code, message):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        error_response = {'error': message}
        self.wfile.write(json.dumps(error_response).encode())