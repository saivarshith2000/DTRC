// Navbar component
import React from "react";
import { Link } from "react-router-dom";

export default () => {
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
                <Link to="/about" className="mr-5 text-xl">
                    About
                </Link>
            </div>
        </div>
    );
};
