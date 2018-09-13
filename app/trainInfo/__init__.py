from flask import Blueprint

train = Blueprint('train', __name__)
from app.trainInfo import views