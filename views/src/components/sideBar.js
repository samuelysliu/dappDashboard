import React, { useState } from "react";
import Box from '@mui/material/Box';
import Drawer from '@mui/material/Drawer';
import Button from '@mui/material/Button';
import List from '@mui/material/List';
import Divider from '@mui/material/Divider';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import MailIcon from '@mui/icons-material/Mail';
import MenuIcon from '@mui/icons-material/Menu';
import RowingIcon from '@mui/icons-material/Rowing';
import ScatterPlotIcon from '@mui/icons-material/ScatterPlot';
import SportsEsportsIcon from '@mui/icons-material/SportsEsports';
import { useNavigate } from "react-router-dom";

function SideBar() {
    const navigate = useNavigate();
    const [isOpen, setIsOpen] = useState(false);

    const toggleDrawer = (open) => (event) => {
        if (event.type === 'keydown' && (event.key === 'Tab' || event.key === 'Shift')) {
            return;
        }

        setIsOpen(open)
    };
    return (
        <React.Fragment key={"left"}>
            <Button onClick={toggleDrawer(true)}><MenuIcon style={{ color: "#049EB8" }} /></Button>
            <Drawer
                anchor={"left"}
                open={isOpen}
                onClose={toggleDrawer(false)}
                PaperProps={{
                    sx: {
                        backgroundColor: "#171F34",
                        color: "white"
                    }
                }}
            >

                <Box
                    sx={{ width: 250 }}
                    role="presentation"
                    onClick={toggleDrawer(false)}
                    onKeyDown={toggleDrawer(false)}
                >
                    <div style={{ padding: "10px" }}>
                        <font className="test">Dapp Dashboard</font>
                    </div>
                    <Divider style={{ backgroundColor: "#049EB8" }} />
                    <List>
                        <ListItem disablePadding>
                            <ListItemButton onClick={() => navigate("/")}>
                                <ListItemIcon>
                                    <MailIcon style={{ color: "white" }} />
                                </ListItemIcon>
                                <ListItemText primary="Dashboard" />
                            </ListItemButton>
                        </ListItem>

                        <ListItem disablePadding>
                            <ListItemButton onClick={() => navigate("/userActive")}>
                                <ListItemIcon>
                                    <RowingIcon style={{ color: "white" }} />
                                </ListItemIcon>
                                <ListItemText primary="User Active" />
                            </ListItemButton>
                        </ListItem>

                        <ListItem disablePadding>
                            <ListItemButton onClick={() => navigate("/betTime")}>
                                <ListItemIcon>
                                    <SportsEsportsIcon style={{ color: "white" }} />
                                </ListItemIcon>
                                <ListItemText primary="Bet Time" />
                            </ListItemButton>
                        </ListItem>

                        <ListItem disablePadding>
                            <ListItemButton onClick={() => navigate("/correlation")}>
                                <ListItemIcon>
                                    <ScatterPlotIcon style={{ color: "white" }} />
                                </ListItemIcon>
                                <ListItemText primary="Correlation" />
                            </ListItemButton>
                        </ListItem>
                    </List>
                </Box>
            </Drawer>
        </React.Fragment>
    );
}

export default SideBar;

