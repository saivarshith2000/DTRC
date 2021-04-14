import { React, useState } from "react";
import InputField from "../components/InputField";
import Error from "../components/Error";

export default () => {
    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPwd, setConfirmPwd] = useState("");
    const [error, setError] = useState("");

    const onSubmit = (e) => {
        e.preventDefault();
        // validate form
        if (
            name === "" ||
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
        console.log(name);
        console.log(email);
        console.log(password);
        console.log(confirmPwd);
        console.log("test");
    };

    // renders form errors
    const renderError = () => {
        if (error) {
            return <Error error={error} />;
        }
        return null;
    };

    return (
        <div className="flex-col w-1/3 mx-auto mt-10">
            {renderError()}
            <p className="px-2 mx-auto mb-4 text-4xl font-semibold">Register</p>
            <form onSubmit={onSubmit}>
                <InputField
                    name="name"
                    isPassword={false}
                    fieldInfo="Enter your name"
                    field={name}
                    setField={setName}
                />
                <InputField
                    name="email"
                    isPassword={false}
                    fieldInfo="Enter your email"
                    field={email}
                    setField={setEmail}
                />
                <InputField
                    name="password"
                    isPassword={true}
                    fieldInfo="Enter your password"
                    field={password}
                    setField={setPassword}
                />
                <InputField
                    name="confirm password"
                    isPassword={true}
                    fieldInfo="Confirm your password"
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
