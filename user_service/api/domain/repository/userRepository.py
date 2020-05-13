from api.domain.google.firebase import FireBase 

class UserRepository:

    firebase = FireBase()

    USER = {
    '1': {'name': 'Mark', 'age': 23, 'spec': 'math'},
    '2': {'name': 'Jane', 'age': 20, 'spec': 'biology'},
    '3': {'name': 'Peter', 'age': 21, 'spec': 'history'},
    '4': {'name': 'Kate', 'age': 22, 'spec': 'science'},
    }

    def get(self):
       return self.firebase.get()

    def add(self, USER):
        self.firebase.add()
