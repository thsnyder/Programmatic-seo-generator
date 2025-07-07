# SEO Content Generator

A full-stack web application for generating SEO content briefs and complete articles from keywords. Created by Tom for Files.com.

## Features

- **Keyword Input**: Add keywords to generate content for
- **Content Brief Generation**: Automatically generate content briefs from keywords
- **Article Title Generation**: Create compelling article titles
- **Full Article Generation**: Generate complete articles based on briefs and titles
- **Spreadsheet-style Interface**: Manage multiple content pieces in a table format
- **AI-Powered**: Uses OpenAI GPT for intelligent content generation

## Tech Stack

- **Frontend**: React + Vite + Tailwind CSS
- **Backend**: Flask (Python) + OpenAI API
- **Deployment**: Vercel (Full-stack)

## Quick Start

### Local Development

1. **Install Dependencies**
   ```bash
   npm install
   pip install -r requirements.txt
   ```

2. **Set Environment Variables**
   Create a `.env.local` file:
   ```bash
   OPENAI_API_KEY=your_openai_api_key_here
   ```

3. **Start Development Servers**
   ```bash
   # Terminal 1: Start backend
   python3 vercel_app.py
   
   # Terminal 2: Start frontend
   npm run dev
   ```

4. **Access the Application**
   - Frontend: `http://localhost:5173`
   - Backend: `http://localhost:5000`

## Deployment to Vercel

### Prerequisites
- Vercel account
- OpenAI API key

### Deployment Steps

1. **Install Vercel CLI** (optional)
   ```bash
   npm i -g vercel
   ```

2. **Set Environment Variables in Vercel**
   ```bash
   vercel env add OPENAI_API_KEY
   vercel env add OPENAI_SECRET_KEY
   ```

3. **Deploy**
   ```bash
   vercel --prod
   ```

   Or connect your GitHub repository to Vercel for automatic deployments.

### Environment Variables Required

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |
| `OPENAI_SECRET_KEY` | Alternative name for OpenAI API key | Yes |
| `PRODUCT_NAME` | Custom product name (defaults to "Files.com") | No |

### Vercel Configuration

The project includes `vercel.json` with:
- Python Flask backend for API routes
- Static build for React frontend
- Proper routing configuration
- 30-second function timeout for AI generation

## API Endpoints

- `POST /api/generate_brief_title` - Generate content brief and article title
- `POST /api/generate_article` - Generate full article with meta data
- `GET /api/health` - Health check endpoint

## Usage

1. Add a keyword in the "Keyword" column
2. Click "Generate Brief" to create a content brief and article title
3. Click "Write Article" to generate the full article
4. Add more rows to manage multiple content pieces

## Project Structure

```
├── src/                    # Frontend source code
│   ├── components/        # React components
│   ├── App.jsx           # Main app component
│   └── main.jsx          # React entry point
├── vercel_app.py         # Flask backend server (Vercel deployment)
├── content_with_ai.py    # Content generation logic with OpenAI
├── requirements.txt      # Python dependencies
├── package.json          # Node.js dependencies
├── vercel.json          # Vercel configuration
└── vite.config.js        # Vite configuration
```

## Development

- The frontend uses Vite for fast development
- The backend uses Flask with CORS enabled
- API calls are made directly to the backend during development
- Hot reload is enabled for both frontend and backend

## Troubleshooting

### Common Issues

1. **OpenAI API Key Not Found**
   - Ensure `OPENAI_API_KEY` is set in your environment variables
   - The app will fall back to template-based content if no API key is provided

2. **Build Errors**
   - Make sure all dependencies are installed: `npm install && pip install -r requirements.txt`
   - Check that Node.js version is 16+ and Python version is 3.8+

3. **API Timeout**
   - Vercel functions have a 30-second timeout
   - For longer content generation, consider breaking into smaller chunks

## License

Created by Tom for Files.com
