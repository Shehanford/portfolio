from flask import Flask, render_template, url_for, send_from_directory
import json, os

app = Flask(__name__)

def load_content():
    path = os.path.join(app.root_path, "data", "content.json")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

content = load_content()

@app.route("/")
def index():
    return render_template("index.html", content=content)

@app.route("/resume")
def resume():
    return send_from_directory("static", "Shehan Resume.pdf")

if __name__ == "__main__":
    app.run(debug=True)
