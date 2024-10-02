from models import coinModel, diceModel, dividendModel, goldDividend, lotteryModel, revenueModel, userModel, redis
from controllers import tools
from conf import config
import numpy as np
import pandas as pd

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

pearson = lambda x_simple, y_simple: np.corrcoef(x_simple, y_simple)
dataFrameCreater = lambda someList, col1, col2: pd.DataFrame(someList, columns=[col1, col2])
relationRateFormat = lambda r: round(r[0][1], 3)


# 計算透過遊戲獲得Prize跟玩dividend是否具備相關性
def relationOfGameAndDividend():
    coinOrder, lotteryOrder, diceOrder, pirate_robOrder, pirate_treasureOrder = tools.getGameDuringTime("all")
    dividendOrder, goldDividendOrder = tools.getDividendDuringTime("all")

    gameDict = {}
    dividendDict = {}
    goldDict = {}

    for i in coinOrder:
        if adminAddressDict.get(i["address"], 0) == 0:
            gameDict[i["address"]] = gameDict.get(i["address"], 0) + i["winPrize"]

    for i in lotteryOrder:
        if adminAddressDict.get(i["address"], 0) == 0:
            gameDict[i["address"]] = gameDict.get(i["address"], 0) + i["winPrize"]

    for i in diceOrder:
        if adminAddressDict.get(i["address"], 0) == 0:
            gameDict[i["address"]] = gameDict.get(i["address"], 0) + i["PrizeReward"]

    for i in dividendOrder:
        if adminAddressDict.get(i["address"], 0) == 0:
            if i["type"] == "stake":
                dividendDict[i["address"]] = dividendDict.get(i["address"], 0) + i["amount"]
            elif i["type"] == "unstake":
                dividendDict[i["address"]] = dividendDict.get(i["address"], 0) - i["amount"]

    for i in goldDividendOrder:
        if adminAddressDict.get(i["address"], 0) == 0:
            if i["type"] == "stake":
                goldDict[i["address"]] = goldDict.get(i["address"], 0) + i["amount"]
            elif i["type"] == "unstake":
                goldDict[i["address"]] = goldDict.get(i["address"], 0) - i["amount"]

    # 製作 game 跟 dividend 的 list 才能進行相關係數分析
    gamePrizeAndDividendList = []
    gamePrizeAndGoldList = []
    for key, values in gameDict.items():
        gamePrizeAndDividendList.append([values, dividendDict.get(key, 0)])
        gamePrizeAndGoldList.append([values, goldDict.get(key, 0)])

    for key, values in dividendDict.items():
        if gameDict.get(key, 0) == 0:
            gamePrizeAndDividendList.append([0, values])

    for key, values in goldDict.items():
        if gameDict.get(key, 0) == 0:
            gamePrizeAndGoldList.append([0, values])

    gamePrizeAndDividendDateFrame = dataFrameCreater(gamePrizeAndDividendList, "prizeFromGame", "dividend")
    r_dividend = pearson(gamePrizeAndDividendDateFrame["prizeFromGame"], gamePrizeAndDividendDateFrame["dividend"])

    gamePrizeAndGoldDividendDateFrame = dataFrameCreater(gamePrizeAndGoldList, "prizeFromGame", "gold")
    r_gold = pearson(gamePrizeAndGoldDividendDateFrame["prizeFromGame"], gamePrizeAndGoldDividendDateFrame["gold"])

    return {"relationOfGamePrizeAndDividend": gamePrizeAndDividendList,
            "gamePrizeAndDividendPearson": relationRateFormat(r_dividend),
            "relationOfGamePrizeAndGoldDividend": gamePrizeAndGoldList,
            "gamePrizeAndGoldDividendPearson": relationRateFormat(r_gold)}


# 計算玩各遊戲之間是否具備相關性
def relationOfPerGame():
    userOrder = tools.getUserDuringTime("all")
    coinOrder, lotteryOrder, diceOrder, pirate_robOrder, pirate_treasureOrder = tools.getGameDuringTime("all")

    coinDict = {}
    lotteryDict = {}
    diceDict = {}
    pirate_robDict = {}
    pirate_treasureDict = {}

    for i in coinOrder:
        if adminAddressDict.get(i["address"], 0) == 0:
            coinDict[i["address"]] = coinDict.get(i["address"], 0) + i["amount"]

    for i in lotteryOrder:
        if adminAddressDict.get(i["address"], 0) == 0:
            lotteryDict[i["address"]] = lotteryDict.get(i["address"], 0) + i["amount"]

    for i in diceOrder:
        if adminAddressDict.get(i["address"], 0) == 0:
            diceDict[i["address"]] = diceDict.get(i["address"], 0) + i["bet"]

    for i in pirate_robOrder:
        if adminAddressDict.get(i["robPlayer"], 0) == 0:
            pirate_robDict[i["robPlayer"]] = pirate_robDict.get(i["robPlayer"], 0) + i["robValue"]

    for i in pirate_treasureOrder:
        if adminAddressDict.get(i["owner"], 0) == 0:
            if i["isCreator"]:
                pirate_treasureDict[i["owner"]] = pirate_treasureDict.get(i["owner"], 0) + i["invest"]

    gameList = []
    for i in userOrder:
        gameList.append([coinDict.get(i["address"], 0), lotteryDict.get(i["address"], 0), diceDict.get(i["address"], 0),
                         pirate_robDict.get(i["address"], 0), pirate_treasureDict.get(i["address"], 0)])

    gameDataFrame = pd.DataFrame(gameList, columns=["coin", "lottery", "dice", "pirate_rob", "pirate_create"])

    r_coinAndLottery = pearson(gameDataFrame["coin"], gameDataFrame["lottery"])
    r_coinAndDice = pearson(gameDataFrame["coin"], gameDataFrame["dice"])
    r_coinAndPirate_rob = pearson(gameDataFrame["coin"], gameDataFrame["pirate_rob"])
    r_coinAndPirate_create = pearson(gameDataFrame["coin"], gameDataFrame["pirate_create"])

    r_lotteryAndDice = pearson(gameDataFrame["lottery"], gameDataFrame["dice"])
    r_lotteryAndPirate_rob = pearson(gameDataFrame["lottery"], gameDataFrame["pirate_rob"])
    r_lotteryAndPirate_create = pearson(gameDataFrame["lottery"], gameDataFrame["pirate_create"])

    r_diceAndPirate_rob = pearson(gameDataFrame["dice"], gameDataFrame["pirate_rob"])
    r_diceAndPirate_create = pearson(gameDataFrame["dice"], gameDataFrame["pirate_create"])

    r_pirate_robAndCreate = pearson(gameDataFrame["pirate_rob"], gameDataFrame["pirate_create"])

    return {"r_coinAndLottery": relationRateFormat(r_coinAndLottery),
            "r_coinAndDice": relationRateFormat(r_coinAndDice),
            "r_coinAndPirate_rob": relationRateFormat(r_coinAndPirate_rob),
            "r_coinAndPirate_create": relationRateFormat(r_coinAndPirate_create),
            "r_lotteryAndDice": relationRateFormat(r_lotteryAndDice),
            "r_lotteryAndPirate_rob": relationRateFormat(r_lotteryAndPirate_rob),
            "r_lotteryAndPirate_create": relationRateFormat(r_lotteryAndPirate_create),
            "r_diceAndPirate_rob": relationRateFormat(r_diceAndPirate_rob),
            "r_diceAndPirate_create": relationRateFormat(r_diceAndPirate_create),
            "r_pirate_robAndCreate": relationRateFormat(r_pirate_robAndCreate)}
