from flask_cors import CORS
from .db import init_db
from .routes import main
from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from dotenv import load_dotenv
    import os
    load_dotenv()
    app.config["DATABASE_URL"] = os.getenv("DATABASE_URL")
    
    init_db(app)
    app.register_blueprint(main)
    
    CORS(app)  # <- Add this

    return app
