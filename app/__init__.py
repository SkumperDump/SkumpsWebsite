import markdown, utils
from flask import (Flask, render_template)

nav_list = ['homepage', 'projects', 'blog']

contactInfo = utils.open_file("app/static/md/contact.md")
contactInfo = markdown.markdown(contactInfo)

app = Flask(__name__)

@app.route('/')
def homepage():
    # markdown -> html
    # need to use {{FOO | safe}} in jinja template to prevent auto-escaping
    content = utils.open_file("app/static/md/index.md")
    content = markdown.markdown(content)
    return render_template("index.html", navigation=nav_list, content=content, contactInfo=contactInfo)

@app.route('/projects')
def projects():
    content = utils.open_file("app/static/md/projects.md")
    content = markdown.markdown(content)
    return render_template("projects.html", navigation=nav_list, content=content, contactInfo=contactInfo)

@app.route('/blog')
def blog():
    return render_template("blog.html", navigation=nav_list)
