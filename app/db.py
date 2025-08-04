import psycopg2
from flask import g

def init_db(app):
    def get_db():
        if 'db' not in g:
            g.db = psycopg2.connect(app.config['DATABASE_URL'])
        return g.db
    app.teardown_appcontext(close_db)
    app.get_db = get_db

def close_db(error=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
