import React from "react"

const InfoList = ({ infos, updateCallback }) => {
    const onDelete = async (id) => {
        try {
            const options = {
                method: "DELETE"
            }
            const response = await fetch(`http://127.0.0.1:5000/delete_info/${id}`, options)
            if (response.status === 200) {
                updateCallback()
            } else {
                console.error("Failed to delete")
            }
        } catch (error) {
            alert(error)
        }
    }

    return <div>
        <h2>Infos</h2>
        <table>
            <thead>
                <tr>
                    <th>name</th>
                    <th>adress</th>
                    <th>dob</th>
                    <th>cin</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                {infos.map((info) => (
                    <tr key={info.Id}>
                        <td>{info.Name}</td>
                        <td>{info.Adress}</td>
                        <td>{info.Dob}</td>
                        <td>{info.Cin}</td>
                        <td>
                           
                            <button onClick={() => onDelete(info.id)}>Delete</button>
                        </td>
                    </tr>
                ))}
            </tbody>
        </table>
    </div>
}

export default InfoList