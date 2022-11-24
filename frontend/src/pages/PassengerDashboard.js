import {useEffect, useState} from "react";

function PassengerDashboard() {
    const [data, setData] = useState([]);
    let INVENTORY_API_URL;
    // GET request function to your Mock API
    const fetchInventory = () => {

        fetch(`${INVENTORY_API_URL}`)
            .then(res => res.json())
            .then(json => setData(json));
    }

    // Calling the function on component mount
    useEffect(() => {
        fetchInventory();
    }, []);


    return (
        <div className="container">
            <h1>Simple Inventory Table</h1>
            <table>
                <thead>
                <tr>
                    <th>Product Name</th>
                    <th>Product Category</th>
                    <th>Unit Price</th>
                    <th>Action</th>
                </tr>
                </thead>
                <tbody>
                {
                    data.map((flight)=> (
                        {
if(flight.type_of == "arrival"){

                    <tr key={flight.id}>
                    <td>{flight.product_name}</td>
                    <td>{flight.product_category}</td>
                    <td>{flight.unit_price}</td>
                    <td/>
                    </tr>
                } }
                        ))
                }
                </tbody>
            </table>
        </div>
    );
}


// let PassengerDashboard;
export default PassengerDashboard;