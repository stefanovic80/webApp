from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "here we go!"

@app.route("/anotherPage/")
def anotherPage():
    return "here another page!"

if __name__ == "__main__":
    app.run(port = 5000)
