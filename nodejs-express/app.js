var express = require('express');
var http = require('http');
var path = require('path');
var r = require('rethinkdb');
var app = express();
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
if ('development' == app.get('env')) {app.use(express.errorHandler());}
app.get('/', function(req, res) {res.render('index');});
app.get('/post', function(req, res) {res.render('makepost');});

/*
// DO THINGS HERE:
*/

//TODO: #1 look at the README to add yourself to the blog

//TODO: #2 make database connection
var connection = null;
r.connect({/* Database connection goes here */}, function(err, conn) {
  if (err) throw err;
  connection = conn;
});

app.get('/users', function(req, res) {
  //TODO: #3 get all users
  var users = [];

  res.render('users', { users: users });
});

app.post('/post', function(req, res) {
  var postInfo = req.body.post;

  //TODO: #4 save the post
  var post = {};

  res.redirect('/post/' + post.id);
});

app.get('/post/:id', function(req, res) {
  var postId = req.params.id;

  //TODO: #5 get the post by its id (use postId)
  var post = {};

  res.render('post', { post: post });
});

app.get('/posts', function(req, res) {
  //TODO: #6 get all posts
  var posts = [];

  res.render('posts', { posts: posts });
});

app.get('/user/:id/posts', function(req, res) {
  var userId = req.params.id;

  //TODO: #7 get all posts by a user (use their userId)
  var posts = [];

  res.render('posts', { posts: posts });
});

// ADVANCED
// get post by title
app.get('/post/title/:title', function(req, res) {
  var postTitle = req.params.title;

  //TODO: #8 get the post by its title
  var post = {};

  res.render('post', { post: post });
});

// get post and author (user) information
app.get('/post/:id/details', function(req, res) {
  var postId = req.params.id;

  //TODO: #9 get the post by its id (use postId) (you did this before :)
  var post = {};

  //TODO: #10 get the user's information
  var user = {};

  res.render('post', { post: post, user: user });
});

/*
// OK STOP DOING THINGS
*/

http.createServer(app).listen(app.get('port'), function(){console.log('Express server listening on port ' + app.get('port'));});
