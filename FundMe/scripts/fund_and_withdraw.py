from brownie import FundMe
from scripts.helpful_scripts import getAccount


def fund():
    fund_me = FundMe[-1]
    account = getAccount()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)


def main():
    fund()
