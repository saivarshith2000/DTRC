// Central Search Bar component
import { React, useState } from "react";
import Message from "./Message";
import axios from "axios";

export default ({ setTickets }) => {
    const [from, setFrom] = useState("");
    const [to, setTo] = useState("");
    const [date, setDate] = useState("");
    const [error, setError] = useState("");

    const onSubmit = async (event) => {
        event.preventDefault();

        console.log("from: ", from);
        console.log("to: ", to);
        console.log("date: ", date);
        if (from === "" || to === "") {
            setError("FROM or TO is necessary");
            return;
        }
        try {
            const response = await axios.get("/trains/", {
                from,
                to,
                date,
            });
            setTickets(response.data);
        } catch (e) {
            setError("Network request failed !");
        }
    };

    const renderMessage = () => {
        if (error) {
            return <Message error={error} />;
        }
        return null;
    };

    return (
        <div className="mx-48 mt-20 text-center">
            {renderMessage()}
            <form onSubmit={onSubmit}>
                {/* header */}
                <div>
                    <p className="pb-10 text-6xl text-semibold">
                        Search for Tickets
                    </p>
                </div>
                <div className="flex justify-center align-center">
                    {/* From */}
                    <div className="ml-5">
                        <input
                            type="text"
                            placeholder="From"
                            className={InputStyle}
                            value={from}
                            onChange={(e) => setFrom(e.target.value)}
                        ></input>
                    </div>
                    {/* To */}
                    <div className="ml-5">
                        <input
                            type="text"
                            placeholder="To"
                            className={InputStyle}
                            value={to}
                            onChange={(e) => setTo(e.target.value)}
                        ></input>
                    </div>
                    <div className="ml-5">
                        {/* Date */}
                        <div>
                            <input
                                type="date"
                                placeholder="date"
                                className={InputStyle}
                                value={date}
                                onChange={(e) => setDate(e.target.value)}
                            ></input>
                        </div>
                    </div>
                </div>
                <button className="w-64 mx-auto mt-10">
                    <div>
                        {/* Search Button */}
                        <p className="p-5 text-lg font-semibold text-white bg-green-600 rounded-lg shadow-md hover:bg-green-800">
                            Search
                        </p>
                    </div>
                </button>
            </form>
        </div>
    );
};

// Tailwind styles
const InputStyle = "rounded-lg p-5 text-lg shadow-md border-0";
