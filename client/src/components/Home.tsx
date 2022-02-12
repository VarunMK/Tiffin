import React, { useState } from 'react';
import { createReadStream } from 'fs';
import {
    Box,
    Button,
    Flex,
    Heading,
    Input,
    Select,
    Tab,
    TabList,
    TabPanel,
    TabPanels,
    Tabs,
    Text,
    createStandaloneToast,
    Link,
} from '@chakra-ui/react';
import axios from 'axios';

const versionList = [
    'Python 2.7',
    'Python 3.6',
    'Python 3.7',
    'Python 3.8',
    'Python 3.9',
];

const Home = () => {
    const [version, setVersion] = useState<string>('Python 3.6');
    const [contList, setContList] = useState<Array<string>>([]);
    const [contName, setContName] = useState<string>('');
    const [isLoading,setisLoading]=useState<boolean>(false);
    const [fileData, setFileData] = useState<File>();
    const [accessCodeServer, setAccessCodeServer] = useState<boolean>(false);
    const [show, setShow] = useState<boolean>(false);
    const toast = createStandaloneToast();
    const createContainer = async (
        fileData: File,
        version: string,
        contName: string
    ) => {
        const formData = new FormData();
        formData.append('file', fileData, fileData.name);

        try {
            const { data } = await axios.post(
                'http://localhost:5000/createContainer?pyversion=' +
                    version +
                    '&contName=' +
                    contName,
                formData
            );
            if (data === 'success') {
                setAccessCodeServer(true);
                setisLoading(false);
                toast({
                    title: 'Container Created Successfully',
                    description:
                        'Visit http://localhost:3001/ to check the codebase',
                    status: 'success',
                    duration: 6000,
                    isClosable: true,
                });
            }
        } catch (err) {
            console.log(err);
        }
    };
    console.log(version);
    return (
        <Box margin="0 auto">
            <Box backgroundColor="black" py="3" textAlign="center">
                <Heading color="white">Tiffin</Heading>
            </Box>
            <Box
                width="50%"
                borderRadius="20"
                margin="0 auto"
                mt="100"
                border="1px solid rgba(0, 0, 0, 0.05);"
                boxShadow="-2px -2px 8px rgba(0, 0, 0, 0.02), 6px 6px 12px rgba(0, 0, 0, 0.08);"
                p="45"
                backgroundColor="#FAFAFA"
                color="black"
            >
                <Tabs>
                    <TabList>
                        <Tab>
                            <Heading
                                fontSize="2xl"
                                fontWeight={show ? 'extrabold' : 'light'}
                                justifyContent="center"
                                flexDirection="column"
                                onClick={() => {
                                    setShow(true);
                                }}
                                _hover={{ cursor: 'pointer' }}
                                marginRight="5"
                            >
                                Create Container
                            </Heading>
                        </Tab>
                        <Tab>
                            <Heading
                                fontSize="2xl"
                                justifyContent="center"
                                flexDirection="column"
                                fontWeight={show ? 'light' : 'extrabold'}
                                onClick={() => {
                                    setShow(false);
                                }}
                                _hover={{ cursor: 'pointer' }}
                            >
                                Select Container
                            </Heading>
                        </Tab>
                    </TabList>
                    <TabPanels>
                        <TabPanel>
                            <Flex direction="column">
                                <Text mt="5">Set Container Name:</Text>
                                <Input
                                    mt="3"
                                    _focus={{
                                        border: '#008080 solid 2px',
                                    }}
                                    onChange={(e) => {
                                        setContName(e.target.value);
                                    }}
                                />
                                <Text mt="5">
                                    Set Python Version (Default Version is:
                                    Python 3.6):
                                </Text>
                                <Select
                                    mt="5"
                                    w="30%"
                                    borderColor="#ced4da"
                                    background="#FAFAFA"
                                    boxShadow="inset -3px -3px 2px #FFFFFF, inset 2px 2px 8px rgba(0, 0, 0, 0.08);"
                                    borderRadius="md"
                                    onChange={(e) => {
                                        setVersion(e.target.value);
                                    }}
                                    _focus={{
                                        border: '#008080 solid 2px',
                                    }}
                                >
                                    <option
                                        style={{
                                            display: 'none',
                                        }}
                                    >
                                        Choose Python Version
                                    </option>
                                    {versionList.map((value) => {
                                        return (
                                            <option key={value} value={value}>
                                                {value}
                                            </option>
                                        );
                                    })}
                                </Select>
                                <Text mt="5">
                                    Upload your requirements file(.txt):
                                </Text>
                                <Input
                                    mt="5"
                                    mb="5"
                                    type="file"
                                    width="30%"
                                    onChange={(e: any) => {
                                        setFileData(e.target.files[0]);
                                    }}
                                />
                                {!accessCodeServer ? (
                                    <Button
                                        mt="2"
                                        _active={{
                                            bg: '#008080',
                                            color: 'white',
                                        }}
                                        isLoading={isLoading}
                                        onClick={() => {
                                            if (fileData != undefined) {
                                                setisLoading(true);
                                                createContainer(
                                                    fileData,
                                                    version,
                                                    contName
                                                );
                                            }
                                        }}
                                        size="lg"
                                    >
                                        Create Container
                                    </Button>
                                ) : (
                                    <a href="http://localhost:3001" target="_blank" >
                                        <Button
                                            mt="2"
                                            width="100%"
                                            _active={{
                                                bg: '#008080',
                                                color: 'white',
                                            }}
                                            size="lg"
                                        >
                                            Open Code
                                        </Button>
                                    </a>
                                )}
                            </Flex>
                        </TabPanel>
                        <TabPanel>
                            <Flex direction="column">
                                <Text mt="5">Run An Existing Environment:</Text>
                                <Select
                                    mt="5"
                                    w="90%"
                                    borderColor="#ced4da"
                                    background="#FAFAFA"
                                    boxShadow="inset -3px -3px 2px #FFFFFF, inset 2px 2px 8px rgba(0, 0, 0, 0.08);"
                                    borderRadius="md"
                                    onChange={(e) => {
                                        setVersion(e.target.value);
                                    }}
                                    _focus={{
                                        border: '#008080 solid 2px',
                                    }}
                                >
                                    <option
                                        style={{
                                            display: 'none',
                                        }}
                                    >
                                        Select Environment
                                    </option>
                                    {contList.map((value) => {
                                        return (
                                            <option key={value} value={value}>
                                                {value}
                                            </option>
                                        );
                                    })}
                                </Select>
                                <Button
                                    mt="5"
                                    _active={{
                                        bg: '#008080',
                                        color: 'white',
                                    }}
                                    onClick={() => {
                                        if (fileData != undefined) {
                                            createContainer(
                                                fileData,
                                                version,
                                                contName
                                            );
                                        }
                                    }}
                                    size="lg"
                                >
                                    Create Environment
                                </Button>
                            </Flex>
                        </TabPanel>
                    </TabPanels>
                </Tabs>
            </Box>
        </Box>
    );
};

export default Home;
