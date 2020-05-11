from flask import Flask
from flask_restplus import Api
from api.controller.userController import UserController

app = Flask(__name__)
api = Api(app)

controller = UserController()
@api.route('/users')
def get(self):
  return controller.get()

'''
@api.route('/users/<int:id>')
def get(self, id):
  return controller.get()
'''

def initialize_app(app):
  app.config['RESTPLUS_VALIDATE'] = True
  app.config['ERROR_404_HELP'] = False

def main():
  initialize_app(app)
  app.run(host='127.0.0.1', port=5000, debug=True)

if __name__ == "__main__":
    main()