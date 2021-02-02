from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First Post content',
        'date_posted': 'Febuary 01, 2020'
    },
    {
        'author': 'John Doe',
        'title': 'Blog Post 2',
        'content': 'Second Post content',
        'date_posted': 'Febuary 02, 2020'
    }
]

@app.route("/")
@app.route("/home")
def homepage():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title='About')

if __name__ == '__main__':
    app.run(debug=True) 