import { React, useState } from "react";
import InputField from "../components/InputField";
import Message from "../components/Message";
import axios from "axios";
import { useHistory } from "react-router";

export default () => {
    let history = useHistory();
    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPwd, setConfirmPwd] = useState("");
    const [error, setError] = useState("");

    const onSubmit = (e) => {
        e.preventDefault();
        // validate form
        if (
            username === "" ||
            email === "" ||
            password === "" ||
            confirmPwd === ""
        ) {
            setError("All fields are mandatory for registration !");
            return;
        } else if (confirmPwd != password) {
            setError("Passwords do not match !");
            return;
        }
        setError("");

        // send register post request
        const params = new URLSearchParams();
        params.append("username", username);
        params.append("email", email);
        params.append("password", password);
        axios
            .post("/register", params)
            .then(function (response) {
                // if status
                if (response.data.error === undefined) {
                    history.push("/login");
                } else {
                    // render any form errors otherwise
                    setError(response.data.error);
                }
            })
            .catch(function (error) {
                // indicates connection with server.
                setError(
                    "We are experiencing issues contacting the server. Please try again later"
                );
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
            <p className="px-2 mx-auto mb-4 text-4xl font-semibold">Register</p>
            <form onSubmit={onSubmit}>
                <InputField
                    name="username"
                    isPassword={false}
                    fieldInfo="Username"
                    field={username}
                    setField={setUsername}
                />
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
                <InputField
                    name="confirm password"
                    isPassword={true}
                    fieldInfo="Confirm Password"
                    field={confirmPwd}
                    setField={setConfirmPwd}
                />
                <button className="mx-2 mt-4 w-36">
                    <div>
                        {/* Register Button */}
                        <p className="p-5 text-lg font-semibold text-white bg-green-600 rounded-lg shadow-md hover:bg-green-800">
                            Register
                        </p>
                    </div>
                </button>
            </form>
        </div>
    );
};
