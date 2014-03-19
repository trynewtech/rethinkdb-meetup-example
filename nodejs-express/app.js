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
// COMPLETE THE FOLLOWING TODOS:
*/

// TODO: #1. Look at the README to add yourself to the blog

// TODO: #2. Make database connection
// Hint: Set the following variables to actual values provided by the organizers
var host = '';
var port = 0;
var db = '';
var authKey = '';

var connection = null; // Leave this null please :)
r.connect({host: host, port: port, db: db, authKey: authKey}, function(err, conn) {
  if (err) throw err;
  connection = conn;
});

// TODO: #3. Test it by running "npm start" and visiting http://localhost:3000

// REMEMBER!
// If you need help, visit http://rethinkdb.com/docs/guide/javascript/
// Or raise your hand / ask a nearby mentor to come help you if you get stuck.

app.get('/users', function(req, res) {
  // TODO: #4. Get all users
  // Hint: The RethinkDB query will return a cursor
  var users = [];

  // Put this in the final callback
  res.render('users', { users: users });

});

// TODO: #5. Visit http://localhost:3000/users in the browser to test #4

var getUser = function(username) {
  // TODO: #6. Complete the function to get your user from the database
  var user = {};
  return user;
};

app.post('/post', function(req, res) {
  var postInfo = req.body.post;
  postInfo.slug = slugify(postInfo.title);

  // TODO: #6. Save the post to the database and get the resulting ID
  // Hint: Use "postInfo" in your query
  // Hint: Get the ID from the result of the query
  var postId = '';

  res.redirect('/post/' + postId);
});

app.get('/post/:id', function(req, res) {
  var postId = req.params.id;

  // TODO: #7. Get the post by its ID (use postId)
  var post = {};

  res.render('post', { post: post });
});

// TODO: #8. Visit http://localhost:3000/post and create a few posts

app.get('/posts', function(req, res) {
  // TODO: #9. Get all posts
  var posts = [];

  // Put this in the final callback
  res.render('posts', { posts: posts });
});

// TODO: #10. Visit http://localhost:3000/posts to see everyone's posts so far

app.get('/user/:id/posts', function(req, res) {
  var userId = req.params.id;

  // TODO: #11. Get all posts by a user using the provided "userId" variable
  var posts = [];

  // As always, put this in the final callback
  res.render('posts', { posts: posts });
});

// TODO: #12. Visit the users page again and click on a user to see their posts


/*
// CONGRATULATIONS
// You've completed the beginner challenges.
// Now see if you can complete the following!
*/


// TODO: #13. Visit the RethinkDB interface again to see how the data is being
// stored. Note: this is a shared database, please respect each others' data.


// Displays the post given it's title slug
app.get('/post/title/:slug', function(req, res) {
  var postSlug = req.params.slug;

  // TODO: #14. Get a post by its slug by using the postSlug variable
  var post = {};

  res.render('post', { post: post });
});

// TODO: #15. Visit a page and click on the "friendly URL" link to test it

// Displays the post and additional details, i.e. the author information
app.get('/post/:id/details', function(req, res) {
  var postId = req.params.id;

  // TODO: #16. Get the post by its id (use postId), and get the authors information
  // Hint: Use a table join
  var post = {};
  var user = {};

  res.render('post', { post: post, user: user });
});

// TODO: #17. Go back to a post page and visit the "Post details" at the bottom

/*
// CONGRATULATIONS
// You've completed the intermediate challenges.
// Take a breather. Talk to a nearby mentor when you're ready for more.
*/

// Helpers
var slugify = function(title) {
  return title.replace(/\s+/g , '-').toLowerCase();
};

http.createServer(app).listen(app.get('port'), function(){console.log('Express server listening on port ' + app.get('port'));});
