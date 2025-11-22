from flask import Flask, render_template, send_from_directory
import json, os

app = Flask(__name__, static_folder='static', template_folder='templates')

def load_content():
    # Load editable content from data/content.json
    here = os.path.join(app.root_path, 'data', 'content.json')
    if os.path.exists(here):
        with open(here, 'r', encoding='utf-8') as f:
            return json.load(f)
    # fallback (shouldn't be needed)
    return {
        "name": "Shehan Roshantha",
        "title": "Associate – F&A | Software Engineering (reading)",
        "about": "Finance professional with a BBA in Finance and a growing software skillset. Experienced in SAP, Wise Cloud, reconciliations, and month-end processes. I build practical tools to automate accounting workflows and analyze financial data.",
        "skills": ["Accounting","SAP","Wise Cloud","Python","Flask","Excel","Data Analysis"],
        "projects": [],
        "experience": [],
        "contact": {"email":"shehanrford@gmail.com","phone":"0705246616","location":"Wattala, Sri Lanka","linkedin":"https://linkedin.com/in/shehan-roshantha-90811b312"}
    }

CONTENT = load_content()

# Import os if you haven't already
import os 
# ... your existing imports ...

# ... CONTENT = load_content() ...

# Security: Used for sessions/cookies. We use an environment variable for deployment.
app.secret_key = os.environ.get('SECRET_KEY', 'a_temporary_dev_key_for_local_use')


@app.route('/')
def index():
    return render_template('index.html', content=CONTENT)

# Serve resume (place your PDF at static/Shehan Ford Resume.pdf)
@app.route('/resume')
def resume():
    return send_from_directory('static', 'Shehan Ford Resume.pdf')

if __name__ == '__main__':
    app.run(debug=True)

# Custom 404 Error Handler
from flask import render_template

@app.errorhandler(404)
def page_not_found(e):
    # Pass the content data to the 404 template so it can use the name/contact info in the base template
    return render_template('404.html', content=CONTENT), 404