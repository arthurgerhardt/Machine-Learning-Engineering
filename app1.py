from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

# Configurações da Aplicação


app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)

swagger = Swagger(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(88), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username
        }


print(app.config['SECRET_KEY'])
print(app.config['SQLALCHEMY_DATABASE_URI'])
print(app.config['SWAGGER'])
print(app.config['CACHE_TYPE'])

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"error": "Dados incompletos"}), 400

    if User.query.filter_by(username=data['username']).first():
        return jsonify({"error": "Usuário já existe"}), 409

    new_user = User(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.to_dict()), 201

@app.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()

    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"error": "Dados incompletos"}), 400

    user = User.query.filter_by(username=data['username'], password=data['password']).first()
    if not user:
        return jsonify({"error": "Credenciais inválidas"}), 401

    return jsonify(user.to_dict()), 200

@app.route('/')
def main():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)