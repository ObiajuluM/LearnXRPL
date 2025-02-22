from xrpl.clients import JsonRpcClient
from xrpl.models import AccountSet, AccountSetAsfFlag
from xrpl.wallet import Wallet
from xrpl.transaction import submit_and_wait

# create client
client = JsonRpcClient("https://s.altnet.rippletest.net:51234/")

# restore account
account = Wallet.from_seed("sEd7ByDcyHuoKD23tcpKM9fbULC4nNT")

# build account set transaction
accountset_txn = AccountSet(
    account=account.address,
    clear_flag=AccountSetAsfFlag.ASF_DISABLE_INCOMING_CHECK,
)


for i in range(100):
    # sign, submit and wait for a response
    result = submit_and_wait(
        client=client,
        transaction=accountset_txn,
        wallet=account,
    )
    print("done")

    # print result
    print(result.result)
