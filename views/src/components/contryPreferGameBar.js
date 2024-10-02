import React, { useEffect, useState } from "react";
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';
import { Bar } from 'react-chartjs-2';
import axios from 'axios';
import { css } from '@emotion/css';

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

function ContryPreferGameBar({ apiPath }) {
    const [coinTime, setCoinTime] = useState([])
    const [lotteryTime, setLotteryTime] = useState([])
    const [diceTime, setDiceTime] = useState([])
    const [pirateCreateTime, setPirateCreateTime] = useState([])
    const [pirateRobTime, setPirateRobTime] = useState([])

    const [top3Country, setTop3Country] = useState([])

    useEffect(() => {
        axios.get(apiPath + "/countryPreferGame").then((res) => {
            let result = res["data"]["detail"]
            setTop3Country([Object.keys(result)[0], Object.keys(result)[1], Object.keys(result)[2]])
            setCoinTime([result[Object.keys(result)[0]].coin, result[Object.keys(result)[1]].coin, result[Object.keys(result)[2]].coin])
            setLotteryTime([result[Object.keys(result)[0]].lottery, result[Object.keys(result)[1]].lottery, result[Object.keys(result)[2]].lottery])
            setDiceTime([result[Object.keys(result)[0]].dice, result[Object.keys(result)[1]].dice, result[Object.keys(result)[2]].dice])
            setPirateCreateTime([result[Object.keys(result)[0]].createTreasure, result[Object.keys(result)[1]].createTreasure, result[Object.keys(result)[2]].createTreasure])
            setPirateRobTime([result[Object.keys(result)[0]].robTreasure, result[Object.keys(result)[1]].robTreasure, result[Object.keys(result)[2]].robTreasure])
        }).catch(error => console.log(error))
    }, [apiPath])

    const options = {
        plugins: {
            title: {
                display: true,
                text: '遊玩次數',
            },
            legend: {
                position: 'top',
              },
        },
        responsive: true,
    };

    const data = {
        labels: top3Country,
        datasets: [
            {
                label: 'Coin',
                data: coinTime,
                backgroundColor: "#4EA8BE",
            },
            {
                label: 'Lottery',
                data: lotteryTime,
                backgroundColor: "#D27E14",
            },
            {
                label: 'Dice',
                data: diceTime,
                backgroundColor: "#E5DCC5",
            },
            {
                label: 'pirateCreateTime',
                data: pirateCreateTime,
                backgroundColor: "#FF6343",
            },
            {
                label: 'pirateRobTime',
                data: pirateRobTime,
                backgroundColor: "#58b000",
            },
        ],
    };
    return (
        <div className={style}>
            <Bar options={options} data={data} height={300} style={{ backgroundColor: "white" }} />
        </div>
    );
}

export default ContryPreferGameBar;

const style = css`
    
`;

