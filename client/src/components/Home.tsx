import React, { useRef, useState } from 'react'
import { Box, Button,Input,Text,useQuery,useToast } from '@chakra-ui/react'



const Home=()=>{
    const [s,setS]=useState<string>('Hi');
    const toast=useToast();
    const startContainer=async (s:string)=>{
        try{
            const data=await fetch('http://localhost:5000/startContainer',{
                method:'POST',
                headers:{'Content-Type':'application/JSON'},
                body:JSON.stringify({'name':s})
            });
            const jsonData=await data.json();
            console.log(jsonData);
        }
        catch(err){
            console.log(err)
        }
    }
    return(
        <Box>
            <Text>File Upload:</Text>
            {/* <Input onChange={(e:any)=>{setS(e)}}>Text</Input> */}
            <Button onClick={()=>{startContainer(s)}}>Build Container</Button>
            <Button>Start Container</Button>
            <Button>Stop Container</Button>            
        </Box>
    );
}

export default Home;