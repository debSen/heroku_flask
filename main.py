from flask import Flask, send_from_directory, render_template
import os

app = Flask(__name__)

posts = [
    {
        'author':'Deb',
        'title': 'post 1',
        'content': 'my first blog post',
        'date_posted': 'February 6th, 2022'
    },
    {
        'author':'Deb',
        'title': 'post 2',
        'content': 'my second blog post',
        'date_posted': 'February 7th, 2022'
    },   
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

if __name__ == "__main__":
    app.secret_key = 'ItIsASecret'
    app.debug = True
    app.run()