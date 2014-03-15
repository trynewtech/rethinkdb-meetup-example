from flask import Flask, render_template, request
import rethinkdb as r
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/post')
def make_post():
    return render_template('makepost.html')

'''
### DO THINGS HERE
'''

#TODO: #1 Look at the README to add yourself to the blog

#TODO: #2 make database connection
connection = r.connect()


@app.route('/users')
def users():
    #TODO: #3 get all users
    users = []

    return render_template('users.html', users=users)


@app.route('/post', methods=['POST'])
def post_post():
    post_title = request.form['title']
    post_text = request.form['text']

    #TODO: #4 save the post
    post = {}

    return redirect(url_for('post', id=post['id']))


@app.route('/post/<id>')
def post(id):
    #TODO: #5 get the post by its id (use id)
    post = {}

    return render_template('post.html', post=post)


@app.route('/posts')
def posts():
    #TODO: #6 get all posts
    posts = []

    return render_template('posts.html', posts=posts)


@app.route('/user/<id>/posts')
def user_posts(id):
    #TODO: #7 get all posts by a user (use their id)
    posts = []

    return render_template('posts.html', posts=posts)


# ADVANCED
# get post by title
@app.route('/post/title/<title>')
def post_by_title(title):
    #TODO: #8 get the post by its title
    post = {}

    return render_template('post.html', post=post)


# get post and author (user) information
@app.route('/post/<id>/details')
def post_details(id):
    #TODO: #9 get the post by its id (use id) (you did this before :)
    post = {}

    #TODO: #10 get the user's information
    user = {}

    return render_template('post.html', post=post, user=user)


'''
### OKAY STOP DOING THINGS
'''


if __name__ == "__main__":
    app.run(debug=True)
