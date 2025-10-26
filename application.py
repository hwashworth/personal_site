from flask import Flask, render_template, request, redirect, url_for

application = Flask(__name__)

# Example placeholder projects — replace with your real project entries.
projects = [
    {"title": "Project Alpha", "subtitle": "CloudOps demo", "url": "#"},
    {"title": "Project Beta",  "subtitle": "K8s monitor",  "url": "#"},
    {"title": "Project Gamma", "subtitle": "Auto-healer",  "url": "#"},
    {"title": "Project Delta", "subtitle": "Cost tracker",  "url": "#"},
]

@application.route("/")
def home():
    return render_template("index.html", name="Hunter Ashworth", title="Product Development & Cloud Operations")

@application.route("/projects")
def project_list():
    return render_template("projects.html", projects=projects)

@application.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == "POST":
        # For portfolio demo: just redirect (you can plug email service or form backend)
        return redirect(url_for("home"))
    return render_template("contact.html")


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000)
