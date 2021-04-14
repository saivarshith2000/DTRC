// TicketListItem Component
import React from "react";

export default ({ ticket }) => {
    return (
        <div className="flex items-center justify-between p-4 px-8 mb-5 rounded-md shadow-md">
            <p className>{ticket.NAME}</p>
            <p className>{ticket.FROM}</p>
            <p className>{ticket.TO}</p>
            <p className>{ticket.DATE}</p>
            <button className="p-2 ml-5 text-sm font-semibold text-white bg-green-600 rounded-md shadow-md hover:bg-green-800">
                Book Now
            </button>
        </div>
    );
};
