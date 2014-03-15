from flask import Flask, render_template, request
import rethinkdb as r


app = Flask(__name__)


'''
### DO THINGS HERE
'''

# TODO: #1 Look at the README to add yourself to the blog

# TODO: #2 Make database connection
host = ''
port = 0
connection = r.connect(host, port)


@app.route('/users')
def users():
    # TODO: #3 Get all users
    users = []

    return render_template('users.html', users=users)


@app.route('/post', methods=['POST'])
def post_post():
    post_title = request.form['title']
    post_text = request.form['text']

    # TODO: #4 Save the post to the database
    post = {}

    return redirect(url_for('post', id=post['id']))


@app.route('/post/<id>')
def post(id):
    # TODO: #5 Get the post by its id (use id)
    post = {}

    return render_template('post.html', post=post)


@app.route('/posts')
def posts():
    # TODO: #6 Get all posts
    posts = []

    return render_template('posts.html', posts=posts)


@app.route('/user/<id>/posts')
def user_posts(id):
    # TODO: #7 Get all posts by a user (use their id)
    posts = []

    return render_template('posts.html', posts=posts)


# --- ADVANCED ---

@app.route('/post/<title>')
def post_by_title(title):
    """Displays the post given its title."""

    # TODO: #8 Get the post by its title
    post = {}

    return render_template('post.html', post=post)


@app.route('/post/<id>/details')
def post_details(id):
    """Displays the post and additional details, i.e. the author information."""

    # TODO: #9 Get the post by its id (use id) (you did this before :)
    post = {}

    # TODO: #10 Get the user's information
    user = {}

    return render_template('post.html', post=post, user=user)


'''
### OKAY STOP DOING THINGS
'''


# Views you don't care about
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/post')
def make_post():
    return render_template('makepost.html')


if __name__ == "__main__":
    app.run(debug=True)
