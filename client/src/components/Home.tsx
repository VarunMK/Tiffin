import React, { useState } from 'react';
import { createReadStream } from 'fs';
import {
    Box,
    Button,
    Flex,
    Heading,
    Input,
    Text,
    useQuery,
    useToast,
} from '@chakra-ui/react';
import axios from 'axios';

const Home = () => {
    //use state for file data
    const [fileData, setFileData] = useState<File>();
    const toast = useToast();
    const props = {
        name: 'requirements',
        action: '',
    };

    const createContainer = async (fileData:File) => {
        const formData= new FormData();
        formData.append('file',fileData,fileData.name)

        try {
            const {data}=await axios.post('http://localhost:5000/createContainer',formData);
            console.log(data)
            // const data = await fetch('http://localhost:5000/createContainer', {
            //     method: 'POST',
            //     headers:{'Content-Type':'multipart/form-data'},
            //     body: formData,
            // });
            // const jsonData = await data.json();
            // console.log(jsonData);
        } catch (err) {
            console.log(err);
        }
    };

    const startContainer = async () => {
        try {
            const data = await fetch('http://localhost:5000/startContainer', {
                method: 'POST',
                headers: { 'Content-Type': 'application/JSON' },
                body: JSON.stringify({ name: 'hi' }),
            });
            const jsonData = await data.json();
            console.log(jsonData);
        } catch (err) {
            console.log(err);
        }
    };
    console.log(fileData);
    return (
        <Box width="50%" margin="0 auto">
            <Box backgroundColor="gray.100" py="3" textAlign="center">
                <Heading>Tiffin</Heading>
            </Box>
            <Text>File Upload:</Text>
            <Flex direction="column">
                <Input
                    type="file"
                    width="50%"
                    onChange={(e: any) => {
                        setFileData(e.target.files[0])
                    }}
                />
                <Button
                    mt="2"
                    onClick={()=>{
                        if(fileData!=undefined){
                            createContainer(fileData)}}
                        }
                >
                    Build Container
                </Button>
                <Button mt="2">Start Container</Button>
                <Button mt="2">Stop Container</Button>
            </Flex>
        </Box>
    );
};

export default Home;
