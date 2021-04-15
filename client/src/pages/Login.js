import { React, useState } from "react";
import InputField from "../components/InputField";
import Message from "../components/Message";
import axios from "axios";
import { useHistory } from "react-router";

export default () => {
    let history = useHistory();
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");

    const onSubmit = (e) => {
        e.preventDefault();
        // validate form
        if (email === "" || password === "") {
            setError("Email/Password cannot be empty!");
            return;
        }
        setError("");

        // send login post request
        const params = new URLSearchParams();
        params.append("email", email);
        params.append("password", password);
        axios
            .post("/login", params)
            .then(function (response) {
                // if there is no error, redirect to home
                if (response.data.error === undefined) {
                    history.push("/");
                } else {
                    // render any form errors otherwise
                    setError(response.data.error);
                }
            })
            .catch(function (error) {
                console.log(error);
            });
    };

    // renders form errors
    const renderMessage = () => {
        if (error) {
            return <Message msg={error} />;
        }
        return null;
    };
    return (
        <div className="flex-col w-1/3 mx-auto mt-10">
            {renderMessage()}
            <p className="px-2 mx-auto mb-4 text-4xl font-semibold">Login</p>
            <form onSubmit={onSubmit}>
                <InputField
                    name="email"
                    isPassword={false}
                    fieldInfo="Email"
                    field={email}
                    setField={setEmail}
                />
                <InputField
                    name="password"
                    isPassword={true}
                    fieldInfo="Password"
                    field={password}
                    setField={setPassword}
                />
                <button className="mx-2 mt-4 w-36">
                    <div>
                        {/* Login Button */}
                        <p className="p-5 text-lg font-semibold text-white bg-green-600 rounded-lg shadow-md hover:bg-green-800">
                            Login
                        </p>
                    </div>
                </button>
            </form>
        </div>
    );
};
