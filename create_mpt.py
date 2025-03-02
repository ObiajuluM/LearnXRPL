# create multipurpose token
from xrpl.models import (
    MPTokenIssuanceCreate,
    MPTokenIssuanceCreateFlag,
    MPTokenAuthorize,
    MPTokenAuthorizeFlag,
)
from xrpl.wallet import Wallet
from xrpl.clients import JsonRpcClient
from xrpl.utils import str_to_hex
from xrpl.transaction import submit_and_wait


# create client
client = JsonRpcClient("https://s.devnet.rippletest.net:51234/")

# restore account
account = Wallet.from_seed("sEd7z3wRNHcaJcRAdsvPhrawovTHzce")


# build transaction
mpt_create = MPTokenIssuanceCreate(
    account=account.address,
    mptoken_metadata=str_to_hex("{'token': 'land'}"),  # 1024 hex bytes
    maximum_amount="10000",
    asset_scale=0,
    flags=[
        MPTokenIssuanceCreateFlag.TF_MPT_CAN_CLAWBACK,
        MPTokenIssuanceCreateFlag.TF_MPT_CAN_ESCROW,
        MPTokenIssuanceCreateFlag.TF_MPT_CAN_LOCK,
        MPTokenIssuanceCreateFlag.TF_MPT_CAN_TRADE,
        MPTokenIssuanceCreateFlag.TF_MPT_CAN_TRANSFER,
        MPTokenIssuanceCreateFlag.TF_MPT_REQUIRE_AUTH,
    ],
    transfer_fee=10000,
)


# submit and wait
result = submit_and_wait(
    transaction=mpt_create,
    client=client,
    wallet=account,
)

# print(response)
print(result.result)



