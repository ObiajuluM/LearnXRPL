from xrpl.clients import JsonRpcClient
from xrpl.models import AccountInfo

# create a client
client = JsonRpcClient("https://s.altnet.rippletest.net:51234/")

# build request
account_info = AccountInfo(
    account="rUTXBjzxGQmPJFPF3cPGACrrkHc2ZBfnq7",
    ledger_index="validated",
)

# make request
r_account_info = client.request(account_info)


# print result
print(r_account_info.result)