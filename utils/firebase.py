import pyrebase

class Firebase:
    def __init__(self):
        # Configuration key.
        self._firebaseConfig = {
            'apiKey': "AIzaSyCfPF9b2EwwQiQz9XFjtgZMYVusCcNZtvU",
            'authDomain': "singapur-381c8.firebaseapp.com",
            'databaseURL': "https://singapur-381c8-default-rtdb.firebaseio.com",
            'projectId': "singapur-381c8",
            'storageBucket': "singapur-381c8.appspot.com",
            'messagingSenderId': "629536295319",
            'appId': "1:629536295319:web:58d41443e24b69f36a5cd2",
            'measurementId': "G-8GLPJL6BFP"
        }
        # Firebase.
        self._firebase = pyrebase.initialize_app(self._firebaseConfig)
    
    
    def getFirebase(self):
        return self._firebase
    
    def getdb(self):
        # Firebase Database.
        return self._firebase.database()
    
    def getauth(self):
        # Firebase Authentication.
        return self._firebase.auth()
    
    def getstorage(self):
        # Firebase Storage.
        return self._firebase.storage()