from http.server import BaseHTTPRequestHandler
import json
import os
import sys

# Add the current directory to Python path to import content_with_ai
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

try:
    from content_with_ai import generate_full_article, generate_meta_title, generate_meta_description
except ImportError as e:
    print(f"Error importing content functions: {e}")
    # Fallback functions if import fails
    def generate_full_article(keyword, title, brief, product="Files.com"):
        return f"# {title or f'The Complete Guide to {keyword}'}\n\n## Introduction\n\n{keyword} is an essential topic that every professional should understand."
    
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
            title = data.get('title', '').strip()
            brief = data.get('brief', '').strip()
            product = data.get('product', 'Files.com').strip()
            
            if not keyword:
                self.send_error_response(400, 'Keyword cannot be empty')
                return
            
            print(f"🚀 API Call: /generate_article for keyword: '{keyword}' for product: '{product}'")
            
            # Generate all content
            full_article = generate_full_article(keyword, title, brief, product)
            meta_title = generate_meta_title(keyword, product)
            meta_description = generate_meta_description(keyword, product)
            
            print(f"✅ API Response: Successfully generated article for '{keyword}' for {product}")
            
            # Send success response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = {
                'full_article': full_article,
                'meta_title': meta_title,
                'meta_description': meta_description
            }
            self.wfile.write(json.dumps(response).encode())
            
        except Exception as e:
            print(f"❌ Error in generate_article: {e}")
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