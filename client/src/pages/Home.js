import { React, useState } from "react";
import SearchBar from "../components/SearchBar";
import TicketList from "../components/TicketList";

export default () => {
    const [tickets, setTickets] = useState([]);

    return (
        <div>
            <SearchBar setTickets={setTickets} />
            <TicketList tickets={tickets} />
        </div>
    );
};
