from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Oh --- Hello World! --- 1234"

if __name__ == "__main__":
    application.run()
