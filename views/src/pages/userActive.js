import React from "react";
import { css, injectGlobal } from '@emotion/css';
import SideBar from "../components/sideBar";
import Grid from '@mui/material/Grid';
import MonthlyActiveCard from "../components/monthlyActiveCard";
import DailyActiveUserLine from "../components/dailyActiveUserLine";


function UserActive({ apiPath }) {

    return (
        <div className={style}>
            <SideBar />
            <Grid container spacing={2} className="container">
                <Grid item md={12} sm={12} xs={12} className="chart">
                    <MonthlyActiveCard apiPath={apiPath} />
                </Grid>

                <Grid item md={12} sm={12} xs={12} className="chart">
                    <font className="title">每日用戶活躍度</font>
                    <DailyActiveUserLine apiPath={apiPath} />
                </Grid>
            </Grid>
        </div >
    );
}

export default UserActive;

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