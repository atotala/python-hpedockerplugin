from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def hello():
    data = request.data
    return  

if __name__ == '__main__':
app.run(host='0.0.0.0')
