from flask import Blueprint, render_tepmpate

bp = Blueprint(__name__)


@bp.route('/')
def home():
    return render_template("home.html")

@bp.route('/about')
def about():
    return render_template("/about.html")

@bp.route("/contact")
def contact():
    return render_template("/contact")