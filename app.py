from flask import Flask

app = Flask("/",methods=["GET", "POST"])
def index():
    return "Hello world"

if __name__=="__mail__":
    app.run(port=8081)