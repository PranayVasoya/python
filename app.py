from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Return an HTML string with inline style
    return """
    <div style="text-align:center; font-family:sans-serif; padding:40px;">
        <h1 style="color:blue;">Hello, World!</h1>
        <p>This page has some basic inline styling.</p>
    </div>
    """

# Add this new function for the about page
@app.route('/about')
def about():
    return 'This is the About Page.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)