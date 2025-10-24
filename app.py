from flask import Flask, render_template

app = Flask(__name__)

# Example project data (could later be pulled from GitHub API)
projects = [
    {"name": "AWS Cost Tracker", "desc": "Tracks daily AWS costs using boto3."},
    {"name": "Kubernetes Health Monitor", "desc": "Watches for unhealthy pods and restarts them automatically."},
    {"name": "EC2 Auto-Healer", "desc": "Detects and replaces unhealthy instances."},
]

@app.route("/")
def home():
    return render_template("templates/index.html")

@app.route("/projects")
def project_list():
    return render_template("templates/projects.html", projects=projects)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
