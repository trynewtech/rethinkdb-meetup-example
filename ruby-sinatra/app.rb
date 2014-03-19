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
  host = 'localhost'
  port = 28015
  db = 'trynewtech'
  auth_key = 'authkey'

  connection = r.connect(:host => host,
                         :port => port,
                         :db => db,
                         :auth_key => auth_key)

  # TODO: #3. Test it by running this file and visiting http://localhost:4567

  get '/users' do
    # TODO: #4. Get all users
    # Hint: The RethinkDB query will return an interable object
    @users = {}

    slim :users
  end

  # TODO: #5. Visit http://localhost:4567/users in the browser to test #4

  def get_user_id
    # TODO: #6. Complete the function to return your user id
    user_id = 'Put your user ID here'
  end

  post '/post' do
    post = {
      :title => params[:title],
      :slug => slugify(params[:title]),
      :text => params[:text],
      :user_id => get_user_id
    }

    # TODO: #7. Save the post to the database and get the resulting ID
    # Hint: Use "post_info" in your query
    # Hint: Get the ID from the result of the query

    post_id = ''

    # Note: This redirects, so you'll have to complete #8 before testing this
    redirect '/post/' + post_id
  end

  get '/post/:id' do
    post_id = params[:id]

    # TODO: #8. Get the post by its id (use post_id)
    @post = {}

    slim :post
  end

  # TODO: #9. Visit http://localhost:4567/post and create a few posts

  get '/posts' do
    # TODO: #10. Get all posts

    @posts = {}

    slim :posts
  end

  # TODO: #11. Visit http://localhost:4567/posts to see everyone's posts so far

  get '/user/:id/posts' do
    user_id = params[:id]

    # TODO: #12. Get all posts by a user using the provided "user_id" variable

    @posts = {}

    slim :posts
  end

  # TODO: #13. Visit the users page again and click on a user to see their posts

  #
  # CONGRATULATIONS
  # You've completed the beginner challenges.
  # Now see if you can complete the following!
  #

  # TODO: #14. Visit the Rethinkdb interface again to see how the data is being
  # stored. Note: this is a shared database, please respect each others' data.

  # Displays the post given it's title slug
  get '/post/title/:slug' do
    post_slug = params[:slug]

    # TODO: #15. Get a post by its slug by using the "post_slug" variable

    @post = {}

    slim :post
  end

  # TODO: #16. Visit a page and click on the "friendly URL" link to test it

  # Displays the post and additional details, i.e. the author information
  get '/post/:id/details' do
    post_id = params[:id]

    # TODO: #17. Get the post by its id (use postId), and get the authors information
    # Hint: Use a table join

    @post = {}
    @user = {}

    slim :post
  end

  # TODO: #18. Go back to a post page and visit the "Post details" at the bottom

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
