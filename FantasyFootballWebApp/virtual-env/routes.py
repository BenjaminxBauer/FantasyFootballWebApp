from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/owner")
def owner():
    return render_template("owner.html")


if __name__ == "__main__":
    app.run(debug=True) 