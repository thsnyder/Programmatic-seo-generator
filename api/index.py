import os
import sys
import json
from http.server import BaseHTTPRequestHandler
from dotenv import load_dotenv

# Load environment variables from .env.local (for local development)
# Vercel will use environment variables directly
if os.path.exists('.env.local'):
    load_dotenv('.env.local')

# Add the parent directory to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

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

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()
            response = {'status': 'healthy', 'message': 'Server is running'}
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'Not found'}).encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        try:
            data = json.loads(post_data.decode('utf-8'))
        except json.JSONDecodeError:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'Invalid JSON'}).encode())
            return

        if self.path == '/api/generate_brief_title':
            response = self.handle_generate_brief_title(data)
        elif self.path == '/api/generate_article':
            response = self.handle_generate_article(data)
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'Not found'}).encode())
            return

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def handle_generate_brief_title(self, data):
        """Generate content brief and article title for a keyword"""
        try:
            if not data or 'keyword' not in data:
                return {'error': 'Keyword is required'}
            
            keyword = data['keyword'].strip()
            product = data.get('product', 'Files.com').strip()
            
            if not keyword:
                return {'error': 'Keyword cannot be empty'}
            
            print(f"🚀 API Call: /generate_brief_title for keyword: '{keyword}' for product: '{product}'")
            
            # Generate content using functions
            content_brief = generate_content_brief(keyword, product)
            article_title = generate_article_title(keyword, product)
            
            print(f"✅ API Response: Successfully generated brief and title for '{keyword}' for {product}")
            
            return {
                'content_brief': content_brief,
                'article_title': article_title
            }
            
        except Exception as e:
            print(f"❌ API Error in /generate_brief_title: {e}")
            return {'error': 'Internal server error'}

    def handle_generate_article(self, data):
        """Generate full article with meta data"""
        try:
            if not data or 'keyword' not in data:
                return {'error': 'Keyword is required'}
            
            keyword = data['keyword'].strip()
            title = data.get('title', '').strip()
            brief = data.get('brief', '').strip()
            product = data.get('product', 'Files.com').strip()
            
            if not keyword:
                return {'error': 'Keyword cannot be empty'}
            
            print(f"🚀 API Call: /generate_article for keyword: '{keyword}' for product: '{product}'")
            
            # Generate all content
            full_article = generate_full_article(keyword, title, brief, product)
            meta_title = generate_meta_title(keyword, product)
            meta_description = generate_meta_description(keyword, product)
            
            print(f"✅ API Response: Successfully generated article for '{keyword}' for {product}")
            
            return {
                'full_article': full_article,
                'meta_title': meta_title,
                'meta_description': meta_description
            }
            
        except Exception as e:
            print(f"❌ API Error in /generate_article: {e}")
            return {'error': 'Internal server error'} 