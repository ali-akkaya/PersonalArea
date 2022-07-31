from multiprocessing import Pool
from functools import partial
import pandas as pd



def mass_follow(account,user_name):
    print(account[1]["username"],account[1]["password"],account[1]["proxy"],sep="\t")
    print(user_name)

if __name__ == '__main__':
    accounts = pd.read_csv("InstagramBot/accounts_info.csv")
    proxy = pd.read_csv("InstagramBot/proxy.csv")
    # Add a random proxy to accounts
    accounts["proxy"] = proxy.sample(n=len(accounts),replace=True,ignore_index=True)["proxy"]

    pool =Pool()
    pool.map(partial(mass_follow,user_name="deneme"),accounts.iterrows())
    pool.close()
    pool.join()



