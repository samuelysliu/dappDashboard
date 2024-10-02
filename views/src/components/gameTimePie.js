import React, { useEffect, useState } from "react";
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
import { Pie } from 'react-chartjs-2';
import axios from 'axios';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import { css } from '@emotion/css';

ChartJS.register(ArcElement, Tooltip, Legend);

function GameTimePie({ apiPath }) {
    const [playTimeData, setPlayTimeData] = useState([])
    const [type, setType] = useState("today")

    useEffect(() => {
        axios.get(apiPath + "/gameTime/" + type).then((res) => {
            setPlayTimeData([res["data"]["detail"]["coinTime"], res["data"]["detail"]["diceTime"], res["data"]["detail"]["lotteryTime"], res["data"]["detail"]["pirateTime"]])
        }).catch(error => console.log(error))
    }, [type])

    const data = {
        labels: ['Coin', 'Dice', 'Lottery', 'Pirate'],
        datasets: [
            {
                label: 'Play Time',
                data: playTimeData,
                backgroundColor: [
                    "#D27E14",
                    "#4EA8BE",
                    "#FF6343",
                    "#E5DCC5",
                ],
                borderColor: [
                    "#D27E14",
                    "#4EA8BE",
                    "#FF6343",
                    "#E5DCC5",
                ],
                borderWidth: 1,
            },
        ],
    };

    const options = {
        legend: {
            labels: {
                fontColor: "black"
            }
        }
    }
    return (
        <div className={style}>
            <Box sx={{ minWidth: 120 }}>
                <FormControl fullWidth>
                    <InputLabel id="demo-simple-select-label">Type</InputLabel>
                    <Select
                        labelId="demo-simple-select-label"
                        id="demo-simple-select"
                        value={type}
                        label="type"
                        onChange={(e) => setType(e.target.value)}
                    >
                        <MenuItem value="today">today</MenuItem>
                        <MenuItem value="yesterday">yesterday</MenuItem>
                        <MenuItem value="3 days">3 days</MenuItem>
                        <MenuItem value="week">week</MenuItem>
                        <MenuItem value="all">all</MenuItem>
                    </Select>
                </FormControl>
            </Box>
            <Pie data={data} options={options} style={{ backgroundColor: "white" }} />
        </div>
    );
}

export default GameTimePie;

const style = css`
    .MuiBox-root{
        background-color: white;
        margin: 10px;
    }

    .MuiFormLabel-root{
        color: #FF6343;
    }

    .MuiInputBase-root{
        height: 30px;
    }
`;



