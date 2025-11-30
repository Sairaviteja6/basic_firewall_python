import sys
import os

# Absolute path to project root
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(PROJECT_ROOT)  # so 'firewall' module can be imported

from flask import Flask, render_template, request, redirect, url_for, flash, Response
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from firewall.logger import get_events
import json

app = Flask(__name__)
app.secret_key = "supersecretkey"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# Absolute path to rules.json
RULES_FILE = os.path.join(PROJECT_ROOT, "config", "rules.json")
CREDENTIALS = {"admin": "devara"}

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

def load_rules():
    with open(RULES_FILE, "r") as f:
        return json.load(f)

def save_rules(rules):
    with open(RULES_FILE, "w") as f:
        json.dump(rules, f, indent=4)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if CREDENTIALS.get(username) == password:
            user = User(username)
            login_user(user)
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid username or password")
    return render_template("login.html")

@app.route("/dashboard")
@login_required
def dashboard():
    rules = load_rules()
    return render_template("dashboard.html", rules=rules)

@app.route("/events")
@login_required
def events():
    def stream():
        while True:
            messages = get_events()
            for msg in messages:
                yield f"data: {msg}\n\n"
    return Response(stream(), mimetype="text/event-stream")

@app.route("/add_rule", methods=["POST"])
@login_required
def add_rule():
    rules = load_rules()
    r_type = request.form["type"]
    value = request.form["value"]
    if r_type in rules and value not in rules[r_type]:
        if r_type in ["allowed_ports"]:
            value = int(value)
        rules[r_type].append(value)
        save_rules(rules)
    return redirect(url_for("dashboard"))

@app.route("/remove_rule", methods=["POST"])
@login_required
def remove_rule():
    rules = load_rules()
    r_type = request.form["type"]
    value = request.form["value"]
    if r_type in rules:
        if r_type in ["allowed_ports"]:
            value = int(value)
        if value in rules[r_type]:
            rules[r_type].remove(value)
            save_rules(rules)
    return redirect(url_for("dashboard"))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)
