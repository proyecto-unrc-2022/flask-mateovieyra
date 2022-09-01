from flask import Flask, jsonify, request, Response, make_response

app = Flask(__name__)

USERS = {}

@app.route('/')
def index():
    return 'Index Page'

@app.route("/users/<username>", methods=['GET'])
def access_users(username):
    if request.method == 'GET':
        user_details = USERS.get(username)
        if user_details:
            return jsonify(user_details)
        else:
            return Response(status=404)

@app.route("/users", methods=['POST'])
def add_user():
    USERS.update(request.json)
    return make_response(
        jsonify({"status":"true"}),
        201
    )

if __name__ == "__main__":
    app.run()
