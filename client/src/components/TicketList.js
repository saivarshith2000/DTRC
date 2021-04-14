import { React } from "react";
import TicketListItem from "./TicketListItem";

export default ({ tickets }) => {
    if (tickets.length === 0) {
        return null;
    }
    const renderedTickets = tickets.map((ticket) => (
        <TicketListItem ticket={ticket} key={ticket.name} />
    ));
    return (
        <div className="flex justify-center p-5 my-5">
            {" "}
            <div className="w-1/2">{renderedTickets}</div>
        </div>
    );
};
