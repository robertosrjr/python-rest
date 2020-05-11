from api.domain.repository.userRepository import UserRepository

class UserService:

    repository = UserRepository()
    def get(self):
        return self.repository.get()