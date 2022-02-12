const express = require("express");
const app = express()

app.get("/", (req,res) => {
    res.status(200).send("no");
})

app.get("/pyinstall/:ver", (req,res) => {
    console.log(`Install Python: ${ver}`);
})

app.get("/pip", (req,res)=>{
    console.log(`Pip Install`);
})

app.get("/req", (req,res) => {
    console.log("Installing reqs.")
})

app.listen(8080, ()=>{
    console.log("Started on 8080");
})