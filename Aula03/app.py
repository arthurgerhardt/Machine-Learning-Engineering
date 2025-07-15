from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

app = Flask(__name__)
db = SQLAlchemy(app)  
jwt = JWTManager(app)  

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

@app.route('/register', methods=['POST'])
def register_user():
    # Register a new user.
    data = request.get_json()
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"error": "User already exists"}), 400
# Removed invalid block. The registration endpoint is already defined above.
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg": "User created"}), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

if __name__ == '__main__':
    
    app.run(debug=True)
                                