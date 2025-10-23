from openai import OpenAI
import os
import time

# Content generation functions only - no Flask blueprint needed

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

def get_content_length_instructions(content_length):
    """Get specific instructions based on content length"""
    length_instructions = {
        'short': {
            'word_count': 'EXACTLY 500-800 words',
            'sections': 'EXACTLY 3-4 main sections',
            'detail_level': 'concise and focused',
            'max_tokens': 1000,
            'style': 'Keep paragraphs short (2-3 sentences each). Be direct and to the point. Focus on essential information only.',
            'structure': 'Introduction, 2-3 main sections, Conclusion'
        },
        'medium': {
            'word_count': 'EXACTLY 800-1200 words', 
            'sections': 'EXACTLY 4-5 main sections',
            'detail_level': 'balanced with good detail',
            'max_tokens': 1500,
            'style': 'Use medium-length paragraphs (3-4 sentences each). Provide good detail with examples.',
            'structure': 'Introduction, 3-4 main sections, Conclusion'
        },
        'long': {
            'word_count': 'EXACTLY 1200-2000 words',
            'sections': 'EXACTLY 5-6 main sections', 
            'detail_level': 'comprehensive and detailed',
            'max_tokens': 2500,
            'style': 'Use longer paragraphs (4-5 sentences each). Include detailed explanations, examples, and case studies.',
            'structure': 'Introduction, 4-5 main sections, Conclusion'
        },
        'comprehensive': {
            'word_count': 'EXACTLY 2000+ words',
            'sections': 'EXACTLY 6+ main sections',
            'detail_level': 'extremely comprehensive with extensive detail',
            'max_tokens': 3500,
            'style': 'Use comprehensive paragraphs (5+ sentences each). Include extensive examples, case studies, and detailed analysis.',
            'structure': 'Introduction, 5+ main sections, Conclusion'
        }
    }
    return length_instructions.get(content_length, length_instructions['medium'])

def generate_full_article(keyword, title, product="Files.com", content_length="medium"):
    """Generate a full article based on keyword and title using OpenAI"""
    print(f"🤖 OpenAI API: Generating full article for keyword: '{keyword}' with title: '{title}' for product: '{product}' with length: '{content_length}'")
    
    length_config = get_content_length_instructions(content_length)
    
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
    
    # Try multiple times to get the right length
    max_attempts = 3
    for attempt in range(max_attempts):
        try:
            # Adjust temperature and max_tokens based on attempt
            temperature = 0.7 if attempt == 0 else 0.8
            # Cap max_tokens at 4000 to avoid API errors
            max_tokens = min(length_config['max_tokens'], 4000) if attempt == 0 else min(int(length_config['max_tokens'] * 1.2), 4000)
            
            # Create more aggressive prompts for retries
            if attempt > 0:
                system_prompt = f"You are an expert content writer specializing in SEO articles for {product}. Write {length_config['detail_level']}, well-structured articles in markdown format that are specifically tailored for {product}'s audience, brand voice, and expertise. {length_config['style']} Use a balanced mix of paragraph text and bulleted lists to improve readability and engagement. Include headings, subheadings, bullet points, and engaging content that provides real value to {product}'s readers and potential customers. EXPAND EVERY SECTION WITH MORE DETAIL!"
                user_prompt = f"Write a {length_config['detail_level']} article about '{keyword}' with the title '{title}' for {product}'s website. The article should have {length_config['sections']}. Follow this structure: {length_config['structure']}. Write the article in markdown format with proper headings (H1, H2, H3). {length_config['style']} Include practical tips, examples, and actionable advice that are relevant to {product}'s audience and expertise. The content should reflect {product}'s brand voice and market position. Use bullet points for lists of features, benefits, steps, or tips, and use paragraphs for explanations and context. ADD MORE DETAIL TO EVERY SECTION! INCLUDE MORE EXAMPLES, CASE STUDIES, AND DETAILED EXPLANATIONS!"
            else:
                system_prompt = f"You are an expert content writer specializing in SEO articles for {product}. Write {length_config['detail_level']}, well-structured articles in markdown format that are specifically tailored for {product}'s audience, brand voice, and expertise. {length_config['style']} Use a balanced mix of paragraph text and bulleted lists to improve readability and engagement. Include headings, subheadings, bullet points, and engaging content that provides real value to {product}'s readers and potential customers."
                user_prompt = f"Write a {length_config['detail_level']} article about '{keyword}' with the title '{title}' for {product}'s website. The article should have {length_config['sections']}. Follow this structure: {length_config['structure']}. Write the article in markdown format with proper headings (H1, H2, H3). {length_config['style']} Include practical tips, examples, and actionable advice that are relevant to {product}'s audience and expertise. The content should reflect {product}'s brand voice and market position. Use bullet points for lists of features, benefits, steps, or tips, and use paragraphs for explanations and context. INCLUDE DETAILED EXAMPLES, CASE STUDIES, AND COMPREHENSIVE EXPLANATIONS FOR EACH SECTION."
            
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": user_prompt
                    }
                ],
                max_tokens=max_tokens,
                temperature=temperature
            )
            
            article_content = response.choices[0].message.content.strip()
            
            # Clean up any debugging info that might have been included in the content
            article_content = article_content.replace("📊 Generated article word count:", "")
            article_content = article_content.replace("words (target:", "")
            article_content = article_content.replace("EXACTLY", "")
            article_content = article_content.replace("words)", "")
            article_content = article_content.replace("(target:", "")
            article_content = article_content.replace(")", "")
            
            # Remove word count references from headlines and content
            import re
            # Remove word count patterns from headings only (e.g., "## Section Title (500 words)")
            article_content = re.sub(r'\([0-9]+\s*words?\)', '', article_content)
            # Remove specific word count debugging text that might appear
            article_content = re.sub(r'This section contains [0-9]+ words?', '', article_content)
            article_content = re.sub(r'Target: [0-9]+ words?', '', article_content)
            # Clean up any empty parentheses left behind
            article_content = re.sub(r'\s*\(\s*\)', '', article_content)
            
            word_count = len(article_content.split())
            
            # Check if we meet the minimum word count requirements (more realistic targets)
            min_words = {
                'short': 400,      # More realistic for short articles
                'medium': 600,     # More realistic for medium articles  
                'long': 900,       # More realistic for long articles
                'comprehensive': 1200  # More realistic for comprehensive articles
            }
            
            if word_count >= min_words.get(content_length, 800):
                print(f"✅ OpenAI API: Successfully generated full article for '{keyword}' for {product} (attempt {attempt + 1})")
                print(f"📊 Generated article word count: {word_count} words (target: {length_config['word_count']})")
                return article_content
            else:
                print(f"⚠️ Attempt {attempt + 1}: Generated {word_count} words (target: {length_config['word_count']}) - Too short, retrying...")
                if attempt == max_attempts - 1:
                    print(f"⚠️ Final attempt: Using generated content despite being short")
                    return article_content
                    
        except Exception as e:
            print(f"❌ OpenAI API Error generating full article (attempt {attempt + 1}): {e}")
            if attempt == max_attempts - 1:
                print(f"🔄 Falling back to template for keyword: '{keyword}' for {product}")
                # Fallback to template if all attempts fail
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