# Accounts on the XRPL
# from xrpl.account import *

# from xrpl.clients import *

# from xrpl.models import *

# from xrpl.transaction import *

# from xrpl.wallet import *

# from xrpl.asyncio import *

# from xrpl.core import *

# from xrpl.utils import *

# from xrpl.constants import *


from xrpl.wallet import Wallet, generate_faucet_wallet
from xrpl.clients import JsonRpcClient
from xrpl.models import AccountInfo
from xrpl.utils import drops_to_xrp, xrp_to_drops

client = JsonRpcClient("https://s.altnet.rippletest.net:51234")

# query information about the account from the ledger


f = generate_faucet_wallet(client=client)

print(f.address)
print(f.seed)


# balance = resp.result["account_data"]["Balance"]

# print(f"Balance: {drops_to_xrp(balance)} XRP")
