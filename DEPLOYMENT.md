# Deployment Checklist for Vercel

## Pre-Deployment Checklist

### ✅ Environment Variables
- [ ] Set `OPENAI_SECRET_KEY` in Vercel environment variables
- [ ] Optionally set `PRODUCT_NAME` if you want to customize the product name

### ✅ Code Review
- [ ] All API endpoints are working locally
- [ ] Frontend builds successfully (`npm run build`)
- [ ] Backend runs without errors
- [ ] No hardcoded API keys in the code

### ✅ Dependencies
- [ ] `requirements.txt` is up to date
- [ ] `package.json` has all necessary dependencies
- [ ] `vercel.json` is properly configured

## Deployment Steps

### Option 1: Vercel CLI
```bash
# Install Vercel CLI
npm i -g vercel

# Login to Vercel
vercel login

# Set environment variables
vercel env add OPENAI_SECRET_KEY

# Deploy
vercel --prod
```

### Option 2: GitHub Integration
1. Push your code to GitHub
2. Connect your repository to Vercel
3. Set environment variables in Vercel dashboard
4. Deploy automatically on push

## Post-Deployment Verification

### ✅ Health Checks
- [ ] Visit your deployed URL
- [ ] Check `/api/health` endpoint
- [ ] Test content generation with a sample keyword
- [ ] Verify OpenAI API integration is working

### ✅ Functionality Tests
- [ ] Generate content brief
- [ ] Generate article title
- [ ] Generate full article
- [ ] Check that all UI components render correctly

## Troubleshooting

### Common Issues

1. **Build Fails**
   - Check Node.js version (16+ required)
   - Verify all dependencies are installed
   - Check for syntax errors in code

2. **API Timeout**
   - Vercel functions have 30-second timeout
   - Consider optimizing API calls
   - Break large operations into smaller chunks

3. **Environment Variables Not Working**
   - Ensure variables are set in Vercel dashboard
   - Check variable names match exactly
   - Redeploy after setting environment variables

4. **CORS Issues**
   - CORS is already configured in the Flask app
   - If issues persist, check domain configuration

## Performance Optimization

- [ ] Enable Vercel Edge Functions if needed
- [ ] Optimize bundle size
- [ ] Consider caching strategies
- [ ] Monitor function execution times

## Security

- [ ] No API keys in client-side code
- [ ] Environment variables properly secured
- [ ] CORS properly configured
- [ ] Input validation on API endpoints 