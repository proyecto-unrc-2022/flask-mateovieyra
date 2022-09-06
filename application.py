from flask import Flask, jsonify, request, Response, make_response
import json

app = Flask(__name__)

USERS = {}

@app.route('/')
def index():
    return 'Index Page'

@app.route("/users/<username>", methods=['GET', 'PUT', 'DELETE'])
def access_users(username):
    if request.method == 'GET':
        user_details = USERS.get(username)
        if user_details:
            return jsonify(user_details)
        else:
            return Response(status=404)
    elif request.method == 'PUT':
        USERS.update({username: {'name': request.json}})
        return Response(status=201)
    elif request.method == 'DELETE':
        USERS.pop(username)
        return Response(status=200)

@app.route("/users", methods=['POST', 'GET'])
def add_user():
    if request.method == 'POST':
        USERS.update(request.json)
        new_user_name = list(request.json.keys())[0]
        return Response(json.dumps({"status":"true"}), 201, {"location": f'users/{new_user_name}'})
    elif request.method == 'GET':
        if USERS:
            return make_response(jsonify(USERS))
        else:
            return Response(status=404)

if __name__ == "__main__":
    app.run(debug=True)
