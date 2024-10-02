import React, { useEffect, useState } from "react";
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Filler,
    Legend,
} from 'chart.js';
import { Line } from 'react-chartjs-2';
import axios from 'axios';

ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Filler,
    Legend
);

function NewAddressTrendLine({ apiPath }) {
    const [newAddressTrendData, setNewAddressTrendData] = useState([])
    const [labels, setLabels] = useState([])

    useEffect(() => {
        axios.get(apiPath + "/addressTrend").then((res) => {
            const tempArray = []
            const tempLabel = []

            const curDate = new Date()
            curDate.setDate(32)

            for (let i = 0; i < 32 - curDate.getDate(); i++) {
                tempArray.push(res["data"]["detail"]["addressArray"][i + 1])
                tempLabel.push(i + 1)
            }

            setNewAddressTrendData(tempArray)
            setLabels(tempLabel)
        }).catch(error => console.log(error))
    }, [])


    const options = {
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: 'monthly',
            },
        },
    };

    const data = {
        labels,
        datasets: [
            {
                fill: false,
                label: 'wallet address',
                data: newAddressTrendData,
                borderColor: '#4EA8BE',
                backgroundColor: '#4EA8BE',
            },
        ],
    };



    return (
        <Line options={options} data={data} style={{ backgroundColor: "white" }} />
    );
}

export default NewAddressTrendLine;

