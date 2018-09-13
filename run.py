from flask import Flask
from app.login import login as login_blueprint
from app.register import register as register_blueprint
from app.trainInfo import train as train_blueprint

app = Flask(__name__)

app.register_blueprint(login_blueprint, url_prefix='/login')
app.register_blueprint(register_blueprint, url_prefix='/register')
app.register_blueprint(train_blueprint, url_prefix='/train')

if __name__ == '__main__':
    app.run(host="192.168.2.213", port=10010)
