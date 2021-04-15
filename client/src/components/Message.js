// Error banner component
import React from "react";

export default ({ msg, isError = true }) => {
    if (!isError) {
        return (
            <div className="p-2 m-2 bg-green-700 rounded align-center shadown-lg">
                <p className="text-white text-md text-semibold">{msg}</p>
            </div>
        );
    }
    return (
        <div className="p-2 m-2 bg-red-700 rounded align-center shadown-lg">
            <p className="text-white text-md text-semibold">{msg}</p>
        </div>
    );
};
