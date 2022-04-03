import imp
from brownie import accounts, config, FundMe, network, MockV3Aggregator
from web3 import Web3


def getAccount():

    if network.show_active() == "development":
        return accounts[0]

    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print(f"Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(18, Web3.toWei(2000, "ether"), {"from": getAccount()})
    print("Mocks deployed!")
