import rethinkdb as r
from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)


"""
### COMPLETE THE FOLLOWING TODOS
"""


# TODO: #1. Look at the README to add yourself to the blog


# TODO: #2. Make database connection
# Hint: Set the following variables to actual values provided by the organizers
host = 'localhost'
port = 28015
db = 'trynewtech'
auth_key = 'authkey'
connection = r.connect(host, port, db, auth_key)


# TODO: #3. Test it by running this script and visiting http://localhost:5000


# REMEMBER!
# If you need help, visit http://rethinkdb.com/docs/guide/python/
# Or raise your hand / ask a nearby mentor to come help you if you get stuck.


@app.route('/users')
def users():
    # TODO: #4. Get all users
    # Hint: The RethinkDB query will return an iterable
    users = {}

    return render_template('users.html', users=users)


# TODO: #5. Visit http://localhost:5000/users in the browser to test #4


def get_user_id():
    # TODO: #6. Complete the function to return your user id
    user_id = 'Put your user ID here'
    return user_id


@app.route('/post', methods=['POST'])
def post_post():
    post_title = request.form['title']
    post_slug = slugify(post_title)
    post_text = request.form['text']
    post_user_id = get_user_id()


    # TODO: #7. Save the post to the database and get the resulting ID
    # Hint: Use "post_title", "post_slug", and "post_text" in your query
    # Hint: Get the ID from the result of the query
    post_id = ''


    # Note: This redirects, so you'll have to complete #8 before testing this
    return redirect(url_for('post', id=post_id))


@app.route('/post/<id>')
def post(id):
    # TODO: #8. Get the post by its ID by using the provided "id" argument

    post = {}

    return render_template('post.html', post=post)


# TODO: #9. Visit http://localhost:5000/post and create a few posts


@app.route('/posts')
def posts():
    # TODO: #10. Get all posts

    posts = {}

    return render_template('posts.html', posts=posts)


# TODO: #11. Visit http://localhost:5000/posts to see everyone's posts so far


@app.route('/user/<id>')
def user_posts(id):
    # TODO: #12. Get all posts from a specific user by using the provided "id" argument

    posts = {}

    return render_template('posts.html', posts=posts)


# TODO: #13. Visit the users page again and click on a user to see their posts


"""
### CONGRATULATIONS
### You've completed the beginner challenges.
### Now see if you can complete the following!
"""


# TODO: #14. Visit the RethinkDB interface again to see how the data is being
# stored. Note: this is a shared database, please respect each others' data.


@app.route('/post/title/<slug>')
def post_by_slug(slug):
    """Displays the post given its slug."""

    # TODO: #15. Get a post by its slug by using the provided "slug" argument

    post = {}

    return render_template('post.html', post=post)


# TODO: #16. Visit a post page and click on the "friendly URL" link to test it


@app.route('/post/<id>/details')
def post_details(id):
    """Displays the post and additional details, i.e. the author information."""

    # TODO: #17. Get the post and its user from the provided post ID
    # Hint: Use a table join

    post = {}
    user = {}

    return render_template('post.html', post=post, user=user)


# TODO: #18. Go back to a post page and visit the "Post details" at the bottom


"""
### CONGRATULATIONS!
### You've completed the intermediate challenges.
### Take a breather. Talk to a nearby mentor when you're ready for more.
"""


# Views you don't care about
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/post')
def new_post():
    return render_template('new_post.html')


# Helpers
def slugify(title):
    return title.replace(' ', '-').lower()


if __name__ == '__main__':
    app.run(debug=True)
