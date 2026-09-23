from flask import Flask 

app = Flask(__name__)

@app.route("/")

def home():
    return "<h1>This Laptop is not for General use!! Please Leave it Alone</h1>"

app.run(debug=True)