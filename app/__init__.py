import markdown, utils
from flask import (Flask, render_template)

nav_list = ['homepage', 'projects', 'blog']

app = Flask(__name__)

@app.route('/')
def homepage():
    # markdown -> html
    # need to use {{FOO | safe}} in jinja template to prevent auto-escaping
    content = utils.open_file("app/static/md/index.md")
    return render_template("index.html", navigation=nav_list, content=markdown.markdown(content))

@app.route('/projects')
def projects():
    return render_template("projects.html", navigation=nav_list)

@app.route('/blog')
def blog():
    return render_template("blog.html", navigation=nav_list)
