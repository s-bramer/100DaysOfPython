from flask import Flask, render_template
from datetime import date
import requests


current_year = date.today().year
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("portfolio.html", year=current_year)

@app.route('/blog')
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)
if __name__ == "__main__":
    app.run()
