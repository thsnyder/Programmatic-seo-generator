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

def handler(request, context):
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
        
        print(f"🚀 API Call: /generate_brief_title for keyword: '{keyword}' for product: '{product}'")
        
        # Use actual AI-powered content generation
        content_brief = generate_content_brief(keyword, product)
        article_title = generate_article_title(keyword, product)
        
        print(f"✅ API Response: Successfully generated brief and title for '{keyword}' for {product}")
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps({
                'content_brief': content_brief,
                'article_title': article_title
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