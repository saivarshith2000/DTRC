import { React, useState } from "react";
import SearchBar from "../components/SearchBar";
import TicketList from "../components/TicketList";

export default ({ userState }) => {
    const [tickets, setTickets] = useState([]);

    return (
        <div>
            <SearchBar setTickets={setTickets} />
            <TicketList tickets={tickets} loggedIn={userState.loggedIn} />
        </div>
    );
};
