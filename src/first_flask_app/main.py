from flask import Blueprint, render_template, url_for  # noqa: F401

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return 'Hello World!'
