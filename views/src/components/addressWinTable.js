import React, { useEffect, useState } from "react";
import axios from 'axios';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { css } from '@emotion/css';

function AddressWinTable({ apiPath }) {
    const [addressArray, setAddressArray] = useState([{ address: '', TTAmount: '' }])

    useEffect(() => {
        axios.get(apiPath + "/mostWinAddress/10").then((res) => {
            const result = res["data"]["detail"]["addressWin"]
            const tempArray = []

            for (let i = 0; i < Object.keys(result).length; i++) {
                tempArray.push({ address: Object.keys(result)[i], TTAmount: result[Object.keys(result)[i]] })
            }

            setAddressArray(tempArray)
        }).catch(error => console.log(error))
    }, [])


    return (
        <TableContainer component={Paper} className={style}>
            <Table sx={{ minWidth: 650 }} stickyHeader aria-label="sticky table">
                <TableHead>
                    <TableRow>
                        <TableCell>Address</TableCell>
                        <TableCell align="right">TT Amount</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {addressArray.map((user) => (
                        <TableRow
                            key={user.address}
                            sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                        >
                            <TableCell component="th" scope="row">
                                {user.address}
                            </TableCell>
                            <TableCell align="right">{user.TTAmount}</TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
        </TableContainer>
    );
}

export default AddressWinTable;

const style = css`

    .MuiTableCell-root{
        color: black;
        background-color: white;
    }

`;
