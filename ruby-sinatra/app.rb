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
  # COMPLETE THE FOLLOWING TODOS
  #
  
  # TODO: #1. Look at the README to add yourself to the blog

  # TODO: #2. Make database connection
  # Hint: Set the following variables to actual values provided by the organizers
=begin
  host = ''
  port = 0
  auth_key = ''
  db = ''

  connection = r.connect(:host => host,
                         :port => port,
                         :db => db,
                         :auth_key => auth_key)
=end

  # TODO: #3. Test it by running this file and visiting http://localhost:4567

  get '/users' do
    # TODO: #4. Get all users
    # Hint: The RethinkDB query will return an interable object
    @users = []

    slim :users
  end

  # TODO: #5. Visit http:localhost:4567/users in the browser to test #4

  post '/post' do
    post = {
      :title => params[:title],
      :slug => slugify(params[:title]),
      :text => params[:text]
    }

    # TODO: #6. Save the post to the database and get the resulting ID
    # Hint: Use "post_info" in your query
    # Hint: Get the ID from the result of the query
    post_id = ''

    redirect '/post' + post_id
  end

  get '/post/:id' do
    post_id = params[:id]

    # TODO: #7. Get the post by its id (use post_id)
    @post = {}

    slim :post
  end

  # TODO: #8. Visit http://localhost:4567/post and create a few posts

  get '/posts' do
    # TODO: #9. Get all posts
    @posts = []

    slim :posts
  end

  # TODO: #10. Visit http:localhost:4567/posts to see everyone's posts so far

  get '/user/:id/posts' do
    user_id = params[:id]

    # TODO: #11. Get all posts by a user using the provided "user_id" variable
    @posts = []

    slim :posts
  end

  #
  # CONGRATULATIONS
  # You've completed the beginner challenges.
  # Now see if you can complete the following!
  #
  
  # TODO: #13. Visit the Rethinkdb interface again to see how the data is being
  # stored. Note: this is a shared database, please respect each others' data.


  # Displays the post given it's title slug
  get '/post/title/:slug' do
    post_slug = params[:slug]

    # TODO: #14. Get a post by its slug by using the "post_slug" variable
    @post = {}

    slim :post
  end

  # TODO: #15. Visit a page and click on the "friendly URL" link to test it

  # Displays the post and additional details, i.e. the author information
  get '/post/:id/details' do
    post_id = params[:id]

    # TODO: #16. Get the post by its id (use postId), and get the authors information
    # Hint: Use a table join
    @post = {}
    @user = {}

    slim :post
  end

  # TODO: #17. Go back to a post page and visit the "Post details" at the bottom

  #
  # CONGRATULATIONS
  # You've completed the intermediate challenges.
  # Take a breather. Talk to a nearby mentor when you're ready for more.
  #
  
  # Helpers
  def slugify(title)
    title.gsub(' ', '-').downcase
  end

  run! if app_file == $0
end
