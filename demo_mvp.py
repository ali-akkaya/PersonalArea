from instagrapi import Client
from concurrent.futures import ThreadPoolExecutor
import threading

#userList = ['artsneedyou','erenblogger', '4play_people', 'pinar.manavi', 'agucompsociety', 'micayazilim', 'dincerisgel',]


def follow(cl, user_follow):

    userId = cl.user_id_from_username(user_follow)
    cl.user_follow(userId)
    print(user_follow + "Followed.")


# with ThreadPoolExecutor(max_workers=10) as executor:
#     for name in userList:
#         future = executor.submit(follow, ["indicator_css", "pomzeR-zyzto7-zibxux", name])
#         print (name+" followed.")



from flask import Flask, jsonify, request, json, abort


app = Flask(__name__)

api_response = []

# Route of the web application.
@app.route('/')
def index():
    return "Welcome to the Flask API"

@app.route('/api', methods=['POST'])
def api_function():

    if not request.json or not 'user_list' in request.json :
        print(request.json)
        abort(400)
    userList = request.json['user_list']
    print(userList)
    threads = []
    import time
    start_time = time.time()
    cl = Client()
    cl.login("indicator_css", "pomzeR-zyzto7-zibxux")
    print("Logged In")
    for i in range(len(userList)):
        browserThread = threading.Thread(target=follow, args=[cl, userList[i]])
        browserThread.start()
        threads.append(browserThread)

    for thread in threads:
        thread.join()
    print("--- %s seconds ---" % (time.time() - start_time))

    return jsonify({"Result": "Accounts are followed"}), 201
# Web application will be launched in local.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)