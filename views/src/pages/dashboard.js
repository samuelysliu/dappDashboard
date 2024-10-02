import React from "react";
import { css, injectGlobal } from '@emotion/css';
import SideBar from "../components/sideBar";
import Grid from '@mui/material/Grid';
import GameTimePie from "../components/gameTimePie";
import MoneyPie from "../components/moneyPie";
import PlayTimeTrendLine from "../components/playTimeTrendLine";
import RevenueTimeTrendLine from "../components/revenueTrendLine";
import NewAddressTrendLine from "../components/newAddressTrendLine";
import AddressWinTable from "../components/addressWinTable";
import CountryTable from "../components/countryTable";
import NetIncomePerGameBar from "../components/netIncomePerGameBar";
import ContryPreferGameBar from "../components/contryPreferGameBar";

function Dashboard({ apiPath }) {


    return (
        <div className={style}>
            <SideBar />
            <Grid container spacing={2} className="container">
                <Grid item md={3} sm={6} xs={12} className="chart">
                    <font className="title">Play Time Per Game</font>
                    <GameTimePie apiPath={apiPath} />
                </Grid>
                <Grid item md={3} sm={6} xs={12} className="chart">
                    <font className="title">Money From Per Game</font>
                    <MoneyPie apiPath={apiPath} />
                </Grid>
                <Grid item md={3} sm={6} xs={12} className="chart">
                    <font className="title">各項目的淨收益</font>
                    <NetIncomePerGameBar apiPath={apiPath} />
                </Grid>
                <Grid item md={3} sm={6} xs={12}>
                    <font className="title">說明</font>
                    <br></br>
                    <p>Dividend的淨收益：用戶 (stake 數量 - unstake 數量) * 100 - claim 的 TT</p>
                    <p>Gold Dividend的淨收益：用戶 (stake 數量 - unstake 數量) / 366 * 200 - claim 的 TT</p>
                </Grid>

                <Grid item md={4} sm={6} xs={12} className="chart">
                    <font className="title">Trend of Play Time</font>
                    <PlayTimeTrendLine apiPath={apiPath} />
                </Grid>
                <Grid item md={4} sm={6} xs={12} className="chart">
                    <font className="title">Trend of Revenue</font>
                    <RevenueTimeTrendLine apiPath={apiPath} />
                </Grid>
                <Grid item md={4} sm={6} xs={12} className="chart">
                    <font className="title">Trend of New Address</font>
                    <NewAddressTrendLine apiPath={apiPath} />
                </Grid>

                <Grid item md={6} sm={6} xs={12} className="chart">
                    <font className="title">Top 10 Win TT Address</font>
                    <AddressWinTable apiPath={apiPath} />
                </Grid>
                <Grid item md={6} sm={6} xs={12} className="chart">
                    <font className="title">User From</font>
                    <CountryTable apiPath={apiPath} />
                </Grid>

                <Grid item md={6} sm={6} xs={12} className="chart">
                    <font className="title">Top3(人數) 國家遊玩次數</font>
                    <ContryPreferGameBar apiPath={apiPath} />
                </Grid>
            </Grid>
        </div >
    );
}

export default Dashboard;

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