import React, { useEffect, useState } from "react";
import { Chart as ChartJS, LinearScale, PointElement, LineElement, Tooltip, Legend } from 'chart.js';
import { Scatter } from 'react-chartjs-2';
import axios from 'axios';
import { css } from '@emotion/css';

ChartJS.register(LinearScale, PointElement, LineElement, Tooltip, Legend);

function GameAndDividendScatter({ apiPath }) {
    const [prizeFromGame_dividend, setPrizeFromGame_dividend] = useState([])
    const [correlation, setCorrelation] = useState(0)

    useEffect(() => {
        axios.get(apiPath + "/relationOfGameAndDividend").then((res) => {
            setPrizeFromGame_dividend(res["data"]["detail"]["relationOfGamePrizeAndDividend"])
            setCorrelation(res["data"]["detail"]["gamePrizeAndDividendPearson"])
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
                label: 'Prize from game and Dividend stake',
                data: prizeFromGame_dividend,
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

export default GameAndDividendScatter;

const style = css`
    
`;

