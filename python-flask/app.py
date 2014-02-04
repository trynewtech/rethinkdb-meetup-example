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

#TODO: Make database connection
connection = r.connect()

@app.route('/post', methods=['POST'])
def post_post():
    post_title = request.form['title']
    post_text = request.form['text']

    #TODO: save the post
    post = {}

    return redirect(url_for('post', id=post['id']))

@app.route('/post/<id>')
def post(id):
    #TODO: get the post by its id (use id)
    post = {}

    #Optional TODO: get the user's information
    user = {}

    return render_template('post.html', post=post, user=user)

@app.route('/users')
def users():
    #TODO: get all users
    users = []

    return render_template('users.html', users=users)

@app.route('/posts')
def posts():
    #TODO: get all posts
    posts = []

    return render_template('posts.html', posts=posts)

@app.route('/user/<id>/posts')
def user_posts(id):
    #TODO: get all posts by a user (use their id)
    posts = []

    return render_template('posts.html', posts=posts)

@app.route('/post/title/<title>')
def post_by_title(title):
    #TODO: get the post by its title
    post = {}

    return render_template('post.html')

'''
### OKAY STOP DOING THINGS
'''

if __name__ == "__main__":
    app.run(debug=True)
