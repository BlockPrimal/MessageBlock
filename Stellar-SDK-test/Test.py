import requests


# todo create test account on horizon_testnet
# todo test memo_text

secret_phrase = 'acoustic super rice plug match source turtle fiscal valve nothing armed leave'
publickey = 'GBMXAPHVCX4JK5MRGWQO67RNHP2ZUEUTXBOYBTBXVEXE74DUCR3DRFXJ'
seed = 'SC4A7PB4LWNKOTMYB2VEZDH2TDB753IWIUHFINYAKNSV3YIEM5KB2OES'

from stellar_base.keypair import Keypair
kp = Keypair.random()

from stellar_base.utils import StellarMnemonic
# Here we use Chinese, but English is the default language.

url = 'https://friendbot.stellar.org'
r = requests.get(url, params={'addr': publickey})

print(r)
print(secret_phrase)

print(publickey)
print(seed)

from stellar_base.keypair import Keypair
from stellar_base.operation import CreateAccount, Payment
from stellar_base.transaction import Transaction
from stellar_base.transaction_envelope import TransactionEnvelope as Te
from stellar_base.memo import TextMemo
from stellar_base.horizon import horizon_testnet

# This creates a new Horizon Livenet instance
horizon = horizon_testnet()

# This is the seed (the StrKey representation of the secret seed that
# generates your private key from your original account that is funding the
# new account in the create account operation. You'll need the seed in order
# to sign off on the transaction. This is the source account.
old_account_seed = "SCVLSUGYEAUC4MVWJORB63JBMY2CEX6ATTJ5MXTENGD3IELUQF4F6HUB"
old_account_keypair = Keypair.from_seed(old_account_seed)

# This is the new account ID (the StrKey representation of your newly
# created public key). This is the destination account.
new_account_addr = "GBMXAPHVCX4JK5MRGWQO67RNHP2ZUEUTXBOYBTBXVEXE74DUCR3DRFXJ"

amount = '1' # Your new account minimum balance (in XLM) to transfer over
# create the CreateAccount operation
op = CreateAccount(
    destination=new_account_addr,
    starting_balance=amount
)
# create a memo
memo = TextMemo('Hello, StellarCN!')

# Get the current sequence of the source account by contacting Horizon. You
# should also check the response for errors!
# Python 3
sequence = horizon.account(old_account_keypair.address().decode()).get('sequence')
# Python 2
# sequence = horizon.account(old_account_keypair.address()).get('sequence')

# Create a transaction with our single create account operation, with the
# default fee of 100 stroops as of this writing (0.00001 XLM)
tx = Transaction(
    source=old_account_keypair.address().decode(),
    sequence=sequence,
    memo=memo,
    operations=[
        op,
    ],
)
# Build a transaction envelope, ready to be signed.
envelope = Te(tx=tx, network_id="PUBLIC")

# Sign the transaction envelope with the source keypair
envelope.sign(old_account_keypair)

# Submit the transaction to Horizon
te_xdr = envelope.xdr()
response = horizon.submit(te_xdr)

