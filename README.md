# SEO Content Generator

A modern, streamlined web application for generating complete SEO content in one click. Enter keywords and get full articles with titles, meta descriptions, and more.

## ✨ Features

- **One-Step Generation**: Generate complete content (title, article, meta title, meta description) in a single click
- **Clean, Modern UI**: Beautiful, responsive interface with intuitive design
- **Multiple Keywords**: Work with multiple keywords simultaneously
- **Export Functionality**: Export all generated content as a markdown file
- **Preview Mode**: Preview articles in a formatted modal
- **Copy to Clipboard**: Easy copying of individual content pieces
- **Product Selection**: Choose from different products (Files.com, ExaVault, ExpanDrive)

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Programmatic_SEO_Generator
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Set up environment variables**
   Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Start the development server**
   ```bash
   npm run dev
   ```

5. **Open your browser**
   Navigate to `http://localhost:5173`

## 🎯 How to Use

1. **Enter Keywords**: Add your target keywords in the input fields
2. **Select Product**: Choose the product/brand for content generation
3. **Generate Content**: Click "Generate Content" to create all SEO content at once
4. **Review & Copy**: Preview, copy, or export your generated content
5. **Export All**: Use the "Export All" button to download all completed content

## 🛠️ Technology Stack

- **Frontend**: React + Vite + Tailwind CSS
- **Backend**: Python with OpenAI API
- **Deployment**: Vercel
- **AI**: OpenAI GPT-3.5-turbo

## 📁 Project Structure

```
├── src/
│   ├── App.jsx              # Main application component
│   ├── components/ui/       # Reusable UI components
│   └── ...
├── api/
│   ├── generate_content.py  # Main content generation endpoint
│   ├── health.py           # Health check endpoint
│   └── ...
├── content_with_ai.py      # AI content generation functions
└── ...
```

## 🔧 API Endpoints

- `POST /api/generate_content` - Generate complete SEO content
- `GET /api/health` - Health check endpoint

## 🎨 UI Improvements

- **Simplified Workflow**: Removed the two-step process (brief → article)
- **Card-Based Layout**: Clean, organized content cards
- **Modern Color Scheme**: Professional blue/indigo gradient design
- **Responsive Design**: Works perfectly on desktop and mobile
- **Status Indicators**: Clear visual feedback on content generation status
- **Export Features**: Bulk export functionality for all generated content

## 📝 Content Generation

The application generates:
- **Article Title**: SEO-optimized, engaging titles
- **Full Article**: Comprehensive, well-structured content (1500+ words)
- **Meta Title**: SEO-optimized meta titles (under 60 characters)
- **Meta Description**: Compelling meta descriptions (under 160 characters)

## 🚀 Deployment

The application is configured for deployment on Vercel:

1. Connect your repository to Vercel
2. Set environment variables in Vercel dashboard
3. Deploy automatically on push to main branch

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License.
