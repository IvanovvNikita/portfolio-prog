from flask import Flask

from LR8.Controllers import Controller, StoreUserController, UserController
from LR8.Models.IvanovvNikita import IvanovNikita
from LR8.Views import UserView

app = Flask(__name__)


@app.route('/')
def index():
    controller = Controller()
    return controller.get_user_data()


@app.route('/ivanov')
def user():
    user = IvanovNikita()
    view = UserView()
    controller = UserController(user, view)
    return controller.get_user_data()


@app.route('/json')
def json():
    user = IvanovNikita()
    controller = StoreUserController(user)
    return controller.get_user_data()


app.run(host="0.0.0.0", debug=True)
