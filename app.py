from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "The suffering is over, Bang!"

if __name__ == "__main__":
    app.run()
