import pandas as pd


accounts = pd.read_csv("InstagramBot/accounts_info.csv")
print(accounts)
for ind in accounts.index:
    print(accounts.loc[ind, "username"], accounts.loc[ind, "password"])



proxy = pd.read_csv("InstagramBot/proxy.csv")
# Add a random proxy to accounts
accounts["proxy"] = proxy.sample(n=len(accounts),replace=True,ignore_index=True)["proxy"]

print(accounts)

def print_account(account):
    print(account.loc[0],account.loc[1],account.loc[2],sep="\t")



for row in accounts.iterrows():
    print(row[1]["username"],row[1]["password"],row[1]["proxy"], sep="\t")