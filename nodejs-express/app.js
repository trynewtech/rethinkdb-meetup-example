var express = require('express');
var http = require('http');
var path = require('path');
var rethinkdb = require('rethinkdb');

var app = express();

// all environments
app.set('port', process.env.PORT || 3000);
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');
app.use(express.favicon());
app.use(express.logger('dev'));
app.use(express.json());
app.use(express.urlencoded());
app.use(express.methodOverride());
app.use(app.router);
app.use(express.static(path.join(__dirname, 'public')));

// development only
if ('development' == app.get('env')) {
  app.use(express.errorHandler());
}

/*
// DO THINGS HERE:
*/

app.get('/', function(req, res) {
  res.render('index', { title: 'Express' });
});

app.get('/post', function(req, res) {
  res.render('makepost');
});

app.post('/post', function(req, res) {
  postInfo = req.body.post
  //TODO: save the post
  post = {};
  res.redirect('/post/' + post.id);
});

app.get('/post/:id', function(req, res) {
  postId = req.params.id;
  //TODO: get the post by it's id (use postId)
  post = {};
  res.render('post', { post: post });
});

app.get('/users', function(req, res) {
  //TODO: get all users
  users = [];
  res.render('users', { users: users });
});

app.get('/posts', function(req, res) {
  //TODO: get all posts
  posts = [];
  res.render('posts', { posts: posts });
});

app.get('/user/:id/posts', function(req, res) {
  userId = req.params.id;
  //TODO: get all posts by a user (use their userId)
  posts = [];
  res.render('posts', { posts: posts });
});


// ADVANCED
// get post by title
app.get('/post/title/:title', function(req, res) {
  postTitle = req.params.title;
  //TODO: get the post by it's title
  post = {};
  res.render('post', { post: post });
});

/*
// OK STOP DOING THINGS
*/

http.createServer(app).listen(app.get('port'), function(){
  console.log('Express server listening on port ' + app.get('port'));
});
