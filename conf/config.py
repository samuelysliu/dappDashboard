import os
from dotenv import load_dotenv

load_dotenv()


class systemConfig:
    def __init__(self):
        if os.getenv("environment") == "test":
            self.dbName = "tt_prize_test"
        elif os.getenv("environment") == "main":
            self.dbName = "tt_prize"
        else:
            self.dbName = "tt_prize_test"

    def getDBName(self):
        return self.dbName


class gameInfo:
    def __init__(self):
        return None

    def getAdminWalletList(self):
        return ["0xe2421C37fC3a26e84B39F32776b2302bC38e449D", "0xeD730ECbdD28f26A7aDE5d4398CDf6AAc1544010",
                "0x9d9dcBaca3CF3Fd2E01F4A31b510F7f9656eE8E0", "0x0EDb293B029e0cFa2C598D49BC878E3fB34DcFF5",
                "0xaA21c4688Eb22E6aFE7E6EF8Dab610a91049296b", "0x46D82332f5F8358d889e3E84F0baEE27524a8A0e"]
