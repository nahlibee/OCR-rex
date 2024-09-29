import { useState } from "react";

const InfoForm = ({ existingInfo = {}, updateCallback }) => {
    const [name, setName] = useState(existingInfo.name || "");
    const [adress, setAdress] = useState(existingInfo.adress || "");
    const [dob, setDob] = useState(existingInfo.dob || "");
    const [x, setX] = useState(existingInfo.x || "");


    const updating = Object.entries(existingInfo).length !== 0

    const onSubmit = async (e) => {
        e.preventDefault()

        const data = {
            name,
            adress,
            dob,
            x
        }
        const url = "http://127.0.0.1:5000/" + (updating ? `update_Info/${existingInfo.id}` : "create_Info")
        const options = {
            method: updating ? "PATCH" : "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
        const response = await fetch(url, options)
        if (response.status !== 201 && response.status !== 200) {
            const data = await response.json()
            alert(data.message)
        } else {
            updateCallback()
        }
    }

    return (
        <form onSubmit={onSubmit}>
            <div>
                <label htmlFor="name">name:</label>
                <input
                    type="text"
                    id="name"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="adress">adress:</label>
                <input
                    type="text"
                    id="adress"
                    value={adress}
                    onChange={(e) => setAdress(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="dob">dob:</label>
                <input
                    type="text"
                    id="dob"
                    value={dob}
                    onChange={(e) => setDob(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="x">x:</label>
                <input
                    type="text"
                    id="x"
                    value={x}
                    onChange={(e) => setX(e.target.value)}
                />
            </div>
            <button type="submit">{updating ? "Update" : "Create"}</button>
        </form>
    );
};

export default InfoForm