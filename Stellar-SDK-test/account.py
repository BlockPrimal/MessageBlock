# todo create ability to check transations (recieve memo_text)

from stellar_base.address import Address

import requests

from stellar_base.keypair import Keypair
kp = Keypair.random()

publickey = kp.address().decode()
url = 'https://friendbot.stellar.org'
r = requests.get(url, params={'addr': publickey})


address = Address(address=publickey) # See signature for additional args
print(address.get()) # Get the latest information from Horizon