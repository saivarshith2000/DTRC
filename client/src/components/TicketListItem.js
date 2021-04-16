// TicketListItem Component
import React from "react";

export default ({ ticket, bookTicket }) => {
    return (
        <div className="flex items-center justify-between p-4 px-8 mb-5 rounded-md shadow-md">
            <p className>{ticket.train}</p>
            <p className>{ticket._from}</p>
            <p className>{ticket._to}</p>
            <p className>{ticket.date}</p>
            <p className>{ticket.id}</p>
            <button
                className="p-2 ml-5 text-sm font-semibold text-white bg-green-600 rounded-md shadow-md hover:bg-green-800"
                onClick={(e) => bookTicket(ticket.id)}
            >
                Book Now
            </button>
        </div>
    );
};
