from xrpl.wallet import *

from xrpl.wallet import generate_faucet_wallet


from xrpl.core import keypairs


# 1 - get seed
print(keypairs.generate_seed())

# 2 -  generate pubic key and private key
print(keypairs.derive_keypair(keypairs.generate_seed()))

# 3 -  get address from public key
print(keypairs.derive_classic_address())


##2
print(Wallet.create())


# 3
# requires to connect to a node to both create and fund wallet
print(generate_faucet_wallet())
