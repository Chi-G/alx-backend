#!/usr/bin/env python3
"""Create a get_locale function with the babel.localeselector decorator.
Use request.accept_languages to determine the best
match with our supported languages
"""
from flask_babel import Babel
from flask import Flask, render_template, request

app = Flask(__name__)
babel = Babel(app)


class Config:
    """a Config class that has a LANGUAGES class
    attribute equal to ["en", "fr"]
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """get_locale function"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """Route 2.index.html"""
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
