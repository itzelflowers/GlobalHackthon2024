import pyrebase

class Firebase:
    def __init__(self):
        # Configuration key.
        self._firebaseConfig = {
            'apiKey': "AIzaSyCGw0yokHwaEgWWNc1OGDo-8Iwk8_p5R6Q",
            'authDomain': "hackmexico2-784a3.firebaseapp.com",
            'databaseURL': "https://hackmexico2-784a3-default-rtdb.firebaseio.com",
            'projectId': "hackmexico2-784a3",
            'storageBucket': "hackmexico2-784a3.appspot.com",
            'messagingSenderId': "499824700976",
            'appId': "1:499824700976:web:75ce309870353aa99c07f5",
            'measurementId': "G-E3R7BYY22N"
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