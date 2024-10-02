from fastapi import APIRouter
from controllers import basicInfo, rankInfo, activeUser, relationInfo
from models import redis

router = APIRouter()

redisDB = redis.redisObject()

# @router.get("/hello")
# def test():
#     return {"result": "hello"}

@router.get("/gameTime/{type}")
def gameTime(type: str):
    try:
        key = type
        result = redisDB.getObject("gameTime_" + key)
        if result == None:
            result = basicInfo.playTimePerGame({"type": type})
            redisDB.saveObject("gameTime_" + key, result, 60)

        return {"detail": result}

    except:
        return {"detail": "failed"}


# 尚未使用
# @router.get("/prizeFrom/{type}")
# async def prizeFrom(type: str):
#     try:
#         result = basicInfo.calGamePrize({"type": type})
#         return {"detail": result}
#     except:
#         return {"detail": "failed"}


@router.get("/moneyFrom/{type}")
def moneyFrom(type: str):
    try:
        key = type
        result = redisDB.getObject("moneyFrom_" + key)
        if result == None:
            result = basicInfo.calRevenue({"type": type})
            redisDB.saveObject("moneyFrom_" + key, result, 60)

        return {"detail": result}
    except:
        return {"detail": "failed"}


@router.get("/flowTrend")
def flowTrend():
    try:
        result = redisDB.getObject("flowTrend")
        if result == None:
            result = basicInfo.calTrendOfFlow()
            redisDB.saveObject("flowTrend", result, 60)

        return {"detail": result}
    except:
        return {"detail": "failed"}


@router.get("/revenueTrend")
def revenueTrend():
    try:
        result = redisDB.getObject("revenueTrend")
        if result == None:
            result = basicInfo.calTrendOfRevenue()
            redisDB.saveObject("revenueTrend", result, 60)

        return {"detail": result}
    except:
        return {"detail": "failed"}


@router.get("/addressTrend")
def addressTrend():
    try:
        result = redisDB.getObject("addressTrend")
        if result == None:
            result = basicInfo.callTrendOfAddress()
            redisDB.saveObject("addressTrend", result, 60)

        return {"detail": result}
    except:
        return {"detail": "failed"}


@router.get("/mostWinAddress/{records}")
async def mostWinAddress(records: int):
    try:
        result = redisDB.getObject("mostWinAddress")
        if result == None:
            result = rankInfo.mostWinAddress({"records": records})
            redisDB.saveObject("mostWinAddress", result, 60)
        return {"detail": result}
    except:
        return {"detail": "failed"}

@router.get("/userCameFrom")
async def userCameFrom():
    try:
        result = redisDB.getObject("userCameFrom")
        if result == None:
            result = rankInfo.userCameFrom()
            redisDB.saveObject("userCameFrom", result, 600)

        return {"detail": result}
    except:
        return {"detail": "failed"}

@router.get("/countryPreferGame")
async def countryPreferGame():
    try:
        result = redisDB.getObject("countryPreferGame")
        if result == None:
            result = rankInfo.rankCountryPreferGame()
            redisDB.saveObject("countryPreferGame", result, 600)

        return {"detail": result}
    except:
        return {"detail": "failed"}

@router.get("/userMonthlyActiveUser")
def userMonthlyActiveUser():
    try:
        result = redisDB.getObject("userMonthlyActiveUser")
        if result == None:
            result = activeUser.userMonthActivate()
            redisDB.saveObject("userMonthlyActiveUser", result, 600)

        return {"detail": result}
    except:
        return {"detail": "failed"}

@router.get("/userDailyActiveUser/{item}")
def userMonthlyActiveUser(item: str):
    try:
        result = redisDB.getObject("userDailyActiveUser_" + item)
        if result == None:
            result = activeUser.userDailyActivate(item)
            redisDB.saveObject("userDailyActiveUser_" + item, result, 600)

        return {"detail": result}
    except:
        return {"detail": "failed"}

@router.get("/gameBetAmountTime")
def gameBetAmountTime():
    try:
        result = redisDB.getObject("gameBetAmountTime")
        if result == None:
            result = rankInfo.betAmountTimeCal()
            redisDB.saveObject("gameBetAmountTime", result, 600)

        return {"detail": result}
    except:
        return {"detail": "failed"}

@router.get("/netIncomePerGame")
def incomeFromUserType():
    try:
        result = redisDB.getObject("netIncomePerGame")
        if result == None:
            result = basicInfo.netIncomePerGame()
            redisDB.saveObject("netIncomePerGame", result, 600)

        return {"detail": result}
    except:
        return {"detail": "failed"}


@router.get("/relationOfGameAndDividend")
def relationOfGameAndDividend():
    try:
        result = redisDB.getObject("relationOfGameAndDividend")
        if result == None:
            result = relationInfo.relationOfGameAndDividend()
            redisDB.saveObject("relationOfGameAndDividend", result, 600)

        return {"detail": result}
    except:
        return {"detail": "failed"}

@router.get("/relationOfPerGame")
async def relationOfPerGame():
    try:
        result = redisDB.getObject("relationOfPerGame")
        if result == None:
            result = relationInfo.relationOfPerGame()
            redisDB.saveObject("relationOfPerGame", result, 600)

        return {"detail": result}
    except:
        return {"detail": "failed"}