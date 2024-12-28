import { useState, useEffect } from "react"
const apiUrl = import.meta.env.VITE_API_URL

interface Data{
    tables:[];
}

function Editor() {
    const [data, setData] = useState<Data>({
        tables:[],
    })

    useEffect(() =>{
        fetch(`${apiUrl}/data`)
            .then((res)=>{return res.json();})
            .then((data:Data) => {setData(data);})
    },[])

    return(
        
       <h2>
        {data.tables}
        </h2>
    )
}

export default Editor