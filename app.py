from flask import Flask, render_template, send_from_directory
import json, os

app = Flask(__name__, static_folder='static', template_folder='templates')

def load_content():
    # Load editable content from data/content.json
    # Use os.path.dirname(__file__) for robust pathing in deployment
    here = os.path.join(os.path.dirname(__file__), 'data', 'content.json')
    if os.path.exists(here):
        with open(here, 'r', encoding='utf-8') as f:
            return json.load(f)
    # Fallback content (simplified for brevity)
    return {
        "name": "Shehan Ford", 
        "title": "Developer", 
        "about": "Fallback content loaded.", 
        "skills": [], 
        "projects": [], 
        "experience": [], 
        "education": [],
        "contact": {"email":"default@example.com", "resume_file": "Shehan Ford Resume.pdf"}
    }

CONTENT = load_content()

# --- Security and Configuration ---
# Security: Used for sessions/cookies. Set from environment variable.
app.secret_key = os.environ.get('SECRET_KEY', 'a_temporary_dev_key_for_local_use')
# -----------------------------------

@app.route('/')
def index():
    return render_template('index.html', content=CONTENT)

# Serve resume using the dynamic filename
@app.route('/resume')
def resume():
    # Safely retrieve filename from CONTENT['contact']
    filename = CONTENT['contact'].get('resume_file', 'Shehan Ford Resume.pdf')
    # Use app.static_folder for a reliable path
    return send_from_directory(app.static_folder, filename)

# Custom 404 Error Handler (Defined before __main__ block)
@app.errorhandler(404)
def page_not_found(e):
    # Pass the content data to the 404 template
    return render_template('404.html', content=CONTENT), 404

if __name__ == '__main__':
    # Use environment variable to control debug mode
    is_dev = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=is_dev)