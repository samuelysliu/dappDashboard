from models import db
from datetime import datetime

class model:
    def __init__(self):
        self.collection = db.table().revenueTable()


    def getByDuring(self, *args):
        try:
            order = []
            for i in self.collection.find(
                    {"createdAt": {"$gte": datetime(args[0]["gtYear"], args[0]["gtMonth"], args[0]["gtDay"]),
                                   "$lte": datetime(args[0]["ltYear"], args[0]["ltMonth"], args[0]["ltDay"])}}):
                order.append(i)
            return order
        except:
            return "failed"

    def getByType(self, *args):
        try:
            order = []
            for i in self.collection.find({"type": args[0]["type"]}):
                order.append(i)
            return order
        except:
            return "failed"

    def getAll(self):
        try:
            order = []
            for i in self.collection.find():
                order.append(i)
            return order
        except:
            return "failed"