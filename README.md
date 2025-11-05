# Postfix Trainer 🎮

An interactive web application for learning and practicing Reverse Polish Notation (Postfix Notation).

## Features

- **📚 Learn Mode**: Step-by-step walkthrough of converting infix expressions to postfix notation
- **🎯 Practice Mode**: Random problems with difficulty levels (Easy, Medium, Hard)
- **📊 Progress Tracking**: Track your accuracy, streaks, and level up as you improve
- **🎨 Beautiful UI**: Modern, responsive design with TailwindCSS

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

## Project Structure

```
postfix_trainer/
├── app.py                 # Flask application (local development)
├── api/
│   └── index.py          # Vercel serverless function entry point
├── vercel.json            # Vercel configuration
├── requirements.txt       # Python dependencies
├── static/
│   ├── style.css         # Custom CSS styles
│   └── scripts.js        # Shared JavaScript utilities
├── templates/
│   ├── index.html        # Home page
│   ├── learn.html        # Learn mode
│   ├── practice.html     # Practice mode
│   └── results.html      # Progress tracking
└── utils/
    ├── __init__.py       # Package initialization
    ├── postfix.py        # Postfix evaluation utilities
    ├── infix_to_postfix.py  # Conversion utilities
    └── problems.py        # Problem generation
```

## Usage

1. **Home Page**: Start here to learn about postfix notation and see examples
2. **Learn Mode**: Enter an infix expression and see step-by-step conversion to postfix
3. **Practice Mode**: Solve randomly generated problems and track your progress
4. **Results Page**: View your statistics and level progression

## How Postfix Notation Works

Postfix notation (also called Reverse Polish Notation) places operators after their operands:

- **Infix**: `3 + 4 * 5`
- **Postfix**: `3 4 5 * +`

To evaluate postfix:
1. Read from left to right
2. Push operands to a stack
3. When you see an operator, pop two operands, perform the operation, and push the result
4. The final value on the stack is the answer

## Deployment to Vercel

This app is configured for deployment on Vercel through GitHub.

### Prerequisites
- A GitHub account
- A Vercel account (sign up at [vercel.com](https://vercel.com))

### Deployment Steps

1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/your-repo-name.git
   git push -u origin main
   ```

2. **Deploy on Vercel:**
   - Sign in to your Vercel account
   - Click "New Project"
   - Import your GitHub repository
   - Vercel will automatically detect the Flask app and `vercel.json` configuration
   - Click "Deploy"

3. **Environment Variables (Optional):**
   - In Vercel project settings, you can add a `SECRET_KEY` environment variable for session security
   - If not set, the app will use a default key

### Important Notes

- **Sessions**: Vercel serverless functions are stateless. Sessions may not persist between function invocations in the same way as a traditional server. Stats are stored in session cookies, which work for individual user sessions.
- **Static Files**: Static files in `/static/` are automatically served by Vercel
- **Templates**: Templates in `/templates/` are served by the Flask app

## License

MIT License

