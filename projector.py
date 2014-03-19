import rethinkdb as r
from werkzeug.local import LocalProxy
from flask import Flask, g, request, render_template, redirect, url_for


# Flask application
app = Flask(__name__)
app.config.from_object('settings')
app.config.from_envvar('SETTINGS_MODULE', silent=True)
app.config.from_pyfile('settings_local.py', silent=True)
# Database
def get_db():
    if not hasattr(g, 'db'):
        g.db = r.connect(
            host=app.config['DATABASE_HOST'],
            port=app.config['DATABASE_PORT'],
            db=app.config['DATABASE_DB'],
            auth_key=app.config['DATABASE_AUTH_KEY'],
        )
    return g.db
db = LocalProxy(get_db)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user-list')
def user_list():
    #users = [
    #    {
    #        'name': 'One',
    #    },
    #]
    cursor = r.table('users').run(db)
    users = list(cursor)
    return render_template('user-list.html', users=users)


@app.route('/post-list')
def post_list():
    #posts = [
    #    {
    #        'title': 'Title!',
    #    }
    #]
    #cursor = r.table('posts')\
    #    .eq_join('user_id', r.table('users'))\
    #    .filter(r.row['left']['id'] == id)\
    #    .run(connection)
    #post_and_user = list(cursor)
    #post = post_and_user[0]['left']
    #user = post_and_user[0]['right']
    cursor = r.table('posts').run(db)
    posts = list(cursor)
    return render_template('post-list.html', posts=posts)


# Run development server
if __name__ == '__main__':
    app.run(app.config['HOST'], app.config['PORT'], app.debug)
