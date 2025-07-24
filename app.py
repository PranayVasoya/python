from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Add this new function for the about page
@app.route('/about')
def about():
    return 'This is the About Page.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)