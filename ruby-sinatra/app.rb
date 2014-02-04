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

  #TODO: Make database connection
  connection = RethinkDB::Connection.new()

  post '/post' do
    post_info = params[:post]

    #TODO: save the post
    post = {}

    redirect '/post' + post.id
  end

  get '/post/:id' do
    post_id = params[:id]

    #TODO: get the post by its id (use postId)
    @post = {}

    #Optional TODO: get the users information
    @user = {}

    slim :post
  end

  get '/users' do
    #TODO: get all users
    @users = []

    slim :users
  end

  get '/posts' do
    #TODO: get all posts
    @posts = []

    slim :posts
  end

  get '/user/:id/posts' do
    user_id = params[:id]

    #TODO: get all posts by a user (user their userId)
    @posts = []

    slim :posts
  end

  # ADVANCED
  # get post by title
  get '/post/title/:title' do
    post_title = params[:title]

    #TODO: get the post by its title
    @post = {}

    slim :post
  end

  #
  # OK STOP DOING THINGS
  #

end
