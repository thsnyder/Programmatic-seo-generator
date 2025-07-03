import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env.local (for local development)
# Vercel will use environment variables directly
if os.path.exists('.env.local'):
    load_dotenv('.env.local')

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(__file__))

from flask import Flask, send_from_directory
from flask_cors import CORS

# Import blueprints with error handling
try:
    from src.routes.user import user_bp
except ImportError as e:
    print(f"Warning: Could not import user_bp: {e}")
    user_bp = None

try:
    from content_with_ai import content_bp
except ImportError as e:
    print(f"Error: Could not import content_bp: {e}")
    content_bp = None

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'

# Enable CORS for all routes
CORS(app)

# Register blueprints only if they exist
if user_bp:
    app.register_blueprint(user_bp, url_prefix='/api')
if content_bp:
    app.register_blueprint(content_bp, url_prefix='/api')

# Skip database initialization for Vercel to avoid issues
# Database is not needed for the content generation functionality

@app.route('/api/health', methods=['GET'])
def health_check():
    """Simple health check endpoint"""
    return {'status': 'healthy', 'message': 'Server is running'}

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    static_folder_path = app.static_folder
    if static_folder_path is None:
        return "Static folder not configured", 404

    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        index_path = os.path.join(static_folder_path, 'index.html')
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, 'index.html')
        else:
            return "index.html not found", 404

# Export the app for Vercel
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 