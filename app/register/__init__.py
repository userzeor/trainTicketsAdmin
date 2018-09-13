from flask import Blueprint

register = Blueprint('register', __name__)
from app.register import views