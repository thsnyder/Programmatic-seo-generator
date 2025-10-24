#!/usr/bin/env python3
"""
Test script to verify API endpoints work correctly
"""
import sys
import os
import json
import urllib.request
import urllib.parse

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

def test_content_functions():
    """Test the content generation functions directly"""
    print("🧪 Testing content generation functions...")
    
    try:
        from content_with_ai import generate_article_title, generate_full_article, generate_meta_title, generate_meta_description
        
        # Test with sample data
        keyword = "test keyword"
        product = "Files.com"
        
        print(f"  Testing with keyword: '{keyword}' for product: '{product}'")
        
        # Test each function
        title = generate_article_title(keyword, product)
        print(f"  ✅ Article title: {title[:50]}...")
        
        article = generate_full_article(keyword, title, product, "medium")
        print(f"  ✅ Full article: {len(article)} characters")
        
        meta_title = generate_meta_title(keyword, product)
        print(f"  ✅ Meta title: {meta_title}")
        
        meta_desc = generate_meta_description(keyword, product)
        print(f"  ✅ Meta description: {meta_desc[:50]}...")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Error testing content functions: {e}")
        return False

def test_api_endpoint():
    """Test the API endpoint structure"""
    print("\n🧪 Testing API endpoint structure...")
    
    try:
        # Test the generate_content module
        from api.generate_content import handler
        
        print("  ✅ API endpoint module imports successfully")
        print("  ✅ Handler class exists")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Error testing API endpoint: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 Starting API tests...\n")
    
    # Test content functions
    content_ok = test_content_functions()
    
    # Test API structure
    api_ok = test_api_endpoint()
    
    print(f"\n📊 Test Results:")
    print(f"  Content Functions: {'✅ PASS' if content_ok else '❌ FAIL'}")
    print(f"  API Structure: {'✅ PASS' if api_ok else '❌ FAIL'}")
    
    if content_ok and api_ok:
        print("\n🎉 All tests passed! The API should work on Vercel.")
        return True
    else:
        print("\n⚠️  Some tests failed. Check the errors above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
