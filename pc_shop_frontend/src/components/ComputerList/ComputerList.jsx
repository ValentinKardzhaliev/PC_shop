import { useContext, useEffect, useState } from 'react';
import './ComputerList.css'
import Computer from './Computer/Computer';
import LoadingContext from '../../contexts/LoadingContext';
import ComputerFilters from '../Filters/ComputerFilters/ComputerFilters';
import { getAllComputers } from '../../services/productService';

function ComputerList() {
    const [computers, setComputers] = useState([]);
    const { isLoading, startLoading, stopLoading } = useContext(LoadingContext);

    useEffect(() => {
        startLoading()
        getAllComputers()
            .then((computers) => {
                setComputers(computers);
                stopLoading();
            })
            .catch((err) => console.log(err));
    }, [])


    return (
        <>
            <ComputerFilters
                setComputers={setComputers}
                startLoading={startLoading}
                stopLoading={stopLoading}
            />

            <ul className="computer-list">
                {isLoading ? <h1>Loading...</h1> : computers.length === 0 && <h1>No computers found!</h1>}
                {computers.map(computer => <Computer key={computer._id} product={computer} />)}
            </ul>
        </>
    )
}

export default ComputerList;