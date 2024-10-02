from controllers import tools
from conf import config

gameInfo = config.gameInfo()
adminAddressDict = dict.fromkeys(gameInfo.getAdminWalletList(), 1)


# 計算地址在我們遊戲賺了多少錢
def mostWinAddress(*args):
    coinOrder, lotteryOrder, diceOrder, pirate_robOrder, pirate_treasureOrder = tools.getGameDuringTime("all")

    addressWin = {}

    for j in coinOrder:
        addressWin[j["address"]] = addressWin.get(j["address"], 0) + j["winTT"] - j["amount"]

    for j in lotteryOrder:
        addressWin[j["address"]] = addressWin.get(j["address"], 0) + j["winTT"] - j["amount"]

    for j in diceOrder:
        addressWin[j["address"]] = addressWin.get(j["address"], 0) + j["TTReward"] - j["bet"]

    for j in pirate_treasureOrder:
        if j["isCollected"]:
            addressWin[j["owner"]] = addressWin.get(j["owner"], 0) + j["collectValue"] - j["invest"]


    sorted_keys = sorted(addressWin, key=addressWin.get, reverse=True)
    sorted_address = {}
    j = 0

    for i in sorted_keys:
        if j < int(args[0]["records"]):
            if adminAddressDict.get(i, 0) == 1:
                j -= 1
            else:
                sorted_address[i] = addressWin[i]
        else:
            break
        j += 1

    return {"addressWin": sorted_address}


def userCameFrom():
    userOrder = tools.getUserDuringTime("all")
    countryDict = {}
    for i in userOrder:
        countryDict[i["region"]] = countryDict.get(i["region"], 0) + 1
    return {"userCameFrom": list(countryDict.items())}


def normalGameCal(topThreeCountryDict, order, addressDict, address, type):
    for i in order:
        region = addressDict.get(i[address], "0")
        if region in topThreeCountryDict:
            topThreeCountryDict.update({region: {type: topThreeCountryDict[region][type] + 1}})


def rankCountryPreferGame():
    userOrder = tools.getUserDuringTime("all")
    addressDict = {}

    # 根據人數排序國家
    country = sorted(userCameFrom()["userCameFrom"], key=lambda x: x[1])

    topThreeCountryDict = {
        country[-1][0]: {"coin": 0, "dice": 0, "lottery": 0, "robTreasure": 0, "createTreasure": 0},
        country[-2][0]: {"coin": 0, "dice": 0, "lottery": 0, "robTreasure": 0, "createTreasure": 0},
        country[-3][0]: {"coin": 0, "dice": 0, "lottery": 0, "robTreasure": 0, "createTreasure": 0},
    }

    # 取得每個地址所屬的國家
    for i in userOrder:
        addressDict[i["address"]] = i["region"]

    coinOrder, lotteryOrder, diceOrder, pirate_robOrder, pirate_treasureOrder = tools.getGameDuringTime("all")


    for i in coinOrder:
        region = addressDict.get(i["address"], "0")
        if region in topThreeCountryDict:
            topThreeCountryDict[region]["coin"] += 1

    for i in lotteryOrder:
        region = addressDict.get(i["address"], "0")
        if region in topThreeCountryDict:
            topThreeCountryDict[region]["lottery"] += 1

    for i in diceOrder:
        region = addressDict.get(i["address"], "0")
        if region in topThreeCountryDict:
            topThreeCountryDict[region]["dice"] += 1

    for i in pirate_robOrder:
        region = addressDict.get(i["robPlayer"], "0")
        if region in topThreeCountryDict:
            topThreeCountryDict[region]["robTreasure"] += 1

    for i in pirate_treasureOrder:
        if i["isCreator"]:
            region = addressDict.get(i["owner"], "0")
            if region in topThreeCountryDict:
                topThreeCountryDict[region]["createTreasure"] += 1

    return topThreeCountryDict


def betAmountTimeCal():
    coinOrder, lotteryOrder, diceOrder, pirate_robOrder, pirate_treasureOrder = tools.getGameDuringTime("all")

    coinBetDict = {}
    lotteryBetDict = {}
    diceBetDict = {}
    pirateRobBetDict = {}
    pirateCreateBetDict = {}

    for i in coinOrder:
        if adminAddressDict.get(i["address"], 0) == 0:
            coinBetDict[i["amount"]] = coinBetDict.get(i["amount"], 0) + 1

    for i in lotteryOrder:
        if adminAddressDict.get(i["address"], 0) == 0:
            lotteryBetDict[i["amount"]] = lotteryBetDict.get(i["amount"], 0) + 1

    for i in diceOrder:
        if adminAddressDict.get(i["address"], 0) == 0:
            diceBetDict[i["bet"]] = diceBetDict.get(i["bet"], 0) + 1

    for i in pirate_robOrder:
        if adminAddressDict.get(i["robPlayer"], 0) == 0:
            pirateRobBetDict[i["robValue"]] = pirateRobBetDict.get(i["robValue"], 0) + 1

    for i in pirate_treasureOrder:
        if i["isCreator"]:
            if adminAddressDict.get(i["owner"], 0) == 0:
                pirateCreateBetDict[i["invest"]] = pirateCreateBetDict.get(i["invest"], 0) + 1

    return {"coinBetAmountTime": coinBetDict, "lotteryBetAmountTime": lotteryBetDict, "diceBetAmountTime": diceBetDict,
            "pirateRobAmountTime": pirateRobBetDict, "pirateCreateAmountTime": pirateCreateBetDict}
