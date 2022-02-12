const express = require("express");
const child = require('child_process')
const app = express()

app.get("/", (req,res) => {
    res.status(200).send("no");
})

app.get("/pyinstall/:ver", (req,res) => {
    console.log(`Install Python: ${req.params.ver}`);
    let apt = child.exec(`sudo apt-get install python${req.params.ver} -y`);
    apt.stdout.on('data', (data)=>{
        console.log(`APT: ${data}`);
    });
    let ln = child.exec(`sudo ln -sf /usr/bin/python${req.params.ver} /usr/bin/python`);
    ln.stdout.on("data", (data)=>{
        console.log("LN:", data);
    })
    res.status(200).send();
    /*
    console.log("Linked command");
    res.status("200").send();
    */
})

app.get("/pip/:pkg", (req,res)=>{
    console.log(`Pip Install`);
    let pip = child.exec(`pip3 install ${req.params.pkg}`);
    pip.stdout.on('data', (data)=>{
        console.log("pip:", data);
    });
    res.status(200).send();
})

app.get("/req", (req,res) => {
    console.log("Installing reqs.");
    let pip = child.exec("pip3 install -r requirements.txt");
    pip.stdout.on('data', (data)=>{
        console.log("req:", data);
    });
    res.status(200).send();
})

app.listen(8080, ()=>{
    console.log("Started on 8080");
})