import os
from flask import Flask


def creat_app(test_config=None):
  '''Create and configure the app.'''
  app = Flask(__name__, instance_relative_config=True)


if test_config is None:
  # load the instance config, if it exists, when not testing
  app.config.from_pyfile('config.py', silent=True)
else:
  # load the test config if passed in
  app.config.from_mapping(test_config)

# Ensure the instance folder exists
try:
  os.makedirs(app.instance_path)
except OSError:
  pass


@app.route("/")
def home():
  return render_template("home.html")


@app.route("/about/")
def about():
  return render_template("about.html")


return app

app = creat_app()
