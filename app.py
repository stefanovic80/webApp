import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    #return "it's working, cazzarola!"
    return render_template('black_body.html')

@app.route("/clausius_mossotti_model/")
def home2():
    return render_template('clausius_mossotti_model.html')

if __name__ == "__main__":
    #app.run(port = 5000)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
