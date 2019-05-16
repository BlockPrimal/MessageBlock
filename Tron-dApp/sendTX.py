from tronapi import Tron
from tronapi import HttpProvider
import logging

# docker run -it  -p 9090:9090  --rm  --name tron  trontools/quickstart

full_node = HttpProvider('http://127.0.0.1:9090')
solidity_node = HttpProvider('http://127.0.0.1:9090')
event_server = HttpProvider('http://127.0.0.1:9090')


import logging
from tronapi import Tron

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()


private_key = '13c645c0d0fc8c0b4a5869123eed19563c58cff48137cff4792c94a7a314e073'

tron = Tron(full_node=full_node,
            solidity_node=solidity_node,
            event_server=event_server)



tron.private_key = '13c645c0d0fc8c0b4a5869123eed19563c58cff48137cff4792c94a7a314e073'
tron.default_address = 'THUKckk7VoEnRkNDHSkWudWSQGxXBYMmHT'

# added message
send = tron.trx.send_transaction('TCqLG9TvQq4YC7Gjt1QrtcR3iNVNKM32qX', 100.0)
print(send)