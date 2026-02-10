"""
WSGI Entry Point for Wilderness Destinations Chatbot
For deployment to Hostinger, PythonAnywhere, or other WSGI servers
"""

import sys
import os

# Add the backend directory to the Python path
sys.path.insert(0, os.path.dirname(__file__))

# Import the Flask app
from app import app as application

# For development/testing
if __name__ == "__main__":
    application.run(debug=False, host='0.0.0.0', port=5000)
