from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash
from flasgger import Swagger

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['JWT_SECRET_KEY'] = 'sua-chave-secreta-aqui'  # Troque por uma chave segura em produção
db = SQLAlchemy(app)
jwt = JWTManager(app)
# 🔷 Adiciona Flasgger
swagger = Swagger(app)

# Modelo de Usuário
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Modelo de Receita
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    time_minutes = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Registro de usuário
@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"error": "Username and password are required"}), 400

    if User.query.filter_by(username=data['username']).first():
        return jsonify({"error": "User already exists"}), 400

    hashed_password = generate_password_hash(data['password'])
    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User created successfully"}), 201

# Login e geração de token
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"error": "Username and password are required"}), 400

    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password, data['password']):
        # ⚠️ CORREÇÃO: garantir que o identity seja uma string
        token = create_access_token(identity=str(user.id))
        return jsonify({
            "access_token": token,
            "username": user.username
        }), 200

    return jsonify({"error": "Invalid credentials"}), 401

# Rota protegida para teste
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    return jsonify({"msg": f"Usuário com ID {current_user_id} acessou a rota protegida."}), 200

# Criar receita vinculada ao usuário logado
@app.route('/recipes', methods=['POST'])
@jwt_required()
def create_recipe():
    data = request.get_json()
    required_fields = ['title', 'ingredients', 'time_minutes']
    if not data or not all(field in data for field in required_fields):
        return jsonify({"error": "All fields are required"}), 400

    current_user_id = get_jwt_identity()
    new_recipe = Recipe(
        title=data['title'],
        ingredients=data['ingredients'],
        time_minutes=data['time_minutes'],
        user_id=int(current_user_id)  # Garantir que user_id seja inteiro
    )
    db.session.add(new_recipe)
    db.session.commit()
    return jsonify({"msg": "Recipe created"}), 201

# Listar receitas do usuário logado
@app.route('/my_recipes', methods=['GET'])
@jwt_required()
def get_my_recipes():
    current_user_id = get_jwt_identity()
    recipes = Recipe.query.filter_by(user_id=int(current_user_id)).all()
    output = [
        {
            "title": r.title,
            "ingredients": r.ingredients,
            "time_minutes": r.time_minutes
        } for r in recipes
    ]
    return jsonify(output), 200

@app.route('/recipes/<int:recipe_id>', methods=['PUT'])
@jwt_required()
def update_recipe(recipe_id):
    """
    Atualiza uma receita existente.

    ---
    security:
      - BearerAuth: []
    parameters:
      - in: path
        name: recipe_id
        required: true
        type: integer
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
            ingredients:
              type: string
            time_minutes:
              type: integer
    responses:
      200:
        description: Receita atualizada
      404:
        description: Receita não encontrada ou acesso negado
      401:
        description: Token não fornecido ou inválido
    """
    current_user_id = get_jwt_identity()
    recipe = Recipe.query.filter_by(id=recipe_id, user_id=int(current_user_id)).first()

    if not recipe:
        return jsonify({"error": "Receita não encontrada ou acesso negado"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Corpo da requisição inválido"}), 400

    if 'title' in data:
        recipe.title = data['title']
    if 'ingredients' in data:
        recipe.ingredients = data['ingredients']
    if 'time_minutes' in data:
        recipe.time_minutes = data['time_minutes']

    db.session.commit()
    return jsonify({"msg": "Recipe updated"}), 200
@app.route('/recipes/<int:recipe_id>', methods=['DELETE'])
@jwt_required()
def delete_recipe(recipe_id):   
    """
    Deleta uma receita existente.

    ---
    security:
      - BearerAuth: []
    parameters:
      - in: path
        name: recipe_id
        required: true
        type: integer           
    responses:
      200:
        description: Receita deletada
      404:
        description: Receita não encontrada ou acesso negado
      401:
        description: Token não fornecido ou inválido
    """
    current_user_id = get_jwt_identity()
    recipe = Recipe.query.filter_by(id=recipe_id, user_id=int(current_user_id)).first() 
    if not recipe:
        return jsonify({"error": "Receita não encontrada ou acesso negado"}), 404 
    db.session.delete(recipe)
    db.session.commit()
    return jsonify({"msg": "Recipe deleted"}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Database created!")
    app.run(debug=True)
