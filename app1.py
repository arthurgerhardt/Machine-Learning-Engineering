from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Certifique-se de que o arquivo config.py existe ou defina a classe Config abaixo
# from config import Config

# Configurações da Aplicação

app = Flask(__name__)

app.config.from_object('config')  # ou 'Config' se você importar uma classe Config

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Banco de dados criado!")

print(app.config.get('SECRET_KEY'))
print(app.config.get('SQLALCHEMY_DATABASE_URI'))
print(app.config.get('SWAGGER'))
print(app.config.get('CACHE_TYPE'))

@app.route('/')
def main():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)