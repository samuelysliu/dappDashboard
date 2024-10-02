import React, { useEffect, useState } from "react";
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js';
import { Line } from 'react-chartjs-2';
import axios from 'axios';
import { css } from '@emotion/css';

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

function DailyActiveUserLine({ apiPath }) {
    const [thisMonthDate, setThisMonthDate] = useState([])
    const [dailyCoin, setDailyCoin] = useState([])
    const [dailyLottery, setDailyLottery] = useState([])
    const [dailyDice, setDailyDice] = useState([])
    const [dailyPirate, setDailyPirate] = useState([])
    const [dailyDividend, setDailyDividend] = useState([])
    const [dailyGold, setDailyGold] = useState([])


    const jsonLenthCal = (jsonFormat) => {
        let jsonLength = 0
        for (let i in jsonFormat) {
            jsonLength += 1
        }
        return jsonLength
    }

    const monthDateAppend = (monthDateLength) => {
        let tempDate = []
        for (let i = 1; i <= monthDateLength; i++) {
            tempDate.push(i)
        }
        return tempDate
    }

    const dailyDateCal = (monthDateLength, jsonObject) => {
        let tempDaily = []
        for (let i = 1; i <= monthDateLength; i++) {
            if (i < 10) {
                tempDaily.push(jsonObject["0" + i.toString()])
            } else {
                tempDaily.push(jsonObject[i.toString()])
            }
        }
        return tempDaily
    }


    useEffect(() => {
        axios.get(apiPath + "/userDailyActiveUser/coin").then((res) => {
            let result = res["data"]["detail"]
            let monthDateLength = jsonLenthCal(result)
            setThisMonthDate(monthDateAppend(monthDateLength))
            setDailyCoin(dailyDateCal(monthDateLength, result))
        }).catch(error => console.log(error))

        axios.get(apiPath + "/userDailyActiveUser/lottery").then((res) => {
            let result = res["data"]["detail"]
            let monthDateLength = jsonLenthCal(result)

            setDailyLottery(dailyDateCal(monthDateLength, result))
        }).catch(error => console.log(error))

        axios.get(apiPath + "/userDailyActiveUser/dice").then((res) => {
            let result = res["data"]["detail"]
            let monthDateLength = jsonLenthCal(result)
            
            setDailyDice(dailyDateCal(monthDateLength, result))
        }).catch(error => console.log(error))

        axios.get(apiPath + "/userDailyActiveUser/pirate").then((res) => {
            let result = res["data"]["detail"]
            let monthDateLength = jsonLenthCal(result)

            setDailyPirate(dailyDateCal(monthDateLength, result))
        }).catch(error => console.log(error))

        axios.get(apiPath + "/userDailyActiveUser/dividend").then((res) => {
            let result = res["data"]["detail"]
            let monthDateLength = jsonLenthCal(result)

            setDailyDividend(dailyDateCal(monthDateLength, result))
        }).catch(error => console.log(error))

        axios.get(apiPath + "/userDailyActiveUser/gold dividend").then((res) => {
            let result = res["data"]["detail"]
            let monthDateLength = jsonLenthCal(result)

            setDailyGold(dailyDateCal(monthDateLength, result))
        }).catch(error => console.log(error))
    }, [apiPath])

    const options = {
        plugins: {
            title: {
                display: true,
                text: '每日活躍用戶數',
            },
        },
        responsive: true,
        interaction: {
            mode: 'index',
            intersect: false,
        },
        stacked: false,
        scales: {
            y: {
                type: 'linear',
                display: true,
                position: 'left',
            },
            y1: {
                type: 'linear',
                display: true,
                position: 'right',
                grid: {
                    drawOnChartArea: false,
                },
            },
        },
    };

    const data = {
        labels: thisMonthDate,
        datasets: [
            {
                label: 'Coin',
                data: dailyCoin,
                borderColor: "#4EA8BE",
                backgroundColor: "#4EA8BE",
                yAxisID: 'y',
            },
            {
                label: 'Dice',
                data: dailyDice,
                borderColor: "#D27E14",
                backgroundColor: "#D27E14",
                yAxisID: 'y',
            },
            {
                label: 'Lottery',
                data: dailyLottery,
                borderColor: "#E5DCC5",
                backgroundColor: "#E5DCC5",
                yAxisID: 'y',
            },
            {
                label: 'Pirate',
                data: dailyCoin,
                borderColor: "#FF6343",
                backgroundColor: "#FF6343",
                yAxisID: 'y',
            },
            {
                label: 'Dividend',
                data: dailyDividend,
                borderColor: "#a574ff",
                backgroundColor: "#a574ff",
                yAxisID: 'y1',
            },
            {
                label: 'Gold Dividend',
                data: dailyGold,
                borderColor: "#1300a6",
                backgroundColor: "#1300a6",
                yAxisID: 'y1',
            },
        ],
    };
    return (
        <div className={style}>
            <Line options={options} data={data} style={{ backgroundColor: "white" }} />
        </div>
    );
}

export default DailyActiveUserLine;

const style = css`
    
`;

