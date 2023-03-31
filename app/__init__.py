import utils
from flask import (Flask, render_template)
from pathlib import Path

nav_list = ['homepage', 'projects', 'blog', 'books']

markdownDir = str(Path.home())
markdownDir += "/SkumpsWebsite/app/static/md/{}"

# turns markdown file into string of html
contactInfo = utils.mdToHtml(markdownDir.format("contact.md"))

app = Flask(__name__)

@app.route('/')
def homepage():
    # markdown -> html
    # need to use {{FOO | safe}} in jinja template to prevent auto-escaping
    content = utils.mdToHtml(markdownDir.format("index.md"))
    return render_template("index.html", navigation=nav_list, content=content, contactInfo=contactInfo)

@app.route('/projects')
def projects():
    content = utils.mdToHtml(markdownDir.format("projects.md"))
    return render_template("projects.html", navigation=nav_list, content=content, contactInfo=contactInfo)

@app.route('/blog')
def blog():
    content = utils.mdToHtml(markdownDir.format("blog.md"))
    return render_template("blog.html", navigation=nav_list, content=content, contactInfo=contactInfo)

@app.route('/books')
def books():
    content = utils.mdToHtml(markdownDir.format("books.md"))
    return render_template("books.html", navigation=nav_list, content=content, contactInfo=contactInfo)
