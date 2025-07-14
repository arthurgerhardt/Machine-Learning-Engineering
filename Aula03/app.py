from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

db = SQLAlchemy(app)  
jwt = JWTManager(app)                 
                                