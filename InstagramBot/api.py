import os
from multiprocessing import Pool
from functools import partial
import pandas as pd
from flask import Flask, jsonify, request, json, abort
import bot


app = Flask(__name__)

api_response = []


def mass_follow(account,user_name):
    # instagram_bot = bot.Bot(account.loc[0],account.loc[1],account.loc[2])
    # instagram_bot.follow_user(user_name)
    print(account[1]["username"], account[1]["password"], account[1]["proxy"], sep="\t")
    print(user_name)





# Route of the web application.
@app.route('/')
def index():
    print(__name__)
    return "Welcome to the Flask API"


@app.route('/api', methods=['POST'])
def follow_thread():
    if not request.json or not 'user_name' in request.json :
        print(request.json)
        abort(400)


    user_name_to_follow = request.json['user_name']
    print(user_name_to_follow)
    accounts_filepath = os.path.join(app.root_path, "accounts_info.csv")
    print(accounts_filepath)
    accounts = pd.read_csv(accounts_filepath)
    proxy_filepath = os.path.join(app.root_path, "proxy.csv")
    print(proxy_filepath)
    proxy = pd.read_csv(proxy_filepath)
    # Add a random proxy to accounts
    accounts["proxy"] = proxy.sample(n=len(accounts), replace=True, ignore_index=True)["proxy"]
    print(accounts)
    if __name__ == '__main__':
        pool = Pool()
        pool.map(partial(mass_follow,user_name=user_name_to_follow),accounts.iterrows())
        pool.close()
        pool.join()
    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)