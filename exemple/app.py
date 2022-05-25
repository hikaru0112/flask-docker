from flask import Flask, render_template

app = Flask(__name__)
app.config.update(
    SESSION_COOKIE_SAMESITE='lax',
)

@app.route("/")
def index():
    return "Test"

