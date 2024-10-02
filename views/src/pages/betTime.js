import React, { useEffect, useState } from "react";
import { css, injectGlobal } from '@emotion/css';
import SideBar from "../components/sideBar";
import Grid from '@mui/material/Grid';
import GameTimePie from "../components/gameTimePie";
import MonthlyActiveCard from "../components/monthlyActiveCard";
import DailyActiveUserLine from "../components/dailyActiveUserLine";
import BetTimeBar from "../components/betTimeBar";


function BetTime({ apiPath }) {

    return (
        <div className={style}>
            <SideBar />
            <Grid container spacing={2} className="container">
                <Grid item md={4} sm={4} xs={12} className="chart">
                    <font className="title">coin 下注金額次數</font>
                    <BetTimeBar apiPath={apiPath} item={"coin"} />
                </Grid>
                <Grid item md={4} sm={4} xs={12} className="chart">
                    <font className="title">dice 下注金額次數</font>
                    <BetTimeBar apiPath={apiPath} item={"dice"} />
                </Grid>
                <Grid item md={4} sm={4} xs={12} className="chart">
                    <font className="title">lottery 下注金額次數</font>
                    <BetTimeBar apiPath={apiPath} item={"lottery"} />
                </Grid>
                <Grid item md={6} sm={6} xs={12} className="chart">
                    <font className="title">pirate 創建寶箱金額次數</font>
                    <BetTimeBar apiPath={apiPath} item={"pirate create"} />
                </Grid>
                <Grid item md={6} sm={6} xs={12} className="chart">
                    <font className="title">pirate 搶寶箱金額次數</font>
                    <BetTimeBar apiPath={apiPath} item={"pirate rob"} />
                </Grid>
            </Grid>
        </div >
    );
}

export default BetTime;

const style = css`
    .container{
        padding-left: 20px;
        padding-right: 20px;
    }

    .chart{
        text-align: center;
    }

    
    .title{
        color: #4B4B4B;
        font-size: 20px;
        font-weight: 800;
    }

`

injectGlobal`
    body{
        background-color: #EEF3FD;
    }
`