require 'sinatra/base'
require 'sinatra/reloader'
require 'slim'
require 'rethinkdb'

class Rethink < Sinatra::Base
  configure(:development){ register Sinatra::Reloader }
  r = RethinkDB::RQL.new

  get '/' do slim :index end
  get '/post' do slim :makepost end

  #
  # DO THINGS HERE
  #
  
  #TODO: #1 look at the README to add yourself to the blog

  #TODO: #2 make database connection
  connection = RethinkDB::Connection.new()

  get '/users' do
    #TODO: #3 get all users
    @users = []

    slim :users
  end

  post '/post' do
    post_info = params[:post]

    #TODO: #4 save the post
    post = {}

    redirect '/post' + post.id
  end

  get '/post/:id' do
    post_id = params[:id]

    #TODO: #5 get the post by its id (use postId)
    @post = {}

    slim :post
  end


  get '/posts' do
    #TODO: #6 get all posts
    @posts = []

    slim :posts
  end

  get '/user/:id/posts' do
    user_id = params[:id]

    #TODO: #7 get all posts by a user (user their userId)
    @posts = []

    slim :posts
  end

  # ADVANCED
  # get post by title
  get '/post/title/:title' do
    post_title = params[:title]

    #TODO: #8 get the post by its title
    @post = {}

    slim :post
  end

  # get post and author (user) information
  get '/post/:id/details' do
    post_id = params[:id]

    #TODO: #9 get the post by its id (use postId) (you did this before :)
    @post = {}

    #TODO: #10 get the users information
    @user = {}

    slim :post
  end

  #
  # OK STOP DOING THINGS
  #

end
