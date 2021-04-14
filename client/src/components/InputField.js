// Render an input field in forms

import { React } from "react";

export default ({
    field,
    setField,
    fieldName,
    isPassword = false,
    fieldInfo,
}) => {
    return (
        <div className="flex items-center justify-between px-2 py-4">
            <p className="px-2 text-gray-800">{fieldInfo}</p>
            <input
                className="w-2/3 px-2 py-3 border-0 rounded-md shadow-md text-md"
                type={isPassword ? "password" : "text"}
                name={fieldName}
                onChange={(e) => setField(e.target.value)}
                value={field}
                placeholder={fieldInfo}
            ></input>
        </div>
    );
};
