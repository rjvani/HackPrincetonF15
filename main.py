from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("main.html")

@app.route('/main.html')
def mainpage():
    return render_template("main.html")

@app.route('/index.html')
def dashboard():
    return render_template("index.html")

@app.route('/maps.html')
def maps():
    return render_template("maps.html")

@app.route('/works.html')
def works():
    return render_template("works.html")

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/future.html')
def future():
    return render_template("future.html")


@app.route('/home.html')
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run()