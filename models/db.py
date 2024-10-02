import os
from pymongo import MongoClient
from conf import config
from dotenv import load_dotenv
load_dotenv()


configObject = config.systemConfig()


class table:
    def __init__(self):
        client = MongoClient(os.getenv("MONGO_URI"))
        self.db = client[configObject.getDBName()]

    def coinTable(self):
        return self.db["coin"]

    def diceTable(self):
        return self.db["diceRollerOrder"]

    def dividendTable(self):
        return self.db["dividendOrder"]

    def goldDividendTable(self):
        return self.db["goldDividendOrder"]

    def lotteryTable(self):
        return self.db["lottery"]

    def revenueTable(self):
        return self.db["revenue"]

    def userTable(self):
        return self.db["user"]

    def treasureTable(self):
        return self.db["treasure"]

    def robTransactionTable(self):
        return self.db["robTransaction"]
