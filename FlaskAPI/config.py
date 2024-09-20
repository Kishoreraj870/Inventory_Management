import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'your_default_secret_key')
