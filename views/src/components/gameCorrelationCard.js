import React, { useEffect, useState } from "react";
import axios from 'axios';
import { css } from '@emotion/css';
import Grid from '@mui/material/Grid';

function GameCorrelationCard({ apiPath }) {
    const [coin_lottery, setCoin_lottery] = useState(0)
    const [coin_dice, setCoin_dice] = useState(0)
    const [coin_pirate_rob, setCoin_pirate_rob] = useState(0)
    const [coin_pirate_create, setCoin_pirate_create] = useState(0)
    const [lottery_dice, setLottery_dice] = useState(0)
    const [lottery_pirate_rob, setLottery_pirate_rob] = useState(0)
    const [lottery_pirate_create, setLottery_pirate_create] = useState(0)
    const [dice_pirate_rob, setDice_pirate_rob] = useState(0)
    const [dice_pirate_create, setDice_pirate_create] = useState(0)
    const [rob_create, setRob_create] = useState(0)


    useEffect(() => {
        axios.get(apiPath + "/relationOfPerGame").then((res) => {
            let result = res["data"]["detail"]
            setCoin_lottery(result["r_coinAndLottery"])
            setCoin_dice(result["r_coinAndDice"])
            setCoin_pirate_rob(result["r_coinAndPirate_rob"])
            setCoin_pirate_create(result["r_coinAndPirate_create"])
            setLottery_dice(result["r_lotteryAndDice"])
            setLottery_pirate_rob(result["r_lotteryAndPirate_rob"])
            setLottery_pirate_create(result["r_lotteryAndPirate_create"])
            setDice_pirate_rob(result["r_diceAndPirate_rob"])
            setDice_pirate_create(result["r_diceAndPirate_create"])
            setRob_create(result["r_pirate_robAndCreate"])
        }).catch(error => console.log(error))
    }, [apiPath])


    return (
        <div className={style}>

            <Grid container spacing={2}>
                <Grid item md={2} sm={4} xs={6} >
                    <div className="card">
                        <div className="cardTitle">Coin 跟 Lottery 的相關性</div>
                        <div className="activeNumber">
                            <div className="correlationNum">{coin_lottery}</div>
                        </div>
                    </div>
                </Grid>

                <Grid item md={2} sm={4} xs={6} >
                    <div className="card">
                        <div className="cardTitle">Coin 跟 Dice 的相關性</div>
                        <div className="activeNumber">
                            <div className="correlationNum">{coin_dice}</div>
                        </div>
                    </div>
                </Grid>

                <Grid item md={2} sm={4} xs={6} >
                    <div className="card">
                        <div className="cardTitle">Coin 跟 搶寶箱的相關性</div>
                        <div className="activeNumber">
                            <div className="correlationNum">{coin_pirate_rob}</div>
                        </div>
                    </div>
                </Grid>

                <Grid item md={2} sm={4} xs={6} >
                    <div className="card">
                        <div className="cardTitle">Coin 跟 創寶箱的相關性</div>
                        <div className="activeNumber">
                            <div className="correlationNum">{coin_pirate_create}</div>
                        </div>
                    </div>
                </Grid>

                <Grid item md={2} sm={4} xs={6} >
                    <div className="card">
                        <div className="cardTitle">Lottery 跟 Dice 的相關性</div>
                        <div className="activeNumber">
                            <div className="correlationNum">{lottery_dice}</div>
                        </div>
                    </div>
                </Grid>

                <Grid item md={2} sm={4} xs={6} >
                    <div className="card">
                        <div className="cardTitle">Lottery 跟 搶寶箱的相關性</div>
                        <div className="activeNumber">
                            <div className="correlationNum">{lottery_pirate_rob}</div>
                        </div>
                    </div>
                </Grid>

                <Grid item md={2} sm={4} xs={6} >
                    <div className="card">
                        <div className="cardTitle">Lottery 跟 創寶箱的相關性</div>
                        <div className="activeNumber">
                            <div className="correlationNum">{lottery_pirate_create}</div>
                        </div>
                    </div>
                </Grid>

                <Grid item md={2} sm={4} xs={6} >
                    <div className="card">
                        <div className="cardTitle">Dice 跟 搶寶箱的相關性</div>
                        <div className="activeNumber">
                            <div className="correlationNum">{dice_pirate_rob}</div>
                        </div>
                    </div>
                </Grid>

                <Grid item md={2} sm={4} xs={6} >
                    <div className="card">
                        <div className="cardTitle">Dice 跟 創寶箱的相關性</div>
                        <div className="activeNumber">
                            <div className="correlationNum">{dice_pirate_create}</div>
                        </div>
                    </div>
                </Grid>

                <Grid item md={2} sm={4} xs={6} >
                    <div className="card">
                        <div className="cardTitle">搶寶箱跟創寶箱的相關性</div>
                        <div className="activeNumber">
                            <div className="correlationNum">{rob_create}</div>
                        </div>
                    </div>
                </Grid>
            </Grid>

        </div>
    );
}

export default GameCorrelationCard;

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

    .correlationNum{
        font-size: 24px;
        font-weight: 800;
    }

    .progress{
        font-size: 20px;
        font-weight: 600;
    }
    
`;

