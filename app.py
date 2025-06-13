from flask import Flask

app = Flask(__name__)

@app.route("/")
def function():
    return "here we go!"

if __name__ == "__main__":
    app.run(port = 5000)
