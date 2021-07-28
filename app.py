import os
from flask import Flask, request
from flask_cors import CORS
import os

app = Flask('MeuIP')

cors = CORS(app, resource={r'/*':{'origins': '*'}})

@app.route('/', methods=['GET'])
def index():
    return '<h1>Hello WOrld!</h1>'

@app.route('/user', methods=['GET'])
def createUser():

    #body = request.get_json()

    return {'aa': 'safasf'}


def main():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    main()