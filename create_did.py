# updating a decentralized identifier

from xrpl.models import DIDSet
from xrpl.clients import JsonRpcClient
from xrpl.wallet import Wallet
from xrpl.utils import str_to_hex
from xrpl.transaction import submit_and_wait


# build client
client = JsonRpcClient("https://s.altnet.rippletest.net:51234/")

# restore account
account = Wallet.from_seed("sEd7ByDcyHuoKD23tcpKM9fbULC4nNT")



# build transaction
did_set = DIDSet(
    account=account.address,
    did_document=str_to_hex("updated account did document"),
    data=str_to_hex("updated account did data"),
    uri=str_to_hex("did.data.com"),
)

# submit and wait for response
response = submit_and_wait(
    client=client,
    transaction=did_set,
    wallet=account,
)

print(response.result)
