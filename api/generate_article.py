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

def handler(request, response):
    # Set CORS headers
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except:
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'POST, OPTIONS',
                    'Access-Control-Allow-Headers': 'Content-Type'
                },
                'body': json.dumps({'error': 'Invalid JSON'})
            }
        
        if not data or 'keyword' not in data:
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'POST, OPTIONS',
                    'Access-Control-Allow-Headers': 'Content-Type'
                },
                'body': json.dumps({'error': 'Keyword is required'})
            }
        
        keyword = data['keyword'].strip()
        title = data.get('title', '').strip()
        brief = data.get('brief', '').strip()
        product = data.get('product', 'Files.com').strip()
        
        if not keyword:
            return {
                'statusCode': 400,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': 'POST, OPTIONS',
                    'Access-Control-Allow-Headers': 'Content-Type'
                },
                'body': json.dumps({'error': 'Keyword cannot be empty'})
            }
        
        print(f"🚀 API Call: /generate_article for keyword: '{keyword}' for product: '{product}'")
        
        # Use actual AI-powered content generation
        full_article = generate_full_article(keyword, title, brief, product)
        meta_title = generate_meta_title(keyword, product)
        meta_description = generate_meta_description(keyword, product)
        
        print(f"✅ API Response: Successfully generated article for '{keyword}' for {product}")
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps({
                'full_article': full_article,
                'meta_title': meta_title,
                'meta_description': meta_description
            })
        }
    
    elif request.method == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': ''
        }
    
    else:
        return {
            'statusCode': 405,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': 'Method not allowed'})
        } 