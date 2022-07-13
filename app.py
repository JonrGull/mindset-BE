from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hi there!'

@app.route("/login") 
def login():
    return "this is login"

if __name__ == '__main__':
    app.run('0.0.0.0', 8080, debug=True)