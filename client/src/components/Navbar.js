// Navbar component
import React from "react";
import { Link } from "react-router-dom";
import { useHistory } from "react-router";

export default ({ userState, setUserState }) => {
    let history = useHistory();
    const logout = () => {
        // clear userstate and redirect to home page
        setUserState({ loggedIn: false, username: null, email: null });
        history.push("/");
    };

    if (userState.loggedIn) {
        return (
            <div className="flex items-center justify-between w-screen p-5 shadow-lg px-96">
                {/* Brand logo */}
                <div id="Brand" className="p-2 bg-green-600 rounded">
                    <a href="/" className="text-4xl font-bold text-white">
                        BookIt
                    </a>
                </div>
                {/* Navigation Menu */}
                <div id="Navigation" className="flex ml-8 align-center">
                    <button className="mr-5 text-xl" onClick={(e) => logout()}>
                        Logout
                    </button>
                    <p className="mr-5 text-xl">Welcome, {userState.email}</p>
                </div>
            </div>
        );
    }
    return (
        <div className="flex items-center justify-between w-screen p-5 shadow-lg px-96">
            {/* Brand logo */}
            <div id="Brand" className="p-2 bg-green-600 rounded">
                <a href="/" className="text-4xl font-bold text-white">
                    BookIt
                </a>
            </div>
            {/* Navigation Menu */}
            <div id="Navigation" className="flex ml-8 align-center">
                <Link to="/login" className="mr-5 text-xl">
                    Login
                </Link>
                <Link to="/register" className="mr-5 text-xl">
                    Register
                </Link>
            </div>
        </div>
    );
};
