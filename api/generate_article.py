import json
from http.server import BaseHTTPRequestHandler

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
        
        # Simple inline content generation for testing
        full_article = f"""# {title or f'The Complete Guide to {keyword}'}

## Introduction

{keyword} is a crucial topic that many people want to understand better, especially in the context of {product}'s expertise. In this comprehensive guide, we'll explore everything you need to know about {keyword}, from the basics to advanced strategies that can help you achieve your goals.

## What is {keyword}?

{keyword} refers to the practice and techniques involved in optimizing and implementing effective strategies. It encompasses various methodologies and approaches that help improve results, increase efficiency, and drive meaningful outcomes for individuals and organizations.

## Key Benefits

1. **Improved Performance**: Better results and enhanced effectiveness
2. **Increased Efficiency**: Streamlined processes and optimized workflows  
3. **Better User Experience**: Solutions that serve real needs and deliver value
4. **Higher Success Rates**: More qualified outcomes and measurable improvements
5. **Competitive Advantage**: Stay ahead of trends and industry developments

## Best Practices for {keyword}

### 1. Research and Planning
Before diving into {keyword}, it's essential to conduct thorough research. This includes understanding your target audience, analyzing current market conditions, identifying opportunities, and setting clear, measurable objectives.

### 2. Strategy Development
Create a comprehensive strategy that addresses your specific needs and goals. Focus on developing actionable plans that can be implemented systematically and measured for effectiveness.

### 3. Implementation Techniques
Apply proven methodologies and techniques that have been tested in real-world scenarios. Consider factors such as scalability, sustainability, and long-term impact when choosing your approach.

### 4. Monitoring and Optimization
Continuously monitor your progress and make data-driven adjustments to improve results. Regular evaluation helps identify what's working well and what needs improvement.

## Common Mistakes to Avoid

- **Lack of Clear Strategy**: Jumping into implementation without proper planning
- **Ignoring Data and Analytics**: Making decisions without supporting evidence
- **Poor Resource Allocation**: Not dedicating sufficient time or resources
- **Resistance to Change**: Failing to adapt when circumstances change
- **Overlooking User Feedback**: Not incorporating valuable insights from stakeholders

## Advanced Strategies

### Leveraging Technology
Modern {keyword} implementations benefit greatly from leveraging appropriate technology solutions. Consider automation tools, analytics platforms, and integration capabilities that can enhance your efforts.

### Building Partnerships
Collaborate with industry experts, complementary service providers, and strategic partners to expand your capabilities and reach. Strong partnerships can accelerate success and provide valuable insights.

## Conclusion

{keyword} is an essential component of modern business strategy. By understanding the fundamentals, implementing best practices, and avoiding common pitfalls, you can achieve significant improvements in your results and overall success.

Remember that success with {keyword} requires ongoing commitment, continuous learning, and adaptation to changing circumstances. Stay focused on your goals, measure your progress, and be willing to adjust your approach as needed."""
        
        meta_title = f"{keyword} - Complete Guide, Tips & Best Practices"
        meta_description = f"Learn everything about {keyword} with our comprehensive guide. Discover best practices, expert tips, and proven strategies."
        
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