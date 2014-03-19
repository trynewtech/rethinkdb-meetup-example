import rethinkdb as r
from flask import Flask, request, render_template, redirect, url_for


# Flask application
app = Flask(__name__)
app.config.from_object('settings')
app.config.from_envvar('SETTINGS_MODULE', silent=True)
app.config.from_pyfile('settings_local.py', silent=True)


@app.route('/')
def index():
    return render_template('index.html')


# Run development server
if __name__ == '__main__':
    app.run(app.config['HOST'], app.config['PORT'], app.debug)
