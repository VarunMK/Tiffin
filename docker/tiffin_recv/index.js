const express = require("express");
const app = express()

app.get("/", (req,res) => {
    res.status(200).send("no");
})

app.listen(8080, ()=>{
    console.log("Started on 8080");
})