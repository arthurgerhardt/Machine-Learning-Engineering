import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'sua_chave_secreta')
    CACHE_TYPE = 'simple'
    SWAGGER = {
        'title': 'Catálogo de Receitas Gourmet',
        'uiversion': 3
    }
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///recipes.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'sua_chave_jwt_secreta')