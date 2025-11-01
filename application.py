from flask import Flask, render_template, request, redirect, url_for

application = Flask(__name__)

@application.route("/")
def home():
    return render_template("index.html", name="Hunter Ashworth")

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=8080)
