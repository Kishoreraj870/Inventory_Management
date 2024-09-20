from flask import Flask
from flask_cors import CORS
from routes import auth
from db import get_db
from routes import inventory 


app = Flask(__name__)

# Load configuration settings from the config.py file
app.config.from_pyfile('config.py')
CORS(app, resources={r"/*": {"origins": "*"}})  # Allows all origins


db= get_db
# Register Blueprints (auth) to organize the routes.
# The 'auth' routes will be prefixed with '/api/auth')
app.register_blueprint(auth.bp, url_prefix='/api/auth')
app.register_blueprint(inventory.bp, url_prefix='/api')  
app.register_blueprint(inventory.pro, url_prefix='/api')
app.register_blueprint(inventory.supplier_route, url_prefix='/api')
app.register_blueprint(inventory.sale_route, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)










































































































































































