// Error banner component
import React from "react";

export default ({ error }) => {
    return (
        <div className="p-2 m-2 bg-red-700 rounded align-center shadown-lg">
            <p className="text-white text-md text-semibold">{error}</p>
        </div>
    );
};
