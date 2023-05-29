from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "just an example to run python code on live"

if __name__ == '__main__':
    app.run()