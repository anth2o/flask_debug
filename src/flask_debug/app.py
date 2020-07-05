from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")

@app.route('/', methods=['GET'])
def index():
    files = [{"name": "test"}]
    return render_template("template.html", data=files)
