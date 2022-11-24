import { Route, Routes } from "react-router-dom";
import React from 'react';
import NavBar from "./components/NavBar";
import Footer from "./components/Footer";
import Home from "./pages/Home";
import About from "./pages/About";
import Login from "./pages/Login";
import Signup from "./pages/Signup";
import FlightInfo from "./pages/Flight";
import Gate from "./pages/Gate";
import Baggage from "./pages/Baggage";
import FlightSchedule from "./pages/Schedule";
//import Cart from "./pages/Cart";
import AirportDashboard from "./pages/AirportDashboard";
import AirlineDashboard from "./pages/AirlineDashboard";
import PassengerDashboard from "./pages/PassengerDashboard";

// material UI
import Grid from "@mui/material/Grid";

// material UI theming
import { ThemeProvider, createTheme } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";

// Date picker
import { AdapterDateFns } from "@mui/x-date-pickers/AdapterDateFns";
import { LocalizationProvider } from "@mui/x-date-pickers/LocalizationProvider";

const theme = createTheme({
  palette: {
    primary: {
      main: "#30658a",
      contrastText: "#ffffff",
    },
    secondary: {
      main: "#06395e",
      contrastText: "#ffffff",
    },
    background: {
      default: "#06395e",
      paper: "#06395e",
    },
    text: {
      primary: "#ffffff",
    },
    divider: "rgba(255,255,255,0.7)",
    error: {
      main: "#ffffff",
    },
  },
  typography: {
    fontFamily: ["Rale way", "Roboto"].join(","),
    h1: {
      fontSize: 60,
    },
    h2: {
      fontSize: 25,
      fontWeight: "bold",
    },
    h3: {
      fontSize: 25,
      fontWeight: "bold",
    },
  },
});

function App() {
  return (
      <LocalizationProvider dateAdapter={AdapterDateFns}>
        <ThemeProvider theme={theme}>
          <CssBaseline />
          <Grid
              container
              height="100vh"
              width="100%"
              direction="column"
              align="center"
              justifyContent="space-between"
              wrap="nowrap"
              overflow="auto"
          >
            <Grid item container>
              <NavBar />
            </Grid>

            <Grid
                item
                container
                justifyContent="center"
                alignItems="center"
                mt="100px"
            >
              <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/flight-details/:id" element={<FlightInfo />} />

                <Route path="/gate" element={<Gate />} />
                <Route path="/reservation/:company/:hotel" element={<Baggage />} />
                <Route path="/schedule" element={<FlightSchedule/>} />
                <Route path="/about" element={<About />} />
                <Route path="/login" element={<Login />} />
                <Route path="/signup" element={<Signup />} />
                <Route path="/airline-dashboard/*" element={<AirlineDashboard />}/>
                <Route path="/airport-dashboard/*" element={<AirportDashboard />}/>
                <Route path="/passenger-dashboard/*" element={<PassengerDashboard />}/>
              </Routes>
            </Grid>

            <Grid item container mt="50px">
              <Footer />
            </Grid>
          </Grid>
        </ThemeProvider>
      </LocalizationProvider>
  );
}

export default App;
