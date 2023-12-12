from icecream import ic
from flask import Flask


ic (print ("Helllllo"))


# Create a Flask web application
app = Flask(__name__)

# Define a route and its associated function
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the Flask application if this script is executed
if __name__ == '__main__':
    app.run(debug=True)
