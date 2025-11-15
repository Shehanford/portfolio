from flask import Flask, render_template, url_for, send_from_directory, jsonify
import json
import os

app = Flask(__name__)

# Load site content from JSON (so you can edit without changing code)
def load_content():
    path = os.path.join(app.root_path, 'data', 'content.json')
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    # fallback: minimal content
    return {
        "name": "Shehan Roshantha",
        "title": "Finance & Software Enthusiast",
        "about": "Finance professional studying Software Engineering. Blend of accounting, ERP tools, and programming skills.",
        "contact": {
            "email": "shehanrford@gmail.com",
            "phone": "0705246616",
            "location": "Wattala, Sri Lanka"
        },
        "projects": [
            {"title": "Project A", "desc": "Short description", "link": "#"},
            {"title": "Project B", "desc": "Short description", "link": "#"}
        ],
        "experience": [
            {"role": "Associate – F&A", "org": "WNS Global Services", "date": "Mar 2025 – Present"},
            {"role": "Finance Trainee", "org": "Resus Energy PLC", "date": "Aug 2024 – Feb 2025"}
        ]
    }

CONTENT = load_content()

@app.route('/')
def index():
    return render_template('index.html', content=CONTENT)

# If you add a resume PDF file in static, serve it
@app.route('/resume')
def resume():
    return send_from_directory('static', 'Shehan Ford Resume.pdf', as_attachment=False)

if __name__ == '__main__':
    app.run(debug=True)
