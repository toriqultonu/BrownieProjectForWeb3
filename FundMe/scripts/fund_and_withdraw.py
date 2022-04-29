from brownie import FundMe
from scripts.helpful_scripts import getAccount


def fund():
    fund_me = FundMe[-1]
    account = getAccount()
    print(fund_me)
    entrance_fee = fund_me.getEntranceFee()
    # entrance_fee = 25000000000000000
    print(entrance_fee)
    print(f"The current entry {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = getAccount()
    fund_me.withdraw({"from": account})


def main():
    fund()


# withdraw()
