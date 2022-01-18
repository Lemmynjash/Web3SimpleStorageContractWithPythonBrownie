from brownie import accounts, Storage,network


def deploy_simple_storage():
    #account = accounts[0]
    account=getaccounts()
    simple_storage=Storage.deploy({"from": account})
    store_value=simple_storage.retrieve()
    print(store_value)
    transaction_store_value=simple_storage.store(15,{"from": account})
    transaction_store_value.wait(1)
    updated_store_value=simple_storage.retrieve()
    print(updated_store_value)

def getaccounts():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.load("lemmy-account")
    
    
def main():
    deploy_simple_storage()
