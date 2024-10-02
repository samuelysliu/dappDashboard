export class systemConfig{
    constructor(){
        if(process.env.REACT_APP_Environment === "test"){
            this.apiPath = "https://dapp-sales-dashboard-test.herokuapp.com/api/v1"
        }else if(process.env.REACT_APP_Environment === "main"){
            this.apiPath = "https://dapp-sales-dashboard.herokuapp.com/api/v1"
        }else{
            this.apiPath = "http://127.0.0.1:5000/api/v1"
        }
    }

    getApiPath(){
        return this.apiPath
    }
}