# SEO Content Generator

A full-stack web application for generating SEO content briefs and complete articles from keywords. Created by Tom for Files.com.

## Features

- **Keyword Input**: Add keywords to generate content for
- **Content Brief Generation**: Automatically generate content briefs from keywords
- **Article Title Generation**: Create compelling article titles
- **Full Article Generation**: Generate complete articles based on briefs and titles
- **Spreadsheet-style Interface**: Manage multiple content pieces in a table format

## Tech Stack

- **Frontend**: React + Vite + Tailwind CSS
- **Backend**: Flask (Python)
- **Database**: SQLite (optional)

## Setup Instructions

### Prerequisites

- Node.js (v16 or higher)
- Python (v3.8 or higher)
- pnpm (recommended) or npm

### Installation

1. **Install Frontend Dependencies**
   ```bash
   pnpm install
   ```

2. **Install Backend Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

#### Option 1: Development Mode (Recommended)

1. **Start the Backend Server**
   ```bash
   python main.py
   ```
   The Flask server will run on `http://localhost:5000`

2. **Start the Frontend Development Server**
   ```bash
   pnpm dev
   ```
   The React app will run on `http://localhost:5173`

3. **Access the Application**
   Open your browser and go to `http://localhost:5173`

#### Option 2: Production Build

1. **Build the Frontend**
   ```bash
   pnpm build
   ```

2. **Start the Backend Server**
   ```bash
   python main.py
   ```

3. **Access the Application**
   Open your browser and go to `http://localhost:5000`

## API Endpoints

- `POST /api/generate_brief_title` - Generate content brief and article title
- `POST /api/generate_article` - Generate full article
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
├── main.py               # Flask backend server
├── content.py            # Content generation logic
├── requirements.txt      # Python dependencies
├── package.json          # Node.js dependencies
└── vite.config.js        # Vite configuration
```

## Development

- The frontend uses Vite for fast development
- The backend uses Flask with CORS enabled
- API calls are proxied from frontend to backend during development
- Hot reload is enabled for both frontend and backend # Updated Thu Jul  3 16:06:47 CDT 2025
