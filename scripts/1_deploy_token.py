from brownie import OurToken
from scripts.helpful_scripts import get_account
from web3 import Web3

#########Morceau de code pour le probleme de la boucle lors du deploiement des contrats
from brownie.network import gas_price
from brownie.network.gas.strategies import LinearScalingStrategy

gas_strategy = LinearScalingStrategy("60 gwei", "70 gwei", 1.1)

gas_price(gas_strategy)

# On va mettre l'offre initial qui sera a 1000 ether
initial_supply = Web3.toWei(1000, "ether")


def main():
    account = get_account()
    our_token = OurToken.deploy(
        initial_supply, {"from": account, "gas_price": gas_strategy}
    )
    print(our_token.name())
