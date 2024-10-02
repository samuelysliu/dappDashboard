import React, { useEffect, useState } from "react";
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';
import { Bar } from 'react-chartjs-2';
import axios from 'axios';
import { css } from '@emotion/css';

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

function BetTimeBar({ apiPath, item }) {
    const [betTime, setBetTime] = useState([])

    useEffect(() => {
        axios.get(apiPath + "/gameBetAmountTime").then((res) => {
            let result = res["data"]["detail"]
            if(item === "coin")
                setBetTime(result.coinBetAmountTime)
            else if(item === "dice")
                setBetTime(result.diceBetAmountTime)
            else if(item === "lottery")
                setBetTime(result.lotteryBetAmountTime)
            else if(item === "pirate create")
                setBetTime(result.pirateCreateAmountTime)
            else if(item === "pirate rob")
                setBetTime(result.pirateRobAmountTime)
        }).catch(error => console.log(error))


    }, [apiPath])

    const options = {
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: '下注次數',
            },
        },
    };

    const data = {
        labels: [],
        datasets: [
            {
                label: 'TT',
                data: betTime,
                backgroundColor: "#4EA8BE",
            },
        ],
    };
    return (
        <div className={style}>
            <Bar options={options} data={data} style={{ backgroundColor: "white" }} />
        </div>
    );
}

export default BetTimeBar;

const style = css`
    
`;

