from api.domain.service.userService import UserService

class UserController:

    service = UserService()
    def get(self):
        return self.service.get()