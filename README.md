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

## Production export

Run `python export_static.py --output docs` to render the portfolio into `docs/`
with its stylesheet, JavaScript, image, and favicon. GitHub Pages publishes the
`docs` folder on `main`. Commit and push the regenerated files after changes to
the content, templates, or assets. Relative asset URLs support the repository's
URL path, and `.nojekyll` tells Pages to serve the exported files directly.

Production URL: https://jaswanthjanga99-portfolio.github.io/

## Hosting the Flask application
Flask remains available for local development. `python export_static.py` also
exports to `dist/` for hosting at a domain root. The production portfolio needs
no server because its content is rendered at export time and its interactions
run in the browser.

