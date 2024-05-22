from flask import Flask
app = Flask(__name__)

# Creating routes
@app.route("/")
def index():
    return """<h1> Test Page </h1>"""


if __name__ == '__main__':
    app.run(debug=True)