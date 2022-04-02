from os import access
from brownie import FundMe, MockV3Aggregator, accounts, network, config
from scripts.helpful_scripts import getAccount


def deploy_fund_me():

    account = getAccount()
    # pass the price feed address to our fundme contract
    if network.show_active() != "development":
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]

    else:
        print(f"The active network is {network.show_active()}")
        print(f"Deploying Mocks...")
        mock_aggregator = MockV3Aggregator.deploy(
            18, 2000000000000000000000, {"from": account}
        )
        price_feed_address = mock_aggregator.address
        print("Mocks deployed!")

    fund_me = FundMe.deploy({"from": account}, publish_source=True)
    print(f"Contract deployed to {fund_me.address}")


def main():
    deploy_fund_me()
