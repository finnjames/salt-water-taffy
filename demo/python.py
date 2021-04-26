from flask import Flask, jsonify, make_response, request
import time


class Abstract:

    hello = "world"

    def __init__(self, a):
        self.a = a


app = Flask('python-flask-seed')
# hello world

a = Abstract()

a.hello = "lo"

print(time.time())


@app.route('/welcome', methods=['POST'])
def welcome(self, a):
    content = request.get_json(silent=True, force=True)

    try:
        message = 'Welcome %s!' % content['name']
        response = {'message': message}
        return make_response(jsonify(response), 200)

    except Exception as ex:
        response = {'error': 'name is required'}
        return make_response(jsonify(response), 400)
