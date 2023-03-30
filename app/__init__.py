import utils
from flask import (Flask, render_template)

nav_list = ['homepage', 'projects', 'blog', 'books']
markdownDir = "app/static/md/{}.md"

# turns markdown file into string of html
contactInfo = utils.mdToHtml(markdownDir.format("contact"))

app = Flask(__name__)

@app.route('/')
def homepage():
    # markdown -> html
    # need to use {{FOO | safe}} in jinja template to prevent auto-escaping
    content = utils.mdToHtml(markdownDir.format("index"))
    return render_template("index.html", navigation=nav_list, content=content, contactInfo=contactInfo)

@app.route('/projects')
def projects():
    content = utils.mdToHtml(markdownDir.format("projects"))
    return render_template("projects.html", navigation=nav_list, content=content, contactInfo=contactInfo)

@app.route('/blog')
def blog():
    content = utils.mdToHtml(markdownDir.format("blog"))
    return render_template("blog.html", navigation=nav_list, content=content, contactInfo=contactInfo)

@app.route('/books')
def books():
    content = utils.mdToHtml(markdownDir.format("books"))
    return render_template("books.html", navigation=nav_list, content=content, contactInfo=contactInfo)
