from web3 import Web3
from web3.middleware import geth_poa_middleware
from contract_info import abi, contract_address

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

contract = w3.eth.contract(address=contract_address, abi=abi)

print(contract.address)
print(f"Баланс вашего смарт-контракта: {w3.eth.get_balance(contract_address)}")
print(f"Баланс первого аккаунта:{w3.eth.get_balance('0x27E8cEeCc41fC6532B265c0e8f69Ec3b4755e5a6')}")
print(f"Баланс второго аккаунта:{w3.eth.get_balance('0x44e1d455baF1f45726d8232f9019351620eE8478')}")
print(f"Баланс третьего аккаунта:{w3.eth.get_balance('0xdF785D685745EdF4d960E7C30b5cbBe8d5B88693')}")
print(f"Баланс четвёртого аккаунта:{w3.eth.get_balance('0x963a320162c4E9B039f681ab9fFfd7C12F7f5365')}")
print(f"Баланс пятого аккаунта:{w3.eth.get_balance('0x108A30BAdbE93556830eB46002Ef609De5F96304')}")