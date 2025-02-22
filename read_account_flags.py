from xrpl.clients import JsonRpcClient
from xrpl.models import AccountInfo


# build the client
client = JsonRpcClient("https://s.altnet.rippletest.net:51234/")


# build request
account_info_flags = AccountInfo(
    account="rUTXBjzxGQmPJFPF3cPGACrrkHc2ZBfnq7",
    ledger_index="validated",
)


# make request
r_account_info_flags = client.request(account_info_flags)


flags = r_account_info_flags.result["account_data"]["Flags"]


# account root flags list
ACCOUNT_ROOT_FLAGS = [
    {
        "flagname": "Free Regular Key Transaction",
        "hex": 0x00010000,
        "decimal": 65536,
        "asf": "",
        "description": "This account has used its free SetRegularKey transaction.",
    },
    #
    {
        "flagname": "Default Ripple",
        "hex": 0x00800000,
        "decimal": 8388608,
        "asf": "asfDefaultRipple",
        "description": "Enable rippling on this account's trust lines by default. Required for issuing addresses; discouraged for others.",
    },
    {
        "flagname": "Deposit Authorization",
        "hex": 0x01000000,
        "decimal": 16777216,
        "asf": "asfDepositAuth",
        "description": "This account can only receive funds from transactions it initiates, and from [preauthorized accounts](link to deposit preauth).",
    },
    {
        "flagname": "Disable Master Key",
        "hex": 0x00100000,
        "decimal": 1048576,
        "asf": "asfDisableMaster",
        "description": "Disallow the use of the master key to sign transactions for this account. Can only be enabled if the account has configured another way to sign transactions, such as a Regular Key or a Signer List.",
    },
    {
        "flagname": "Block Incoming Checks",
        "hex": 0x08000000,
        "decimal": 134217728,
        "asf": "asfDisallowIncomingCheck",
        "description": "No account should create checks directed to this account.",
    },
    {
        "flagname": "Block Incoming NFTokenOffers",
        "hex": 0x04000000,
        "decimal": 134217728,
        "asf": "asfDisallowIncomingNFTokenOffer",
        "description": "No account should create nft offers directed to this account.",
    },
    {
        "flagname": "Block Incoming Payment Channnels",
        "hex": 0x10000000,
        "decimal": 268435456,
        "asf": "asfDisallowIncomingPayChan",
        "description": "No account should create payment channels directed to this account.",
    },
    {
        "flagname": "Block Incoming Trustlines",
        "hex": 0x20000000,
        "decimal": 536870912,
        "asf": "asfDisallowIncomingTrustline",
        "description": "No account should create trustlines directed to this account.",
    },
    {
        "flagname": "Block XRP",
        "hex": 0x00080000,
        "decimal": 524288,
        "asf": "asfDisallowXRP",
        "description": "No account should send XRP to this account. Not enforced by the blockchain.",
    },
    {
        "flagname": "Global Freeze",
        "hex": 0x00400000,
        "decimal": 4194304,
        "asf": "asfGlobalFreeze",
        "description": "Freeze all assets issued by this account",
    },
    {
        "flagname": "No Freeze",
        "hex": 0x00200000,
        "decimal": 2097152,
        "asf": "asfNoFreeze",
        # "description": "This address cannot freeze trust lines connected to it. Once enabled, cannot be disabled.",
        "description": "Permanently give up the ability to freeze individual trust lines or modify Global Freeze. This flag can never be disabled after being enabled.",
    },
    {
        "flagname": "Require Authorization",
        "hex": 0x00040000,
        "decimal": 262144,
        "asf": "asfRequireAuth",
        "description": "This account must individually approve any account that wants to hold tokens it issues. Can only be enabled if this account has no trust lines connected to it.",
        # "description": "Require authorization for users to hold balances issued by this address. Can only be enabled if the address has no trust lines connected to it."
    },
    {
        "flagname": "Require Destination Tag",
        "hex": 0x00020000,
        "decimal": 131072,
        "asf": "asfRequireDest",
        "description": "Requires incoming payments to this account to specify a Destination Tag.",
    },
    {
        "flagname": "Trustline Clawback",
        "hex": 0x80000000,
        "decimal": 2147483648,
        "asf": "asfAllowTrustLineClawback",
        "description": "This account can claw back tokens it has issued. Can only be set if the account has an empty owner directory (no trust lines, offers, escrows, payment channels, checks, or signer lists, etc). Once enabled it cannot be disabled.",
    },
]


# bitwise AND
for flag in ACCOUNT_ROOT_FLAGS:
    if flag["hex"] & flags == flag["hex"]:
        print(flag)
    else:
        print("no flags found")
        break
