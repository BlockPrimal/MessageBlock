from tronapi import Tron
from tronapi import HttpProvider
from solcx import compile_source
from solcx import set_solc_version
set_solc_version('v0.4.25')


# docker run -it  -p 9090:9090  --rm  --name tron  trontools/quickstart

full_node = HttpProvider('http://127.0.0.1:9090')
solidity_node = HttpProvider('http://127.0.0.1:9090')
event_server = HttpProvider('http://127.0.0.1:9090')


import logging


logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()



tron = Tron(full_node=full_node,
            solidity_node=solidity_node,
            event_server=event_server)
tron.private_key = '8bf08095f01afbaee2616da0bc7b2c182f41051af413bc0b7544241acc9d214d'
tron.default_address = 'TUV6hdSDBza3fPQRRfiKhWNGPTfebtyhei'





# Solidity source code
contract_source_code = '''
pragma solidity ^0.4.25;

contract Hello {
    string public message;

    function Hello(string initialMessage) public {
        message = "This is a test";
    }

    function setMessage(string newMessage) public {
        message = newMessage;
    }
}

'''

compiled_sol = compile_source(contract_source_code)
contract_interface = compiled_sol['<stdin>:Hello']

hello = tron.trx.contract(
    abi=contract_interface['abi'],
    bytecode=contract_interface['bin']
)

# Submit the transaction that deploys the contract
tx = hello.deploy(fee_limit=1000,
                  call_value=0,
                  consume_user_resource_percent=1)

# sign = tron.trx.sign(tx)
# result = tron.trx.broadcast(sign)