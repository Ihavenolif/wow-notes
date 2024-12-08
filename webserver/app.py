from flask import Flask, render_template, redirect, request
import subprocess


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
    # yes, i know this can get ddosed easily
    # no, i dont care
    
    payload = request.get_json()

    try:
        if not payload["action"] == "completed":
            print("job not completed")
            return "no"
        
        if not payload["repoitory"]["id"] == 898164860:
            print("wrong repository")
            return "no"
        
        print("restarting")
        subprocess.Popen("/usr/bin/sudo /bin/systemctl restart iao-strats", shell=True, stdout=subprocess.PIPE)
        return "ok"


    except:
        print("wrong payload")
        print(request.get_data())
        return "fuckoff"

if __name__ == '__main__':
    app.run(debug=True)
