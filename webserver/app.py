from flask import Flask, render_template, redirect, request


app = Flask(__name__)

@app.route('/')
def hello():
    return redirect("/court2")
    return "Hello, World!"

@app.route("/court")
def court():
    return render_template("court.html")

@app.route("/court2")
def court2():
    return render_template("court2.html")

@app.route("/api/github-webhook", methods=["POST"])
def github_webhook():
    payload = request.get_json()

    print(payload)

if __name__ == '__main__':
    app.run(debug=True)
