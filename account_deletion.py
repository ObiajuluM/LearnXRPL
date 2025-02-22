from pydoc import cli
from xrpl.clients import JsonRpcClient
from xrpl.transaction import submit_and_wait
from xrpl.models import AccountDelete
from xrpl.wallet import Wallet, generate_faucet_wallet


# create client
client = JsonRpcClient("https://s.altnet.rippletest.net:51234/")

# restore account from seed
account = Wallet.from_seed("sEd7ByDcyHuoKD23tcpKM9fbULC4nNT")

# build account delete transaction
accountdel_txn = AccountDelete(
    account=account.address,
    destination="rPT1Sjq2YGrBMTttX4GZHjKu9dyfzbpAYe",
)


generate_faucet_wallet(client=client, wallet=account)

# sign, submit and wait for a response
# result = submit_and_wait(
#     client=client,
#     transaction=accountdel_txn,
#     wallet=account,
# )

# # print result
# print(result.result)
