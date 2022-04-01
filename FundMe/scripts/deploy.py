from os import access
from brownie import FundMe, accounts
from scripts.helpful_scripts import getAccount


def deploy_fund_me():

    account = getAccount()
    fund_me = FundMe.deploy({"from": account})
    print(f"Contract deployed to {fund_me.address}")


def main():
    deploy_fund_me()
