from flask import Flask

app = Flask(__name__)

@app.get("/")

def index():
    me = {
        "first_name": "Alejandro",
        "first_name": "Barragan",
        "hobbies": "Watch movies and series",
        "is_online": True
    }
    return me