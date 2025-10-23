from http.server import BaseHTTPRequestHandler
import json
import os
import sys

# Add the current directory to Python path to import content_with_ai
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

try:
    from content_with_ai import generate_content_brief, generate_article_title
except ImportError as e:
    print(f"Error importing content functions: {e}")
    # Fallback functions if import fails
    def generate_content_brief(keyword, product="Files.com"):
        return f"Content brief for '{keyword}' for {product}: Create a comprehensive guide covering fundamentals, best practices, and actionable tips. Target audience: {product} users and potential customers."
    
    def generate_article_title(keyword, product="Files.com"):
        return f"The Complete Guide to {keyword}: Everything You Need to Know"

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
            
            if not keyword:
                self.send_error_response(400, 'Keyword cannot be empty')
                return
            
            print(f"🚀 API Call: /generate_brief_title for keyword: '{keyword}' for product: '{product}'")
            
            # Generate content using functions
            content_brief = generate_content_brief(keyword, product)
            article_title = generate_article_title(keyword, product)
            
            print(f"✅ API Response: Successfully generated brief and title for '{keyword}' for {product}")
            
            # Send success response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = {
                'content_brief': content_brief,
                'article_title': article_title
            }
            self.wfile.write(json.dumps(response).encode())
            
        except Exception as e:
            print(f"❌ Error in generate_brief_title: {e}")
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