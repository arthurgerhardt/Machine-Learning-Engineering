from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

@app.route('/')
def home():
    return "Welcome to the Flask App!"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Banco de dados criado!")
        print(app.config['SECRET_KEY'])
        print(app.config['SQLALCHEMY_DATABASE_URI'])
        print(app.config['SWAGGER'])
        print(app.config['CACHE_TYPE'])
    app.run(debug=True)