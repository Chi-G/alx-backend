#!/usr/bin/env python3
"""Create a get_locale function with the babel.localeselector decorator
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


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


def get_user(login_as):
    """get user"""
    try:
        return users.get(int(login_as))
    except Exception:
        return


@app.before_request
def before_request():
    """Before requests"""
    g.user = get_user(request.args.get('login_as'))


@babel.localeselector
def get_locale():
    """get_locale function"""
    locale = request.args.get("locale")
    if locale:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.route('/', strict_slashes=False)
def index():
    """Route 2.index.html"""
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
