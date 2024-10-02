import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { systemConfig } from "./conf/config";
import Dashboard from './pages/dashboard';
import UserActive from './pages/userActive';
import BetTime from './pages/betTime';
import Correlation from './pages/correlation';

function App() {
  const systemObject = new systemConfig();
  const apiPath = systemObject.getApiPath();
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Dashboard apiPath={apiPath} />}></Route>
        <Route path="/userActive" element={<UserActive apiPath={apiPath} />}></Route>
        <Route path="/betTime" element={<BetTime apiPath={apiPath} />}></Route>
        <Route path="/correlation" element={<Correlation apiPath={apiPath} />}></Route>
      </Routes>
    </Router>
  );
}

export default App;
