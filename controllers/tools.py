import datetime
from models import coinModel, diceModel, dividendModel, goldDividend, lotteryModel, revenueModel, userModel, \
    robTransactionModel, treasureModel, redis
from conf import config

coinDB = coinModel.model()
diceDB = diceModel.model()
dividendDB = dividendModel.model()
goldDividendDB = goldDividend.model()
lotteryDB = lotteryModel.model()
revenueDB = revenueModel.model()
userDB = userModel.model()
pirate_robDB = robTransactionModel.model()
pirate_treasureDB = treasureModel.model()
redisDB = redis.redisObject()

gameInfo = config.gameInfo()
adminAddressDict = dict.fromkeys(gameInfo.getAdminWalletList(), 1)


def getTimeNow():
    return datetime.datetime.now(datetime.timezone.utc)


def mongoDBCoverter(object):
    for i in object:
        i["_id"] = str(i["_id"])
        i["createdAt"] = i["createdAt"].strftime("%Y/%m/%d, %H:%M:%S")
    return object

# def getGameDuringTime(type, game):
#     now = getTimeNow()
#     todayYear = now.year
#     todayMonth = now.month
#     todayDay = now.day
#
#     if type == "all":
#         if game == "coin":
#             coinOrder = redisDB.getObject("coin_all")
#             if coinOrder == None:
#                 coinOrder = mongoDBCoverter(coinDB.getAll())
#                 redisDB.saveObject("coin_all", coinOrder, 60)
#             return coinOrder
#
#         elif game == "dice":
#             diceOrder = redisDB.getObject("dice_all")
#             if diceOrder == None:
#                 diceOrder = mongoDBCoverter(diceDB.getAll())
#                 redisDB.saveObject("dice_all", diceOrder, 60)
#             return diceOrder
#
#         elif game == "lottery":
#             lotteryOrder = redisDB.getObject("lottery_all")
#             if lotteryOrder == None:
#                 lotteryOrder = mongoDBCoverter(lotteryDB.getAll())
#                 redisDB.saveObject("lottery_all", lotteryOrder, 60)
#             return lotteryOrder
#
#         elif game == "pirate_rob":
#             pirate_robOrder = redisDB.getObject("pirate_rob_all")
#             if pirate_robOrder == None:
#                 pirate_robOrder = mongoDBCoverter(pirate_robDB.getAll())
#                 redisDB.saveObject("pirate_rob_all", pirate_robOrder, 60)
#             return pirate_robOrder
#
#         elif game == "pirate_treasure":
#             pirate_treasureOrder = redisDB.getObject("pirate_treasure_all")
#             if pirate_treasureOrder == None:
#                 pirate_treasureOrder = mongoDBCoverter(pirate_treasureDB.getAll())
#                 redisDB.saveObject("pirate_treasure_all", pirate_treasureOrder, 60)
#             return pirate_treasureOrder
#
#     else:
#         if type == "today":
#             gtYear = todayYear
#             gtMonth = todayMonth
#             gtDay = todayDay
#         elif type == "yesterday":
#             gtTime = now - datetime.timedelta(days=1)
#             gtYear = gtTime.year
#             gtMonth = gtTime.month
#             gtDay = gtTime.day
#         elif type == "3 days":
#             gtTime = now - datetime.timedelta(days=3)
#             gtYear = gtTime.year
#             gtMonth = gtTime.month
#             gtDay = gtTime.day
#         elif type == "week":
#             gtTime = now - datetime.timedelta(days=(now.weekday() + 1))
#             gtYear = gtTime.year
#             gtMonth = gtTime.month
#             gtDay = gtTime.day
#         elif type == "month":
#             gtYear = now.year
#             gtMonth = now.month
#             gtDay = 1
#         else:
#             return [], [], []
#
#         ltTime = now + datetime.timedelta(days=1)
#         ltYear = ltTime.year
#         ltMonth = ltTime.month
#         ltDay = ltTime.day
#
#         if game == "coin":
#             coinOrder = coinDB.getByDuring(
#                 {"gtYear": gtYear, "gtMonth": gtMonth, "gtDay": gtDay, "ltYear": ltYear, "ltMonth": ltMonth,
#                  "ltDay": ltDay})
#             return coinOrder
#
#         elif game == "dice":
#             diceOrder = diceDB.getByDuring(
#                 {"gtYear": gtYear, "gtMonth": gtMonth, "gtDay": gtDay, "ltYear": ltYear, "ltMonth": ltMonth,
#                  "ltDay": ltDay})
#             return diceOrder
#
#         elif game == "lottery":
#             lotteryOrder = lotteryDB.getByDuring(
#                 {"gtYear": gtYear, "gtMonth": gtMonth, "gtDay": gtDay, "ltYear": ltYear, "ltMonth": ltMonth,
#                  "ltDay": ltDay})
#             return lotteryOrder
#
#         elif game == "pirate_rob":
#             pirate_robOrder = pirate_robDB.getByDuring(
#                 {"gtYear": gtYear, "gtMonth": gtMonth, "gtDay": gtDay, "ltYear": ltYear, "ltMonth": ltMonth,
#                  "ltDay": ltDay})
#             return pirate_robOrder
#
#         elif game == "pirate_treasure":
#             pirate_treasureOrder = pirate_treasureDB.getByDuring(
#                 {"gtYear": gtYear, "gtMonth": gtMonth, "gtDay": gtDay, "ltYear": ltYear, "ltMonth": ltMonth,
#                  "ltDay": ltDay})
#             return pirate_treasureOrder


def getGameDuringTime(type):
    now = getTimeNow()
    todayYear = now.year
    todayMonth = now.month
    todayDay = now.day

    if type == "all":
        coinOrder = redisDB.getObject("coin_all")
        if coinOrder == None:
            coinOrder = mongoDBCoverter(coinDB.getAll())
            redisDB.saveObject("coin_all", coinOrder, 60)

        diceOrder = redisDB.getObject("dice_all")
        if diceOrder == None:
            diceOrder = mongoDBCoverter(diceDB.getAll())
            redisDB.saveObject("dice_all", diceOrder, 60)

        lotteryOrder = redisDB.getObject("lottery_all")
        if lotteryOrder == None:
            lotteryOrder = mongoDBCoverter(lotteryDB.getAll())
            redisDB.saveObject("lottery_all", lotteryOrder, 60)

        pirate_robOrder = redisDB.getObject("pirate_rob_all")
        if pirate_robOrder == None:
            pirate_robOrder = mongoDBCoverter(pirate_robDB.getAll())
            redisDB.saveObject("pirate_rob_all", pirate_robOrder, 60)

        pirate_treasureOrder = redisDB.getObject("pirate_treasure_all")
        if pirate_treasureOrder == None:
            pirate_treasureOrder = mongoDBCoverter(pirate_treasureDB.getAll())
            redisDB.saveObject("pirate_treasure_all", pirate_treasureOrder, 60)

    else:
        if type == "today":
            gtYear = todayYear
            gtMonth = todayMonth
            gtDay = todayDay
        elif type == "yesterday":
            gtTime = now - datetime.timedelta(days=1)
            gtYear = gtTime.year
            gtMonth = gtTime.month
            gtDay = gtTime.day
        elif type == "3 days":
            gtTime = now - datetime.timedelta(days=3)
            gtYear = gtTime.year
            gtMonth = gtTime.month
            gtDay = gtTime.day
        elif type == "week":
            gtTime = now - datetime.timedelta(days=(now.weekday() + 1))
            gtYear = gtTime.year
            gtMonth = gtTime.month
            gtDay = gtTime.day
        elif type == "month":
            gtYear = now.year
            gtMonth = now.month
            gtDay = 1
        else:
            return [], [], []

        ltTime = now + datetime.timedelta(days=1)
        ltYear = ltTime.year
        ltMonth = ltTime.month
        ltDay = ltTime.day

        coinOrder = coinDB.getByDuring(
            {"gtYear": gtYear, "gtMonth": gtMonth, "gtDay": gtDay, "ltYear": ltYear, "ltMonth": ltMonth,
             "ltDay": ltDay})
        diceOrder = diceDB.getByDuring(
            {"gtYear": gtYear, "gtMonth": gtMonth, "gtDay": gtDay, "ltYear": ltYear, "ltMonth": ltMonth,
             "ltDay": ltDay})
        lotteryOrder = lotteryDB.getByDuring(
            {"gtYear": gtYear, "gtMonth": gtMonth, "gtDay": gtDay, "ltYear": ltYear, "ltMonth": ltMonth,
             "ltDay": ltDay})
        pirate_robOrder = pirate_robDB.getByDuring(
            {"gtYear": gtYear, "gtMonth": gtMonth, "gtDay": gtDay, "ltYear": ltYear, "ltMonth": ltMonth,
             "ltDay": ltDay})
        pirate_treasureOrder = pirate_treasureDB.getByDuring(
            {"gtYear": gtYear, "gtMonth": gtMonth, "gtDay": gtDay, "ltYear": ltYear, "ltMonth": ltMonth,
             "ltDay": ltDay})

    return coinOrder, lotteryOrder, diceOrder, pirate_robOrder, pirate_treasureOrder


def getDividendDuringTime(type):
    now = getTimeNow()
    todayYear = now.year
    todayMonth = now.month
    todayDay = now.day

    if type == "all":
        dividendOrder = redisDB.getObject("dividend_all")
        if dividendOrder == None:
            dividendOrder = mongoDBCoverter(dividendDB.getAll())
            redisDB.saveObject("dividend_all", dividendOrder, 60)

        goldDividendOrder = redisDB.getObject("goldDividend_all")
        if goldDividendOrder == None:
            goldDividendOrder = mongoDBCoverter(goldDividendDB.getAll())
            redisDB.saveObject("goldDividend_all", goldDividendOrder, 60)

    else:
        if type == "today":
            gtYear = todayYear
            gtMonth = todayMonth
            gtDay = todayDay
        elif type == "yesterday":
            gtTime = now - datetime.timedelta(days=1)
            gtYear = gtTime.year
            gtMonth = gtTime.month
            gtDay = gtTime.day
        elif type == "3 days":
            gtTime = now - datetime.timedelta(days=3)
            gtYear = gtTime.year
            gtMonth = gtTime.month
            gtDay = gtTime.day
        elif type == "week":
            gtTime = now - datetime.timedelta(days=(now.weekday() + 1))
            gtYear = gtTime.year
            gtMonth = gtTime.month
            gtDay = gtTime.day
        elif type == "month":
            gtYear = now.year
            gtMonth = now.month
            gtDay = 1
        else:
            return [], [], []

        ltTime = now + datetime.timedelta(days=1)
        ltYear = ltTime.year
        ltMonth = ltTime.month
        ltDay = ltTime.day

        dividendOrder = dividendDB.getByDuring(
            {"gtYear": gtYear, "gtMonth": gtMonth, "gtDay": gtDay, "ltYear": ltYear, "ltMonth": ltMonth,
             "ltDay": ltDay})
        goldDividendOrder = goldDividendDB.getByDuring(
            {"gtYear": gtYear, "gtMonth": gtMonth, "gtDay": gtDay, "ltYear": ltYear, "ltMonth": ltMonth,
             "ltDay": ltDay})

    return dividendOrder, goldDividendOrder


def getRevnueDuringTime(type):
    now = getTimeNow()

    if type == "all":
        revenueOrder = redisDB.getObject("revenue_all")
        if revenueOrder == None:
            revenueOrder = mongoDBCoverter(revenueDB.getAll())
            redisDB.saveObject("revenue_all", revenueOrder, 60)
    else:
        if type == "yesterday":
            gtTime = now - datetime.timedelta(days=1)
            gtYear = gtTime.year
            gtMonth = gtTime.month
            gtDay = gtTime.day
        elif type == "3 days":
            gtTime = now - datetime.timedelta(days=3)
            gtYear = gtTime.year
            gtMonth = gtTime.month
            gtDay = gtTime.day
        elif type == "week":
            gtTime = now - datetime.timedelta(days=(now.weekday() + 1))
            gtYear = gtTime.year
            gtMonth = gtTime.month
            gtDay = gtTime.day
        elif type == "month":
            gtYear = now.year
            gtMonth = now.month
            gtDay = 1
        else:
            return [], [], []

        ltTime = now + datetime.timedelta(days=1)
        ltYear = ltTime.year
        ltMonth = ltTime.month
        ltDay = ltTime.day

        revenueOrder = revenueDB.getByDuring(
            {"gtYear": gtYear, "gtMonth": gtMonth, "gtDay": gtDay, "ltYear": ltYear, "ltMonth": ltMonth,
             "ltDay": ltDay})

    return revenueOrder


def getUserDuringTime(type):
    now = getTimeNow()
    if type == "all":
        userOrder = redisDB.getObject("user_all")
        if userOrder == None:
            userOrder = mongoDBCoverter(userDB.getAll())
            redisDB.saveObject("user_all", userOrder, 300)

    else:
        if type == "month":
            gtYear = now.year
            gtMonth = now.month
            gtDay = 1

        ltTime = now + datetime.timedelta(days=1)
        ltYear = ltTime.year
        ltMonth = ltTime.month
        ltDay = ltTime.day

        userOrder = userDB.getByDuring(
            {"gtYear": gtYear, "gtMonth": gtMonth, "gtDay": gtDay, "ltYear": ltYear, "ltMonth": ltMonth,
             "ltDay": ltDay})

    return userOrder

