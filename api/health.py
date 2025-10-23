import json

def handler(request, response):
    # Set CORS headers
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    
    if request.method == 'GET':
        return {
            'statusCode': 200,
            'body': json.dumps({'status': 'healthy', 'message': 'Server is running'})
        }
    
    elif request.method == 'OPTIONS':
        return {
            'statusCode': 200,
            'body': ''
        }
    
    else:
        return {
            'statusCode': 405,
            'body': json.dumps({'error': 'Method not allowed'})
        } 