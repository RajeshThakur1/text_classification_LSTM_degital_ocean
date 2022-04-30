from flask import Flask
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    return "Hello world"

if __name__=="__main__":
    app.run(port=8080)