import { useNavigate } from "react-router-dom"
function Homepage() {
    const navigate = useNavigate()
    const editlink = () =>{navigate('/edit')}

    return (
        <div>
        <h1> Timetabler </h1>
        <button
        onClick = {editlink}
        >
        Edit Database  
        </button>
        
        <button
        onClick = {onClick}
        >
        Make Timetable
        </button>
        </div>
    )

    function onClick() {

    }

}

export default Homepage
