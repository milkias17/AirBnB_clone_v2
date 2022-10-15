#!/usr/bin/python3
"""Starts web application"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    return "C " + text.replace("_", " ")


@app.route("/python", strict_slashes=False)
def default_python_greeting():
    return "Python is cool"


@app.route("/python/<text>", strict_slashes=False)
def greeting_python(text):
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    val = "even" if n % 2 == 0 else "odd"
    return render_template("6-number_odd_or_even.html", val=val, n=n)


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
