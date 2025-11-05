# Vercel Deployment Guide

## Quick Start

1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git push -u origin main
   ```

2. **Deploy on Vercel:**
   - Go to [vercel.com](https://vercel.com)
   - Sign in (or create account)
   - Click "New Project"
   - Import your GitHub repository
   - Vercel will automatically detect the configuration
   - Click "Deploy"

3. **Optional: Set Environment Variables:**
   - In Vercel project settings → Environment Variables
   - Add `SECRET_KEY` with a secure random string (optional, defaults to a built-in key)

## Files Added for Vercel

- `vercel.json` - Vercel configuration file
- `api/index.py` - Serverless function entry point
- `.gitignore` - Git ignore file

## Configuration Details

- **Entry Point**: `api/index.py` (Flask app configured for Vercel)
- **Python Runtime**: Uses `@vercel/python`
- **Static Files**: Automatically served from `/static/` folder
- **Templates**: Served by Flask from `/templates/` folder

## Troubleshooting

### Static Files Not Loading
- Ensure static files are in the `static/` folder
- Check that file paths in templates use `{{ url_for('static', filename='...') }}`

### Sessions Not Working
- Sessions use cookies and work per user session
- Stats reset between browser sessions (this is expected behavior on serverless)

### Import Errors
- Ensure all files in `utils/` are committed
- Check that `__init__.py` exists in `utils/` folder

## Testing Locally

You can still test locally using:
```bash
python app.py
```

The app will run on `http://localhost:5000`

## Notes

- **Local Development**: Use `app.py` in the root directory
- **Vercel Deployment**: Uses `api/index.py` as the entry point
- Both files contain the same routes, but `api/index.py` is configured for Vercel's serverless environment

