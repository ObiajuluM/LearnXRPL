from xrpl.clients import JsonRpcClient


client = JsonRpcClient("https://s.altnet.rippletest.net:51234/")

from xrpl.wallet import Wallet

f = Wallet.create()

print(f.address)
print(f.seed)
