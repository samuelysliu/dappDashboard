import React, { useEffect, useState } from "react";
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';
import { Bar } from 'react-chartjs-2';
import axios from 'axios';
import { css } from '@emotion/css';

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

function NetIncomePerGameBar({ apiPath }) {
    const [itemTypeRevenue, setItemTypeRevenue] = useState([])

    useEffect(() => {
        axios.get(apiPath + "/netIncomePerGame").then((res) => {
            setItemTypeRevenue([res["data"]["detail"]["coinNetIncome"], res["data"]["detail"]["lotteryNetIncome"],
            res["data"]["detail"]["diceNetIncome"], res["data"]["detail"]["pirateNetIncome"], res["data"]["detail"]["dividendNetIncome"],
            res["data"]["detail"]["goldDividendNetIncome"]])
        }).catch(error => console.log(error))
    }, [apiPath])

    const options = {
        plugins: {
            title: {
                display: true,
                text: '各項目的淨收益',
            },
        },
        responsive: true,
        interaction: {
            intersect: false,
        },
        scales: {
            x: {
                stacked: true,
            },
            y: {
                stacked: true,
            }
        },
    };

    const data = {
        labels: ['coin', 'lottery', 'dice', 'pirate', 'dividend', 'gold dividend'],
        datasets: [
            {
                label: 'TT',
                data: itemTypeRevenue,
                backgroundColor: "#4EA8BE",
                stack: 'Stack 0',
            },
        ],
    };
    return (
        <div className={style}>
            <Bar options={options} data={data} height={300} style={{ backgroundColor: "white" }} />
        </div>
    );
}

export default NetIncomePerGameBar;

const style = css`
    
`;

