from flask import Flask

# Configurações da Aplicação
# class Config:
#     SECRET_KEY = 'sua_chave_secreta'
#     CACHE_TYPE = 'simple'
#     SWAGGER = {
#         'title': 'Catálogo de Receitas Gourmet',
#         'uiversion': 3
#     }
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///recipes.db'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     JWT_SECRET_KEY = 'sua_chave_jwt_secreta'

app = Flask(__name__)
app.config.from_object('config.Config')

print(app.config['SECRET_KEY'])
print(app.config['SQLALCHEMY_DATABASE_URI'])
print(app.config['SWAGGER'])
print(app.config['CACHE_TYPE'])

@app.route('/')
def main():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)