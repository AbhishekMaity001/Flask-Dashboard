from application import app

@app.route("/home")
def home():
    return """<h1> Home Page </h1>"""