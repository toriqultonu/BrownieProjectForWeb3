from brownie import accounts, config, FundMe, network


def getAccount():

    if network.show_active() == "development":
        return accounts[0]

    else:
        return accounts.add(config["wallets"]["from_key"])
