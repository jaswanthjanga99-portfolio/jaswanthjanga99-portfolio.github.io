# AI/ML Portfolio (Flask)

A simple Flask web app that serves a portfolio page.

## Local development

1. Create and activate a virtual environment (recommended):

- Windows (PowerShell):
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

2. Install dependencies:
```powershell
pip install -r requirements.txt
```

3. Run the app:
```powershell
python app.py
```

4. Open the app in your browser (usually):
- http://127.0.0.1:5000

## Project structure
- `app.py` - Flask entrypoint and routes
- `templates/index.html` - Portfolio HTML template
- `static/profile.jpg` - Profile image served from `/static/profile.jpg`

## Notes on GitHub Pages
This project is server-side Flask, so it is not directly compatible with GitHub Pages without additional setup (e.g., a build + static export). For a live deployment, use a platform like Render/Railway/Fly.io/Heroku.

