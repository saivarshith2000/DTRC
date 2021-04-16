import { React, useState } from "react";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Register from "./pages/Register";

export default () => {
    const [userState, setUserState] = useState({
        loggedIn: false,
        username: null,
        email: null,
    });
    return (
        <Router>
            <div>
                <Navbar userState={userState} setUserState={setUserState} />
                <Switch>
                    <Route path="/login">
                        <Login
                            userState={userState}
                            setUserState={setUserState}
                        />
                    </Route>
                    <Route path="/register">
                        <Register />
                    </Route>
                    <Route path="/">
                        <Home userState={userState} />
                    </Route>
                </Switch>
            </div>
        </Router>
    );
};
