from flask import Flask
from api.userController import UserController
#from api.userService import UserService
#from api.userRepository import UserRepository

app = Flask(__name__)

controller = UserController()
#service = UserService()
#repository = UserRepository()
@app.route('/users', methods=['GET'])
def get():
  return controller.get()

if __name__ == "__main__":
  app.run(host='127.0.0.1', port=5000, debug=True)