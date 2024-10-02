from models import coinModel, diceModel, dividendModel, goldDividend, lotteryModel, revenueModel, userModel, redis
from controllers import tools
import calendar
from conf import config

coinDB = coinModel.model()
diceDB = diceModel.model()
dividendDB = dividendModel.model()
goldDividendDB = goldDividend.model()
lotteryDB = lotteryModel.model()
revenueDB = revenueModel.model()
userDB = userModel.model()
redisDB = redis.redisObject()

gameInfo = config.gameInfo()
adminAddressDict = dict.fromkeys(gameInfo.getAdminWalletList(), 1)


def playTimePerGame(*args):
    coinOrder, lotteryOrder, diceOrder, pirate_robOrder, pirate_treasureOrder = tools.getGameDuringTime(args[0]["type"])
    totalPlayTime = len(coinOrder) + len(lotteryOrder) + len(diceOrder) + len(pirate_robOrder)

    return {"totalPlayTime": totalPlayTime, "coinTime": len(coinOrder), "lotteryTime": len(lotteryOrder),
            "diceTime": len(diceOrder), "pirateTime": len(pirate_robOrder)}


def calGamePrize(*args):
    coinOrder, lotteryOrder, diceOrder, pirate_robOrder, pirate_treasureOrder = tools.getGameDuringTime(args[0]["type"])
    coinPrize = 0
    for i in coinOrder:
        coinPrize += i["winPrize"]

    lotteryPrize = 0
    for i in lotteryOrder:
        lotteryPrize += i["winPrize"]

    dicePrize = 0
    for i in diceOrder:
        dicePrize += i["PrizeReward"]

    return {"coin": coinPrize, "lottery": lotteryPrize, "dice": dicePrize}


def calRevenue(*args):
    revenueOrder = tools.getRevnueDuringTime(args[0]["type"])
    moneyType = {}
    for i in revenueOrder:
        moneyType[i["type"]] = moneyType.get(i["type"], 0) + i["amount"]

    return {"moneyType": moneyType}


def calTrendOfFlow(*args):
    coinOrder, lotteryOrder, diceOrder, pirate_robOrder, pirate_treasureOrder = tools.getGameDuringTime("month")
    now = tools.getTimeNow()
    todayYear = now.year
    todayMonth = now.month
    firstDay, monthRange = calendar.monthrange(todayYear, todayMonth)
    flowArray = {}

    for i in coinOrder:
        if adminAddressDict.get(i["address"], 0) == 0:
            key = str(i["createdAt"].day)
            flowArray[key] = flowArray.get(key, 0) + 1

    for i in lotteryOrder:
        if adminAddressDict.get(i["address"], 0) == 0:
            key = str(i["createdAt"].day)
            flowArray[key] = flowArray.get(key, 0) + 1

    for i in diceOrder:
        if adminAddressDict.get(i["address"], 0) == 0:
            key = str(i["createdAt"].day)
            flowArray[key] = flowArray.get(key, 0) + 1

    for i in pirate_robOrder:
        if adminAddressDict.get(i["robPlayer"], 0) == 0:
            key = str(i["createdAt"].day)
            flowArray[key] = flowArray.get(key, 0) + 1

    for i in range(monthRange):
        flowArray[str(i + 1)] = flowArray.get(str(i + 1), 0)

    return {"flowArray": flowArray}


def calTrendOfRevenue(*args):
    revenueOrder = tools.getRevnueDuringTime("month")
    revenueArray = {}
    now = tools.getTimeNow()
    todayYear = now.year
    todayMonth = now.month
    firstDay, monthRange = calendar.monthrange(todayYear, todayMonth)

    for i in revenueOrder:
        key = str(i["createdAt"].day)
        revenueArray[key] = revenueArray.get(key, 0) + i["amount"]

    for i in range(monthRange):
        revenueArray[str(i + 1)] = revenueArray.get(str(i + 1), 0)

    return {"revenueArray": revenueArray}


def callTrendOfAddress(*args):
    userOrder = tools.getUserDuringTime("month")
    now = tools.getTimeNow()
    todayYear = now.year
    todayMonth = now.month
    firstDay, monthRange = calendar.monthrange(todayYear, todayMonth)
    userArray = {}

    for i in userOrder:
        if adminAddressDict.get(i["address"], 0) == 0:
            key = str(i["createdAt"].day)
            userArray[key] = userArray.get(key, 0) + 1

    for i in range(monthRange):
        userArray[str(i + 1)] = userArray.get(str(i + 1), 0)

    return {"addressArray": userArray}


# 根據項目營收減去支出算出淨收益
def netIncomePerGame():
    coinOrder, lotteryOrder, diceOrder, pirate_robOrder, pirate_treasureOrder = tools.getGameDuringTime("all")
    dividendOrder, goldDividendOrder = tools.getDividendDuringTime("all")

    # 開始計算從遊戲來的淨收益(扣除用戶賺走的)
    coinNetIncome = 0
    lotteryNetIncome = 0
    diceNetIncome = 0
    pirateNetIncome = 0
    dividendNetIncome = 0
    goldNetIncome = 0

    for i in coinOrder:
        coinNetIncome += (i["amount"] - i["winTT"])

    for i in lotteryOrder:
        lotteryNetIncome += (i["amount"] - i["winTT"])

    for i in diceOrder:
        diceNetIncome += (i["bet"] - i["TTReward"])

    for i in pirate_treasureOrder:
        pirateNetIncome += i["collectFeeValue"]

    for i in dividendOrder:
        if i["type"] == "stake":
            dividendNetIncome += (i["amount"] * 100)
        elif i["type"] == "unstake":
            dividendNetIncome -= (i["amount"] * 100)
        elif i["type"] == "claim":
            dividendNetIncome -= i["amount"]

    for i in goldDividendOrder:
        if i["type"] == "stake":
            goldNetIncome += (i["amount"] / 366 * 200)
        elif i["type"] == "unstake":
            goldNetIncome -= (i["amount"] / 366 * 200)
        elif i["type"] == "claim":
            goldNetIncome -= i["amount"]

    return {"coinNetIncome": coinNetIncome, "lotteryNetIncome": lotteryNetIncome, "diceNetIncome": diceNetIncome,
            "pirateNetIncome": pirateNetIncome, "dividendNetIncome": dividendNetIncome,
            "goldDividendNetIncome": goldNetIncome}
