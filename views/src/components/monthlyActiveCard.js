import React, { useEffect, useState } from "react";
import axios from 'axios';
import { css } from '@emotion/css';
import Grid from '@mui/material/Grid';

function MonthlyActiveCard({ apiPath }) {
    const [coinMonthlyActive, setCoinMonthlyActive] = useState(0)
    const [coinProgress, setCoinProgress] = useState(0)

    const [lotteryMonthlyActive, setLotteryMonthlyActive] = useState(0)
    const [lotteryProgress, setLotteryProgress] = useState(0)

    const [diceMonthlyActive, setDiceMonthlyActive] = useState(0)
    const [diceProgress, setDiceProgress] = useState(0)

    const [pirateMonthlyActive, setPirateMonthlyActive] = useState(0)
    const [pirateProgress, setPirateProgress] = useState(0)

    const [dividendMonthlyActive, setDividendMonthlyActive] = useState(0)
    const [dividendProgress, setDividendProgress] = useState(0)

    const [goldMonthlyActive, setGoldMonthlyActive] = useState(0)
    const [goldProgress, setGoldProgress] = useState(0)

    useEffect(() => {
        axios.get(apiPath + "/userMonthlyActiveUser").then((res) => {
            let result = res["data"]["detail"]["monthlyActivateUser"]
            setCoinMonthlyActive(result.thisMonth_coin)
            setCoinProgress(Math.round((result.thisMonth_coin / result.lastMonth_coin - 1) * 10000) / 100)

            setLotteryMonthlyActive(result.thisMonth_lottery)
            setLotteryProgress(Math.round((result.thisMonth_lottery / result.lastMonth_lottery - 1) * 10000) / 100)

            setDiceMonthlyActive(result.thisMonth_dice)
            setDiceProgress(Math.round((result.thisMonth_dice / result.lastMonth_dice - 1) * 10000) / 100)

            setPirateMonthlyActive(result.thisMonth_pirate)
            setPirateProgress(Math.round((result.thisMonth_pirate / result.lastMonth_pirate - 1) * 10000) / 100)

            setDividendMonthlyActive(result.thisMonth_dividend)
            setDividendProgress(Math.round((result.thisMonth_dividend / result.lastMonth_dividend - 1) * 10000) / 100)

            setGoldMonthlyActive(result.thisMonth_goldDividend)
            setGoldProgress(Math.round((result.thisMonth_goldDividend / result.lastMonth_goldDividend - 1) * 10000) / 100)

        }).catch(error => console.log(error))
    }, [apiPath])


    return (
        <div className={style}>

            <Grid container spacing={2}>
                <Grid item md={2} sm={4} xs={6} >
                    <div className="card">
                        <div className="cardTitle">Coin</div>
                        <div className="activeNumber">
                            <div className="thisMonth">{coinMonthlyActive}</div>
                            <div className="progress">
                                <font style={{ color: coinProgress < 0 ? "red" : "green" }}>{coinProgress}%</font>
                            </div>
                        </div>
                    </div>
                </Grid>

                <Grid item md={2} sm={4} xs={6} className="chart">
                    <div className="card">
                        <div className="cardTitle">Dice</div>
                        <div className="activeNumber">
                            <div className="thisMonth">{diceMonthlyActive}</div>
                            <div className="progress">
                                <font style={{ color: diceProgress < 0 ? "red" : "green" }}>{diceProgress}%</font>
                            </div>
                        </div>
                    </div>
                </Grid>

                <Grid item md={2} sm={4} xs={6} className="chart">
                    <div className="card">
                        <div className="cardTitle">Lottery</div>
                        <div className="activeNumber">
                            <div className="thisMonth">{lotteryMonthlyActive}</div>
                            <div className="progress">
                                <font style={{ color: lotteryProgress < 0 ? "red" : "green" }}>{lotteryProgress}%</font>
                            </div>
                        </div>
                    </div>
                </Grid>

                <Grid item md={2} sm={4} xs={6} className="chart">
                    <div className="card">
                        <div className="cardTitle">Pirate</div>
                        <div className="activeNumber">
                            <div className="thisMonth">{pirateMonthlyActive}</div>
                            <div className="progress">
                                <font style={{ color: pirateProgress < 0 ? "red" : "green" }}>{pirateProgress}%</font>
                            </div>
                        </div>
                    </div>
                </Grid>

                <Grid item md={2} sm={4} xs={6} className="chart">
                    <div className="card">
                        <div className="cardTitle">Dividend</div>
                        <div className="activeNumber">
                            <div className="thisMonth">{dividendMonthlyActive}</div>
                            <div className="progress">
                                <font style={{ color: dividendProgress < 0 ? "red" : "green" }}>{dividendProgress}%</font>
                            </div>
                        </div>
                    </div>
                </Grid>

                <Grid item md={2} sm={4} xs={6} className="chart">
                    <div className="card">
                        <div className="cardTitle">Gold Dividend</div>
                        <div className="activeNumber">
                            <div className="thisMonth">{goldMonthlyActive}</div>
                            <div className="progress">
                                <font style={{ color: goldProgress < 0 ? "red" : "green" }}>{goldProgress}%</font>
                            </div>
                        </div>
                    </div>
                </Grid>
            </Grid>

        </div>
    );
}

export default MonthlyActiveCard;

const style = css`
    .card{
        background-color: white;
        text-align: left;
        padding: 10px;
        border-radius: 15px;
        width: 80%;
    }

    .card .cardTitle{
        font-size: 16px;
        font-weight: 700;
    }

    .activeNumber{
        display: flex;
        justify-content: space-around;
        align-items: flex-end;
    }

    .thisMonth{
        font-size: 36px;
        font-weight: 800;
    }

    .progress{
        font-size: 20px;
        font-weight: 600;
    }
    
`;

