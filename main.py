from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/index.html')
def dashboard():
    return homepage()

@app.route('/maps.html')
def maps():
    return render_template("maps.html")

@app.route('/works.html')
def works():
    return render_template("works.html")

if __name__ == "__main__":
    app.run()