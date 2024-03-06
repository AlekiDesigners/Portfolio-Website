from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/About')
def about():
  return render_template("about.html")
