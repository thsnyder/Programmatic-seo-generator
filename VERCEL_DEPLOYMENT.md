# Vercel Deployment Guide

## Overview
This app is now configured to work with Vercel's serverless functions. The backend API endpoints are deployed as individual serverless functions, and the frontend is built as a static site.

## What's Fixed

### 1. Backend API Structure
- ✅ All API endpoints are now properly configured as Vercel serverless functions
- ✅ Each endpoint (`/api/health`, `/api/generate_content`, `/api/generate_article`, `/api/generate_brief_title`) works independently
- ✅ CORS headers are properly set for cross-origin requests

### 2. Local Development
- ✅ Created `vercel_app.py` Flask application for local development
- ✅ Updated `start.sh` to use the Flask app for local testing
- ✅ All dependencies are properly configured

### 3. Deployment Configuration
- ✅ Updated `vercel.json` with proper routing and function configuration
- ✅ Python runtime is set to 3.9
- ✅ Frontend builds to `dist` directory
- ✅ API routes are properly mapped

## How to Deploy

### Option 1: Deploy via Vercel CLI
```bash
# Install Vercel CLI if you haven't already
npm i -g vercel

# Deploy from your project directory
vercel

# For production deployment
vercel --prod
```

### Option 2: Deploy via Vercel Dashboard
1. Push your code to GitHub
2. Connect your repository to Vercel
3. Vercel will automatically detect the configuration and deploy

## Environment Variables
Make sure to set these environment variables in your Vercel dashboard:

- `OPENAI_SECRET_KEY` or `OPENAI_API_KEY` - Your OpenAI API key

## Local Development
To run locally:

```bash
# Install dependencies
npm install
pip install -r requirements.txt

# Start both frontend and backend
npm run dev:full
```

This will start:
- Frontend: http://localhost:5173
- Backend: http://localhost:5000

## API Endpoints

### Health Check
- **GET** `/api/health` - Check if the server is running

### Content Generation
- **POST** `/api/generate_content` - Generate all content (title, article, meta tags)
- **POST** `/api/generate_article` - Generate article with custom title/brief
- **POST** `/api/generate_brief_title` - Generate content brief and title

### Request Format
All POST endpoints expect JSON with:
```json
{
  "keyword": "your keyword",
  "product": "Files.com",
  "contentLength": "medium" // for generate_content
}
```

## Troubleshooting

### If API calls fail:
1. Check that environment variables are set in Vercel
2. Verify the API endpoints are accessible at `/api/*`
3. Check Vercel function logs for errors

### If frontend can't connect to backend:
1. Ensure you're using the correct API URLs (should be relative paths like `/api/health`)
2. Check that CORS headers are properly set
3. Verify the Vercel routing configuration

## File Structure
```
├── api/                    # Vercel serverless functions
│   ├── health.py
│   ├── generate_content.py
│   ├── generate_article.py
│   └── generate_brief_title.py
├── src/                    # React frontend
├── dist/                   # Built frontend (generated)
├── vercel.json            # Vercel configuration
├── vercel_app.py          # Flask app for local development
├── content_with_ai.py     # AI content generation functions
└── requirements.txt        # Python dependencies
```

Your app should now work perfectly on Vercel! 🚀
