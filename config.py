import os

# Configurações da Aplicação
class Config:
    SECRET_KEY = 'sua_chave_secreta'
    SQLALCHEMY_DATABASE_URI = (
    'mssql+pyodbc://sa:Yehoshua2025@localhost:1433/master?driver=ODBC+Driver+17+for+SQL+Server'
)

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER = {'title': 'Catálogo de Receitas Gourmet', 'uiversion': 3}
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 300  # Tempo de expiração do cache em segundos (opcional)