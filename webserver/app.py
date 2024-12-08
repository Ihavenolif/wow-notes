from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route("/court")
def court():
    return render_template("court.html")

@app.route("/court2")
def court2():
    return render_template("court2.html")

if __name__ == '__main__':
    app.run(debug=True)
