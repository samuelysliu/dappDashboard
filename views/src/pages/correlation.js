import React from "react";
import { css, injectGlobal } from '@emotion/css';
import SideBar from "../components/sideBar";
import Grid from '@mui/material/Grid';
import GameCorrelationCard from "../components/gameCorrelationCard";
import GameAndDividendScatter from "../components/gameAndDividendScatter";
import GameAndGoldScatter from "../components/gameAndGoldScatter";


function Correlation({ apiPath }) {

    return (
        <div className={style}>
            <SideBar />
            <Grid container spacing={10} className="container">
                <Grid item md={12} sm={12} xs={12} className="chart">
                    <GameCorrelationCard apiPath={apiPath} />
                </Grid>

                <Grid item md={6} sm={6} xs={12} className="chart">
                    <font className="title">透過遊戲獲得Prize跟Dividend的關係</font>
                    <GameAndDividendScatter apiPath={apiPath} />
                </Grid>

                <Grid item md={6} sm={6} xs={12} className="chart">
                    <font className="title">透過遊戲獲得Prize跟Gold Dividend的關係</font>
                    <GameAndGoldScatter apiPath={apiPath} />
                </Grid>
            </Grid>
        </div >
    );
}

export default Correlation;

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