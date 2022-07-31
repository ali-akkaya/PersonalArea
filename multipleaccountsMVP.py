import threading
accounts = [("indicator_css", "pomzeR-zyzto7-zibxux"), ("indicator_css_3", "Mrtmxr3321"),
            ("indicator_css_4", "Mrtmxr3321"), ("indicator_css_5", "Mrtmxr3321"),
            ("indicator_css_6", "Mrtmxr3321"), ("indicator_css_7", "Mrtmxr3321")]

threads =[]
def follow(user_name,user_password, user_follow):
    cl = Client()
    cl.login(user_name, user_password)
    print(user_name + "Signed In.")
    userId = cl.user_id_from_username(user_follow)
    cl.user_follow(userId)
    print(user_follow + "Followed.")

def follow_with_bot(user_name, user_password, user_follow):
    bot = Bot()
    bot.login(username=user_name, password=user_password)
    bot.follow(user_follow)
    print(user_follow + "Followed.")


for i in range(len(accounts)):
    browserThread = threading.Thread(target=follow_with_bot, args=[accounts[0][0], accounts[0][1],"artsneedyou"])
    browserThread.start()
    threads.append(browserThread)

for thread in threads:
    thread.join()