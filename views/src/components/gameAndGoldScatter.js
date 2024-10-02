import React, { useEffect, useState } from "react";
import { Chart as ChartJS, LinearScale, PointElement, LineElement, Tooltip, Legend } from 'chart.js';
import { Scatter } from 'react-chartjs-2';
import axios from 'axios';
import { css } from '@emotion/css';

ChartJS.register(LinearScale, PointElement, LineElement, Tooltip, Legend);

function GameAndGoldScatter({ apiPath }) {
    const [prizeFromGame_gold, setPrizeFromGame_gold] = useState([])
    const [correlation, setCorrelation] = useState(0)

    useEffect(() => {
        axios.get(apiPath + "/relationOfGameAndDividend").then((res) => {
            setPrizeFromGame_gold(res["data"]["detail"]["relationOfGamePrizeAndGoldDividend"])
            setCorrelation(res["data"]["detail"]["gamePrizeAndGoldDividendPearson"])
        }).catch(error => console.log(error))
    }, [apiPath])

    const options = {
        scales: {
            y: {
                beginAtZero: true,
            },
        },
    };

    const data = {
        datasets: [
            {
                label: 'Prize from game and Gold Dividend stake',
                data: prizeFromGame_gold,
                backgroundColor: 'rgba(255, 99, 132, 1)',
            },
        ],
    };
    return (
        <div className={style}>
            <p>相關係數：{correlation}</p>
            <Scatter options={options} data={data} height={300} style={{ backgroundColor: "white" }} />
        </div>
    );
}

export default GameAndGoldScatter;

const style = css`
    
`;

