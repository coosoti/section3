from app import Flask

app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def home():
    return 'Welcome to the homepage!'

# Define a route with a variable part
@app.route('/user/<username>')
def user_profile(username):
    return f'Welcome, {username}!'

# Define a route with multiple variable parts
@app.route('/post/<int:post_id>/<post_slug>')
def show_post(post_id, post_slug):
    return f'Post #{post_id}: {post_slug}'

if __name__ == '__main__':
    app.run(debug=True)
