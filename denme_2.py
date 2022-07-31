
import threading
from instagrapi import Client

threads = []
userList =['artsneedyou','gdgkayseri', 'faoluramadogibiolmaz', 'sustainablefertilizer', 'agucompsociety',]


cl = Client()
cl.login("css_indicator", "pyjfyq-neczur-dewhU8")
def follow_user(client, user_name):

    userId = client.user_id_from_username(user_name)
    client.user_follow(user_id=userId)


for i in range(5):
    browserThread = threading.Thread(target=follow_user, args=[cl,userList[i]])
    browserThread.start()
    threads.append(browserThread)

for thread in threads:
    thread.join()