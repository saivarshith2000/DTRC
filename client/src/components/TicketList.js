import { React, useState } from "react";
import TicketListItem from "./TicketListItem";
import Message from "./Message";

export default ({ tickets, logggedIn }) => {
    const [error, setError] = useState("");

    const renderMessage = () => {
        if (error) {
            return <Message msg={error} />;
        }
        return null;
    };

    const bookTicket = (id) => {
        if (logggedIn) {
            // if logged in redirect to booking page
        } else {
            // show error
            setError("You need to login to book tickets!!!");
            return;
        }
    };

    if (tickets.length === 0) {
        return null;
    }
    const renderedTickets = tickets.map((ticket) => (
        <TicketListItem
            ticket={ticket}
            key={ticket.id}
            bookTicket={bookTicket}
        />
    ));
    return (
        <div className="flex justify-center p-5 my-5">
            {renderMessage()}
            <div className="w-1/2">{renderedTickets}</div>
        </div>
    );
};
