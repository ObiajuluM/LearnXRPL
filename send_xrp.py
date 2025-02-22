from xrpl.clients import JsonRpcClient
from xrpl.wallet import Wallet
from xrpl.models import Payment
from xrpl.utils import xrp_to_drops
from xrpl.transaction import sign, sign_and_submit, submit


# define client
client = JsonRpcClient("https://s.altnet.rippletest.net:51234")

# define sender wallet
sender_wallet = Wallet.from_seed("sEdVkZKqtmVRbVk6683tTPzFMRnobHV")

# unkwown wallet
receiver = "rUTXBjzxGQmPJFPF3cPGACrrkHc2ZBfnq7"


# define payment transaction
# 1 xrp = 100,000 drops
pay_txn = Payment(
    # sender
    account=sender_wallet.address,
    # amount to send
    amount=xrp_to_drops(10),
    # reciever
    destination=receiver,
)
# print(f" unsigned: {pay_txn}")

print("")
print("")
print("")


# sign and submit
print(sign_and_submit(transaction=pay_txn, client=client, wallet=sender_wallet).result)
