# mpt issuer authorize
from xrpl.models import (
    MPTokenAuthorize,
    MPTokenAuthorizeFlag,
)
from xrpl.wallet import Wallet
from xrpl.clients import JsonRpcClient

from xrpl.transaction import submit_and_wait


# build client
client = JsonRpcClient("https://s.devnet.rippletest.net:51234/")

# restore issuer account
issuer_account = Wallet.from_seed("sEd7z3wRNHcaJcRAdsvPhrawovTHzce")

mpt_issuer_auth = MPTokenAuthorize(
    account=issuer_account.address,
    mptoken_issuance_id="00081245E73344F4D5C041B27E978976F647C83A3D4E55F1",
    holder="raKGaKtxzdj5q52CCxD99TCfEukNXakPDS",
)

# submit and wait
response = submit_and_wait(
    transaction=mpt_issuer_auth,
    client=client,
    wallet=issuer_account,
)

# print(response)
print(response.result)
