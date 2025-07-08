from flask import Flask


# Configurações da Aplicação

app = Flask(__name__)

app. config.from_object ('config')

print(app.config['SECRET_KEY'])
print (app.config['SQLALCHEMY_DATABASE_URI'])
print (app.config ['SWAGGER' ])
print (app. config ['CACHE_TYPE' ])

@app.route('/')
def main():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)