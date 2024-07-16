from flask import Flask
from env_loader import load_env_variables

# Load the environment variables
env_vars = load_env_variables()

# Initialize the Flask app
app = Flask(__name__)

# Import routes
from app.routes import *

# Run the application
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=('PORT'))
