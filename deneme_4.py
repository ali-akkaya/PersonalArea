from instagrapi import Client
from concurrent.futures import ThreadPoolExecutor
from flask import Flask, jsonify, request, json, abort


app = Flask(__name__)

api_response = []

# Route of the web application.
@app.route('/')
def index():
    return "Welcome to the Flask API"

@app.route('/api', methods=['POST'])
def function():
    if not request.json or not 'user_list' in request.json :
        print(request.json)
        abort(400)
    userList = request.json['user_list']


    with ThreadPoolExecutor(max_workers=10) as executor:
        for name in userList:
            future = executor.submit(follow, ["indicator_css", "pomzeR-zyzto7-zibxux", name])

    return jsonify({"Result": "ACoounts are followed"}), 201


#userList =['artsneedyou','erenblogger', '4play_people', 'pinar.manavi', 'agucompsociety']

def follow(username, password, user_follow):
    cl = Client()
    cl.login(username,password)
    print("Logged In")
    userId = cl.user_id_from_username(user_follow)
    cl.user_follow(userId)


# Web application will be launched in local.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)






