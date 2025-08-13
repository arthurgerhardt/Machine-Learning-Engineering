from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import Base

# Criação da aplicação Flask
def create_app():
    app = Flask(__name__)

    # Configuração do banco de dados SQLite
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meu_banco.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicialização da extensão SQLAlchemy
    db = SQLAlchemy(app)

    # Criação das tabelas no contexto da aplicação
    with app.app_context():
        Base.metadata.create_all(bind=db.engine)

    return app

# Execução da aplicação
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)