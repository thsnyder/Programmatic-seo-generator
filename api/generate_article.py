import os
import sys
import json
from http.server import BaseHTTPRequestHandler
from dotenv import load_dotenv

if os.path.exists('.env.local'):
    load_dotenv('.env.local')

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

try:
    from content_with_ai import generate_full_article, generate_meta_title, generate_meta_description
except ImportError as e:
    print(f"Error importing content functions: {e}")
    def generate_full_article(keyword, title, brief, product="Files.com"):
        return f"# {title}\n\n## Introduction\n\n{keyword} is an essential topic that every professional should understand."
    def generate_meta_title(keyword, product="Files.com"):
        return f"{keyword} - Complete Guide, Tips & Best Practices"
    def generate_meta_description(keyword, product="Files.com"):
        return f"Learn everything about {keyword} with our comprehensive guide. Discover best practices and expert tips."

class handler(BaseHTTPRequestHandler):
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
        if not data or 'keyword' not in data:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'Keyword is required'}).encode())
            return
        keyword = data['keyword'].strip()
        title = data.get('title', '').strip()
        brief = data.get('brief', '').strip()
        product = data.get('product', 'Files.com').strip()
        if not keyword:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'Keyword cannot be empty'}).encode())
            return
        full_article = generate_full_article(keyword, title, brief, product)
        meta_title = generate_meta_title(keyword, product)
        meta_description = generate_meta_description(keyword, product)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        self.wfile.write(json.dumps({
            'full_article': full_article,
            'meta_title': meta_title,
            'meta_description': meta_description
        }).encode())
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers() 