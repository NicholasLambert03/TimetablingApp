import { useState, useEffect } from "react"

interface Data{
    field:string;
}

function Editor() {
    const [data, setData] = useState<Data>({
        field:'',
    })

    useEffect(() =>{
        fetch("/data")
            .then((res)=>{
                if (!res.ok){
                    throw new Error('Network response was not ok');
                }
                return res.json();
            })
            .then((data:Data) => {
                setData(data);
            })
            .catch((error) =>{
                console.error('there was a problem with the fetch opperation:',error);
            })
    },[])

    return(
       <h1>
        {data.field}
        </h1>
    )
}

export default Editor