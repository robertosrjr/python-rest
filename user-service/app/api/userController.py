
from userService import UserService

class UserController:

    def __init__(self, service=None):
        self.service = UserService()

    def get(self):
        return self.service.get()