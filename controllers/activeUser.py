from controllers import tools
from conf import config
import datetime
from models import coinModel, diceModel, dividendModel, goldDividend, lotteryModel, revenueModel, userModel, \
    robTransactionModel, treasureModel, redis
import calendar

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


def userMonthActivate():
    now = tools.getTimeNow()
    ltTime = now + datetime.timedelta(days=1)
    ltYear = ltTime.year
    ltMonth = ltTime.month
    ltDay = ltTime.day

    thisYear = ltYear
    thisMonth = ltMonth
    thisMonthFirstDay = 1

    thisMonthFirstDate = now.replace(day=1)
    lastMonthDate = thisMonthFirstDate - datetime.timedelta(days=1)
    lastMonthFirstDate = lastMonthDate.replace(day=1)
    lastMonthYear = lastMonthFirstDate.year
    lastMonth = lastMonthFirstDate.month
    lastMonthFirstDay = lastMonthFirstDate.day

    # 以下是遊戲
    thisCoinOrder = redisDB.getObject("coin_thisMonth")
    if thisCoinOrder == None:
        thisCoinOrder = tools.mongoDBCoverter(
            coinDB.getByDuring(
                {"gtYear": thisYear, "gtMonth": thisMonth, "gtDay": thisMonthFirstDay, "ltYear": ltYear,
                 "ltMonth": ltMonth, "ltDay": ltDay})
        )
        redisDB.saveObject("coin_thisMonth", thisCoinOrder, 60)

    lastCoinOrder = redisDB.getObject("coin_lastMonth")
    if lastCoinOrder == None:
        lastCoinOrder = tools.mongoDBCoverter(
            coinDB.getByDuring(
                {"gtYear": lastMonthYear, "gtMonth": lastMonth, "gtDay": lastMonthFirstDay, "ltYear": thisYear,
                 "ltMonth": thisMonth, "ltDay": thisMonthFirstDay})
        )
        redisDB.saveObject("coin_lastMonth", lastCoinOrder, 60)

    thisDiceOrder = redisDB.getObject("dice_thisMonth")
    if thisDiceOrder == None:
        thisDiceOrder = tools.mongoDBCoverter(
            diceDB.getByDuring(
                {"gtYear": thisYear, "gtMonth": thisMonth, "gtDay": thisMonthFirstDay, "ltYear": ltYear,
                 "ltMonth": ltMonth, "ltDay": ltDay})
        )
        redisDB.saveObject("dice_thisMonth", thisDiceOrder, 60)

    lastDiceOrder = redisDB.getObject("dice_lastMonth")
    if lastDiceOrder == None:
        lastDiceOrder = tools.mongoDBCoverter(
            diceDB.getByDuring(
                {"gtYear": lastMonthYear, "gtMonth": lastMonth, "gtDay": lastMonthFirstDay, "ltYear": thisYear,
                 "ltMonth": thisMonth, "ltDay": thisMonthFirstDay})
        )
        redisDB.saveObject("dice_lastMonth", lastDiceOrder, 60)

    thislotteryOrder = redisDB.getObject("lottery_thisMonth")
    if thislotteryOrder == None:
        thislotteryOrder = tools.mongoDBCoverter(
            lotteryDB.getByDuring(
                {"gtYear": thisYear, "gtMonth": thisMonth, "gtDay": thisMonthFirstDay, "ltYear": ltYear,
                 "ltMonth": ltMonth, "ltDay": ltDay})
        )
        redisDB.saveObject("lottery_thisMonth", thislotteryOrder, 60)

    lastLotteryOrder = redisDB.getObject("lottery_lastMonth")
    if lastLotteryOrder == None:
        lastLotteryOrder = tools.mongoDBCoverter(
            lotteryDB.getByDuring(
                {"gtYear": lastMonthYear, "gtMonth": lastMonth, "gtDay": lastMonthFirstDay, "ltYear": thisYear,
                 "ltMonth": thisMonth, "ltDay": thisMonthFirstDay})
        )
        redisDB.saveObject("lottery_lastMonth", lastLotteryOrder, 60)

    # thisPirateRobOrder = redisDB.getObject("pirateRob_thisMonth")
    # if thisPirateRobOrder == None:
    #     thisPirateRobOrder = tools.mongoDBCoverter(
    #         pirate_robDB.getByDuring(
    #             {"gtYear": thisYear, "gtMonth": thisMonth, "gtDay": thisMonthFirstDay, "ltYear": ltYear,
    #              "ltMonth": ltMonth, "ltDay": ltDay})
    #     )
    #     redisDB.saveObject("pirateRob_thisMonth", thisPirateRobOrder, 60)
    #
    # lastPirateRobOrder = redisDB.getObject("pirateRob_lastMonth")
    # if lastPirateRobOrder == None:
    #     lastPirateRobOrder = tools.mongoDBCoverter(
    #         pirate_treasureDB.getByDuring(
    #             {"gtYear": lastMonthYear, "gtMonth": lastMonth, "gtDay": lastMonthFirstDay, "ltYear": thisYear,
    #              "ltMonth": thisMonth, "ltDay": thisMonthFirstDay})
    #     )
    #     redisDB.saveObject("pirateRob_lastMonth", lastPirateRobOrder, 60)

    thisPirateTreasureOrder = redisDB.getObject("pirateTreasure_thisMonth")
    if thisPirateTreasureOrder == None:
        thisPirateTreasureOrder = tools.mongoDBCoverter(
            pirate_treasureDB.getByDuring(
                {"gtYear": thisYear, "gtMonth": thisMonth, "gtDay": thisMonthFirstDay, "ltYear": ltYear,
                 "ltMonth": ltMonth, "ltDay": ltDay})
        )
        redisDB.saveObject("pirateTreasure_thisMonth", thisPirateTreasureOrder, 60)

    lastPirateTreasureOrder = redisDB.getObject("pirateRob_lastMonth")
    if lastPirateTreasureOrder == None:
        lastPirateTreasureOrder = tools.mongoDBCoverter(
            pirate_treasureDB.getByDuring(
                {"gtYear": lastMonthYear, "gtMonth": lastMonth, "gtDay": lastMonthFirstDay, "ltYear": thisYear,
                 "ltMonth": thisMonth, "ltDay": thisMonthFirstDay})
        )
        redisDB.saveObject("pirateRob_lastMonth", lastPirateTreasureOrder, 60)

    # 以下是defi
    thisDividendOrder = redisDB.getObject("dividend_thisMonth")
    if thisDividendOrder == None:
        thisDividendOrder = tools.mongoDBCoverter(
            dividendDB.getByDuring(
                {"gtYear": thisYear, "gtMonth": thisMonth, "gtDay": thisMonthFirstDay, "ltYear": ltYear,
                 "ltMonth": ltMonth, "ltDay": ltDay})
        )
        redisDB.saveObject("dividend_thisMonth", thisDividendOrder, 60)

    lastDividendOrder = redisDB.getObject("dividend_lastMonth")
    if lastDividendOrder == None:
        lastDividendOrder = tools.mongoDBCoverter(
            dividendDB.getByDuring(
                {"gtYear": lastMonthYear, "gtMonth": lastMonth, "gtDay": lastMonthFirstDay, "ltYear": thisYear,
                 "ltMonth": thisMonth, "ltDay": thisMonthFirstDay})
        )
        redisDB.saveObject("dividend_lastMonth", lastDividendOrder, 60)

    thisGoldDividendOrder = redisDB.getObject("goldDividend_thisMonth")
    if thisGoldDividendOrder == None:
        thisGoldDividendOrder = tools.mongoDBCoverter(
            goldDividendDB.getByDuring(
                {"gtYear": thisYear, "gtMonth": thisMonth, "gtDay": thisMonthFirstDay, "ltYear": ltYear,
                 "ltMonth": ltMonth, "ltDay": ltDay})
        )
        redisDB.saveObject("goldDividend_thisMonth", thisGoldDividendOrder, 60)

    lastGoldDividendOrder = redisDB.getObject("goldDividend_lastMonth")
    if lastGoldDividendOrder == None:
        lastGoldDividendOrder = tools.mongoDBCoverter(
            goldDividendDB.getByDuring(
                {"gtYear": lastMonthYear, "gtMonth": lastMonth, "gtDay": lastMonthFirstDay, "ltYear": thisYear,
                 "ltMonth": thisMonth, "ltDay": thisMonthFirstDay})
        )
        redisDB.saveObject("goldDividend_lastMonth", lastGoldDividendOrder, 60)

    # 以下進行計算
    thisMonthCoinActiveUser = countUniqueAddressNum(thisCoinOrder, "address")
    lastMonthCoinActiveUser = countUniqueAddressNum(lastCoinOrder, "address")

    thisMonthDiceActiveUser = countUniqueAddressNum(thisDiceOrder, "address")
    lastMonthDiceActiveUser = countUniqueAddressNum(lastDiceOrder, "address")

    thisMonthLotteryActiveUser = countUniqueAddressNum(thislotteryOrder, "address")
    lastMonthLotteryActiveUser = countUniqueAddressNum(lastLotteryOrder, "address")

    thisMonthPirateActiveUser = countUniqueAddressNum(thisPirateTreasureOrder, "owner")
    lastMonthPirateActiveUser = countUniqueAddressNum(lastPirateTreasureOrder, "owner")

    thisMonthDividendActiveUser = countUniqueAddressNum(thisDividendOrder, "address")
    lastMonthDividendActiveUser = countUniqueAddressNum(lastDividendOrder, "address")

    thisMonthGoldDividendActiveUser = countUniqueAddressNum(thisGoldDividendOrder, "address")
    lastMonthGoldDividendActiveUser = countUniqueAddressNum(lastGoldDividendOrder, "address")

    return {
        "monthlyActivateUser": {
            "thisMonth_coin": thisMonthCoinActiveUser, "lastMonth_coin": lastMonthCoinActiveUser,
            "thisMonth_lottery": thisMonthLotteryActiveUser, "lastMonth_lottery": lastMonthLotteryActiveUser,
            "thisMonth_dice": thisMonthDiceActiveUser, "lastMonth_dice": lastMonthDiceActiveUser,
            "thisMonth_pirate": thisMonthPirateActiveUser, "lastMonth_pirate": lastMonthPirateActiveUser,
            "thisMonth_dividend": thisMonthDividendActiveUser, "lastMonth_dividend": lastMonthDividendActiveUser,
            "thisMonth_goldDividend": thisMonthGoldDividendActiveUser,
            "lastMonth_goldDividend": lastMonthGoldDividendActiveUser
        }
    }


def userDailyActivate(item):
    now = tools.getTimeNow()
    gtYear = now.year
    gtMonth = now.month
    ltTime = now + datetime.timedelta(days=1)
    ltYear = ltTime.year
    ltMonth = ltTime.month
    ltDay = ltTime.day

    # 以下是遊戲
    if item == "coin":
        thisCoinOrder = redisDB.getObject("coin_thisMonth")
        if thisCoinOrder == None:
            thisCoinOrder = tools.mongoDBCoverter(
                coinDB.getByDuring(
                    {"gtYear": gtYear, "gtMonth": gtMonth, "gtDay": 1, "ltYear": ltYear,
                     "ltMonth": ltMonth, "ltDay": ltDay})
            )
            redisDB.saveObject("coin_thisMonth", thisCoinOrder, 60)

        return countUniqueAddressNumByDay(thisCoinOrder, "address", calendar.mdays[gtMonth])

    elif item == "dice":
        thisDiceOrder = redisDB.getObject("dice_thisMonth")
        if thisDiceOrder == None:
            thisDiceOrder = tools.mongoDBCoverter(
                diceDB.getByDuring(
                    {"gtYear": gtYear, "gtMonth": gtMonth, "gtDay": 1, "ltYear": ltYear,
                     "ltMonth": ltMonth, "ltDay": ltDay})
            )
            redisDB.saveObject("dice_thisMonth", thisDiceOrder, 60)

        return countUniqueAddressNumByDay(thisDiceOrder, "address", calendar.mdays[gtMonth])

    elif item == "lottery":
        thislotteryOrder = None  # redisDB.getObject("lottery_thisMonth")
        if thislotteryOrder == None:
            thislotteryOrder = tools.mongoDBCoverter(
                lotteryDB.getByDuring(
                    {"gtYear": gtYear, "gtMonth": gtMonth, "gtDay": 1, "ltYear": ltYear,
                     "ltMonth": ltMonth, "ltDay": ltDay})
            )
            redisDB.saveObject("lottery_thisMonth", thislotteryOrder, 60)
        return countUniqueAddressNumByDay(thislotteryOrder, "address", calendar.mdays[gtMonth])

    elif item == "pirate":
        thisPirateTreasureOrder = redisDB.getObject("pirateTreasure_thisMonth")
        if thisPirateTreasureOrder == None:
            thisPirateTreasureOrder = tools.mongoDBCoverter(
                pirate_treasureDB.getByDuring(
                    {"gtYear": gtYear, "gtMonth": gtMonth, "gtDay": 1, "ltYear": ltYear,
                     "ltMonth": ltMonth, "ltDay": ltDay})
            )
            redisDB.saveObject("pirateTreasure_thisMonth", thisPirateTreasureOrder, 60)

        return countUniqueAddressNumByDay(thisPirateTreasureOrder, "owner", calendar.mdays[gtMonth])

    # 以下是Defi
    elif item == "dividend":
        thisDividendOrder = redisDB.getObject("dividend_thisMonth")
        if thisDividendOrder == None:
            thisDividendOrder = tools.mongoDBCoverter(
                dividendDB.getByDuring(
                    {"gtYear": gtYear, "gtMonth": gtMonth, "gtDay": 1, "ltYear": ltYear,
                     "ltMonth": ltMonth, "ltDay": ltDay})
            )
            redisDB.saveObject("dividend_thisMonth", thisDividendOrder, 60)

        return countUniqueAddressNumByDay(thisDividendOrder, "address", calendar.mdays[gtMonth])

    elif item == "gold dividend":
        thisGoldDividendOrder = redisDB.getObject("goldDividend_thisMonth")
        if thisGoldDividendOrder == None:
            thisGoldDividendOrder = tools.mongoDBCoverter(
                goldDividendDB.getByDuring(
                    {"gtYear": gtYear, "gtMonth": gtMonth, "gtDay": 1, "ltYear": ltYear,
                     "ltMonth": ltMonth, "ltDay": ltDay})
            )
            redisDB.saveObject("goldDividend_thisMonth", thisGoldDividendOrder, 60)

        return countUniqueAddressNumByDay(thisGoldDividendOrder, "address", calendar.mdays[gtMonth])


def countUniqueAddressNum(someOrder, keyName):
    addressList = []
    for i in someOrder:
        if not i[keyName] in addressList:
            addressList.append(i[keyName])

    return len(addressList)


def countUniqueAddressNumByDay(someOrder, keyName, thisMonthDay):
    addressDict = [[] for i in range(thisMonthDay)]
    dateDict = {}
    for i in someOrder:
        day = int(i["createdAt"].split(',')[0][8:10]) - 1
        if not i[keyName] in addressDict[day]:
            addressDict[day].append(i[keyName])

    for i in range(thisMonthDay):
        if i + 1 < 10:
            key = "0" + str(i + 1)
        else:
            key = str(i + 1)
        dateDict[key] = dateDict.get(key, len(addressDict[i]))

    return dateDict
