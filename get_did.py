# get did information

from xrpl.clients import JsonRpcClient
from xrpl.models import LedgerEntry
from xrpl.wallet import Wallet
from xrpl.utils import hex_to_str


# build client
client = JsonRpcClient("https://s.altnet.rippletest.net:51234/")

# restore account
account = Wallet.from_seed("sEd7ByDcyHuoKD23tcpKM9fbULC4nNT")

# build request
request = LedgerEntry(did=account.address, ledger_index="validated")

# submit request and return response
response = client.request(request=request).result

# parse DID Object
print(f'did document: {hex_to_str(response["node"]["DIDDocument"])}')
print(f'did data: {hex_to_str(response["node"]["Data"])}')
print(f'did uri: {hex_to_str(response["node"]["URI"])}')

# tec no entry