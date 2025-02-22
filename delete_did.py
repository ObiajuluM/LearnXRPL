from xrpl.models import DIDDelete
from xrpl.clients import JsonRpcClient
from xrpl.wallet import Wallet
from xrpl.transaction import submit_and_wait


# build client
client = JsonRpcClient("https://s.altnet.rippletest.net:51234/")

# restore account
account = Wallet.from_seed("sEd7ByDcyHuoKD23tcpKM9fbULC4nNT")

# build transaction
did_set = DIDDelete(account=account.address)

response = submit_and_wait(
    client=client,
    transaction=did_set,
    wallet=account,
)

# print result
print(response.result)

# TEC_NOENTRY