import React, { useEffect, useState } from "react";
import axios from 'axios';
import { css } from '@emotion/css';
import { DataGrid } from '@mui/x-data-grid';

function CountryTable({ apiPath }) {
    const columns = [
        { field: 'country', headerName: 'country', width: 500 },
        { field: 'userNumber', headerName: 'number', width: 100 },
    ];

    const [rows, setRows] = useState([])

    useEffect(() => {
        axios.get(apiPath + "/userCameFrom").then((res) => {
            let data = res["data"]["detail"]["userCameFrom"]
            let tempRow = []
            for (let i = 0; i < data.length; i++) {
                tempRow.push(
                    { id: i, country: data[i][0], userNumber: data[i][1] }
                )
            }
            setRows(tempRow)
        }).catch(error => console.log(error))
    }, [apiPath])


    return (
        <div className={style} style={{ height: "400px", width: '100%' }}>
            <DataGrid
                rows={rows}
                columns={columns}
                pageSize={5}
                rowsPerPageOptions={[5]}
            />
        </div>
    );
}

export default CountryTable;

const style = css`

`;



