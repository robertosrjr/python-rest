import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import jsonify 
from api.domain.model.userCollection import User

class FireBase():

    def __init__(self):
       self.db = None
       self.bootServer()

    def bootServer(self):

        print("bootServer...")
        try:
            cred = credentials.Certificate('user_service/static/google/firestore/data-base-teste-277100-8a0d28ccf452.json')
            firebase_admin.initialize_app(cred)
            self.db = firestore.client()
            self.add()
        except ValueError:
            print("Oops! Erro ao recuperar as credenciais")
    
    def get(self):
        users_ref = self.db.collection(u'users')
        all_users = [doc.to_dict() for doc in users_ref.stream()]
        return jsonify(all_users)

    def add(self):
        doc_ref = self.db.collection(u'users').document(u'alovelace')
        doc_ref.set({
            u'first': u'Ada',
            u'last': u'Lovelace',
            u'born': 1815
        })