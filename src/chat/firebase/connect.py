from firebase_admin import credentials, initialize_app, db


def connect():
    cred = credentials.Certificate("fire.json")
    initialize_app(cred, {
        "databaseURL": "https://test-project-45a34-default-rtdb.firebaseio.com/"  # Your database URL
    })
    dbconn = db.reference("Users")
    return dbconn
