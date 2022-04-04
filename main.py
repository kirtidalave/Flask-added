from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<h1>Welcome</h1>"

@app.route("/contact")
def Contact_page():
    return "ContactbPage"

@app.route("/home")
def HomePage():
    return "Home Page"

@app.route("/gallery")
def gallery():
    return "Insert your picture"

if __name__=="__main__":
    app.run()