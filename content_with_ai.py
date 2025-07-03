from flask import Blueprint, request, jsonify
from openai import OpenAI
import os
import time

content_bp = Blueprint('content', __name__)

# Configure OpenAI
api_key = os.getenv('OPENAI_SECRET_KEY') or os.getenv('OPENAI_API_KEY')
if not api_key:
    print("⚠️  Warning: OpenAI API key not found in environment variables")
    print("🔄 Using template-based content generation as fallback")
    client = None
else:
    client = OpenAI(api_key=api_key)

def generate_content_brief(keyword, product="Files.com"):
    """Generate a content brief for the given keyword using OpenAI"""
    print(f"🤖 OpenAI API: Generating content brief for keyword: '{keyword}' for product: '{product}'")
    
    if not client:
        print(f"🔄 Using template for keyword: '{keyword}' for {product}")
        return f"Content brief for '{keyword}' for {product}: Create a comprehensive guide covering fundamentals, best practices, and actionable tips. Target audience: {product} users and potential customers. Include examples and case studies relevant to {product}'s market. Use a mix of paragraph text and bulleted lists for better readability."
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"You are an expert content strategist for {product}. Create a detailed content brief for SEO articles that are specifically tailored for {product}'s audience and brand voice. Focus on providing clear direction for content creation that aligns with {product}'s expertise and market position. Include guidance for content structure with a mix of paragraphs and bulleted lists."
                },
                {
                    "role": "user",
                    "content": f"Create a comprehensive content brief for an article about '{keyword}' that will be published on {product}'s website. Include target audience, key topics to cover, tone, content structure (mix of paragraphs and bulleted lists), and specific sections to include. Keep it concise but detailed. Make sure the content aligns with {product}'s brand and expertise."
                }
            ],
            max_tokens=300,
            temperature=0.7
        )
        print(f"✅ OpenAI API: Successfully generated content brief for '{keyword}' for {product}")
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"❌ OpenAI API Error generating content brief: {e}")
        print(f"🔄 Falling back to template for keyword: '{keyword}' for {product}")
        return f"Content brief for '{keyword}' for {product}: Create a comprehensive guide covering fundamentals, best practices, and actionable tips. Target audience: {product} users and potential customers. Include examples and case studies relevant to {product}'s market. Use a mix of paragraph text and bulleted lists for better readability."

def generate_article_title(keyword, product="Files.com"):
    """Generate an article title for the given keyword using OpenAI"""
    print(f"🤖 OpenAI API: Generating article title for keyword: '{keyword}' for product: '{product}'")
    
    if not client:
        print(f"🔄 Using template for keyword: '{keyword}' for {product}")
        return f"The Complete Guide to {keyword}: Everything You Need to Know"
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"You are an expert SEO copywriter for {product}. Create compelling, SEO-friendly article titles that are engaging, click-worthy, and aligned with {product}'s brand voice and expertise. Return only ONE title without quotation marks."
                },
                {
                    "role": "user",
                    "content": f"Create ONE compelling article title for '{keyword}' that will be published on {product}'s website. Make it SEO-friendly, engaging, and click-worthy. The title should reflect {product}'s expertise and appeal to their target audience. Return only the title without any quotation marks or numbering."
                }
            ],
            max_tokens=100,
            temperature=0.8
        )
        print(f"✅ OpenAI API: Successfully generated article title for '{keyword}' for {product}")
        title = response.choices[0].message.content.strip()
        # Remove quotation marks from beginning and end
        title = title.strip('"').strip("'").strip()
        # Remove any numbering or list formatting
        title = title.replace('1.', '').replace('2.', '').replace('3.', '').replace('-', '').strip()
        return title
    except Exception as e:
        print(f"❌ OpenAI API Error generating article title: {e}")
        print(f"🔄 Falling back to template for keyword: '{keyword}' for {product}")
        return f"The Complete Guide to {keyword}: Everything You Need to Know"

def generate_meta_title(keyword, product="Files.com"):
    """Generate a meta title for SEO using OpenAI"""
    print(f"🤖 OpenAI API: Generating meta title for keyword: '{keyword}' for product: '{product}'")
    
    if not client:
        print(f"🔄 Using template for keyword: '{keyword}' for {product}")
        return f"{keyword} - Complete Guide, Tips & Best Practices"
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"You are an SEO expert for {product}. Create compelling meta titles that are under 60 characters, include the target keyword, and are optimized for {product}'s brand and audience. Return titles without quotation marks."
                },
                {
                    "role": "user",
                    "content": f"Create a compelling meta title for '{keyword}' that will be used on {product}'s website. It should be under 60 characters, include the keyword, and be click-worthy. Make it relevant to {product}'s expertise and audience. Return without quotation marks."
                }
            ],
            max_tokens=80,
            temperature=0.7
        )
        print(f"✅ OpenAI API: Successfully generated meta title for '{keyword}' for {product}")
        meta_title = response.choices[0].message.content.strip()
        # Remove quotation marks from beginning and end
        meta_title = meta_title.strip('"').strip("'").strip()
        return meta_title
    except Exception as e:
        print(f"❌ OpenAI API Error generating meta title: {e}")
        print(f"🔄 Falling back to template for keyword: '{keyword}' for {product}")
        return f"{keyword} - Complete Guide, Tips & Best Practices"

def generate_meta_description(keyword, product="Files.com"):
    """Generate a meta description for SEO using OpenAI"""
    print(f"🤖 OpenAI API: Generating meta description for keyword: '{keyword}' for product: '{product}'")
    
    if not client:
        print(f"🔄 Using template for keyword: '{keyword}' for {product}")
        return f"Learn everything about {keyword} with our comprehensive guide. Discover best practices, expert tips, and proven strategies."
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"You are an SEO expert for {product}. Create compelling meta descriptions that are under 160 characters, include the target keyword, and are optimized for {product}'s brand and audience."
                },
                {
                    "role": "user",
                    "content": f"Create a compelling meta description for '{keyword}' that will be used on {product}'s website. It should be under 160 characters, include the keyword, and be engaging and click-worthy. Make it relevant to {product}'s expertise and audience."
                }
            ],
            max_tokens=120,
            temperature=0.7
        )
        print(f"✅ OpenAI API: Successfully generated meta description for '{keyword}' for {product}")
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"❌ OpenAI API Error generating meta description: {e}")
        print(f"🔄 Falling back to template for keyword: '{keyword}' for {product}")
        return f"Learn everything about {keyword} with our comprehensive guide. Discover best practices, expert tips, and proven strategies."

def generate_full_article(keyword, title, brief, product="Files.com"):
    """Generate a full article based on keyword, title, and brief using OpenAI"""
    print(f"🤖 OpenAI API: Generating full article for keyword: '{keyword}' with title: '{title}' for product: '{product}'")
    
    if not client:
        print(f"🔄 Using template for keyword: '{keyword}' for {product}")
        return f"""# {title}

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

### Continuous Learning
Stay updated with the latest trends, best practices, and emerging technologies in the {keyword} space. Attend conferences, participate in professional communities, and invest in ongoing education.

## Measuring Success

### Key Performance Indicators (KPIs)
- Efficiency metrics and performance benchmarks
- User satisfaction and engagement rates
- Return on investment (ROI) calculations
- Quality indicators and success metrics
- Long-term sustainability measures

### Tools and Analytics
Utilize appropriate measurement tools to track progress and identify areas for improvement. Regular reporting and analysis help maintain focus on objectives and demonstrate value.

## Future Trends and Considerations

The landscape of {keyword} continues to evolve rapidly. Stay informed about emerging trends, technological advances, and changing best practices. Consider how these developments might impact your strategy and be prepared to adapt accordingly.

## Conclusion

Mastering {keyword} requires dedication, continuous learning, and adaptation to changing conditions. By following the strategies and best practices outlined in this guide, you'll be well-equipped to achieve success in your {keyword} endeavors.

Remember to always prioritize value creation, maintain ethical practices, and focus on sustainable, long-term results. Success in {keyword} comes from consistent effort, strategic thinking, and a commitment to excellence.

## Additional Resources

- Industry publications and research reports
- Professional associations and communities
- Training programs and certification courses
- Expert consultations and advisory services
- Technology platforms and implementation tools

Start implementing these strategies today and begin your journey toward {keyword} mastery. With the right approach and consistent effort, you can achieve remarkable results and establish yourself as a leader in this important field."""
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"You are an expert content writer specializing in SEO articles for {product}. Write comprehensive, well-structured articles in markdown format that are specifically tailored for {product}'s audience, brand voice, and expertise. Use a balanced mix of paragraph text and bulleted lists to improve readability and engagement. Include headings, subheadings, bullet points, and engaging content that provides real value to {product}'s readers and potential customers."
                },
                {
                    "role": "user",
                    "content": f"Write a comprehensive article about '{keyword}' with the title '{title}' for {product}'s website. Use this content brief as guidance: {brief}\n\nWrite the article in markdown format with proper headings (H1, H2, H3). Use a balanced mix of paragraph text and bulleted lists throughout the article. Include practical tips, examples, and actionable advice that are relevant to {product}'s audience and expertise. Make it at least 1500 words with good readability. The content should reflect {product}'s brand voice and market position. Use bullet points for lists of features, benefits, steps, or tips, and use paragraphs for explanations and context."
                }
            ],
            max_tokens=2000,
            temperature=0.7
        )
        print(f"✅ OpenAI API: Successfully generated full article for '{keyword}' for {product}")
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"❌ OpenAI API Error generating full article: {e}")
        print(f"🔄 Falling back to template for keyword: '{keyword}' for {product}")
        # Fallback to template if API fails
        return f"""# {title}

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

### Continuous Learning
Stay updated with the latest trends, best practices, and emerging technologies in the {keyword} space. Attend conferences, participate in professional communities, and invest in ongoing education.

## Measuring Success

### Key Performance Indicators (KPIs)
- Efficiency metrics and performance benchmarks
- User satisfaction and engagement rates
- Return on investment (ROI) calculations
- Quality indicators and success metrics
- Long-term sustainability measures

### Tools and Analytics
Utilize appropriate measurement tools to track progress and identify areas for improvement. Regular reporting and analysis help maintain focus on objectives and demonstrate value.

## Future Trends and Considerations

The landscape of {keyword} continues to evolve rapidly. Stay informed about emerging trends, technological advances, and changing best practices. Consider how these developments might impact your strategy and be prepared to adapt accordingly.

## Conclusion

Mastering {keyword} requires dedication, continuous learning, and adaptation to changing conditions. By following the strategies and best practices outlined in this guide, you'll be well-equipped to achieve success in your {keyword} endeavors.

Remember to always prioritize value creation, maintain ethical practices, and focus on sustainable, long-term results. Success in {keyword} comes from consistent effort, strategic thinking, and a commitment to excellence.

## Additional Resources

- Industry publications and research reports
- Professional associations and communities
- Training programs and certification courses
- Expert consultations and advisory services
- Technology platforms and implementation tools

Start implementing these strategies today and begin your journey toward {keyword} mastery. With the right approach and consistent effort, you can achieve remarkable results and establish yourself as a leader in this important field."""

@content_bp.route('/generate_brief_title', methods=['POST'])
def generate_brief_title():
    """Generate content brief and article title for a keyword"""
    try:
        data = request.get_json()
        
        if not data or 'keyword' not in data:
            return jsonify({'error': 'Keyword is required'}), 400
        
        keyword = data['keyword'].strip()
        product = data.get('product', 'Files.com').strip()
        
        if not keyword:
            return jsonify({'error': 'Keyword cannot be empty'}), 400
        
        print(f"🚀 API Call: /generate_brief_title for keyword: '{keyword}' for product: '{product}'")
        
        # Generate content using OpenAI
        content_brief = generate_content_brief(keyword, product)
        article_title = generate_article_title(keyword, product)
        
        print(f"✅ API Response: Successfully generated brief and title for '{keyword}' for {product}")
        
        return jsonify({
            'content_brief': content_brief,
            'article_title': article_title
        })
        
    except Exception as e:
        print(f"❌ API Error: /generate_brief_title failed: {e}")
        return jsonify({'error': str(e)}), 500

@content_bp.route('/generate_article', methods=['POST'])
def generate_article():
    """Generate full article based on keyword, title, and brief"""
    try:
        data = request.get_json()
        
        required_fields = ['keyword', 'article_title', 'content_brief']
        for field in required_fields:
            if not data or field not in data:
                return jsonify({'error': f'{field} is required'}), 400
        
        keyword = data['keyword'].strip()
        article_title = data['article_title'].strip()
        content_brief = data['content_brief'].strip()
        product = data.get('product', 'Files.com').strip()
        
        if not all([keyword, article_title, content_brief]):
            return jsonify({'error': 'All fields must be non-empty'}), 400
        
        print(f"🚀 API Call: /generate_article for keyword: '{keyword}' with title: '{article_title}' for product: '{product}'")
        
        # Generate content using OpenAI
        full_article = generate_full_article(keyword, article_title, content_brief, product)
        meta_title = generate_meta_title(keyword, product)
        meta_description = generate_meta_description(keyword, product)
        
        print(f"✅ API Response: Successfully generated full article and meta data for '{keyword}' for {product}")
        
        return jsonify({
            'full_article': full_article,
            'meta_title': meta_title,
            'meta_description': meta_description
        })
        
    except Exception as e:
        print(f"❌ API Error: /generate_article failed: {e}")
        return jsonify({'error': str(e)}), 500

@content_bp.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'message': 'Content generation service is running'}) 