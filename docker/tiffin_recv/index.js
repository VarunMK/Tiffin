const express = require("express");
const child = require('child_process')
const app = express()

app.get("/", (req, res) => {
    res.status(200).send("no");
})

app.get("/pyinstall/:ver", (req, res) => {
    console.log(`Install Python: ${req.params.ver}`);
    let apt = child.exec(`sudo apt-get install python${req.params.ver} python${req.params.ver}-dev -y`);
    apt.stdout.on('data', (data) => {
        console.log(`APT: ${data}`);
    });
    apt.on('exit', () => {
        let pip = child.exec(`python${req.params.ver} -m pip install pip`)
        pip.on('exit', () => {
            let ln = child.exec(`sudo ln -sf /usr/bin/python${req.params.ver} /usr/bin/python`);
            ln.stdout.on("data", (data) => {
                console.log("LN:", data);
            })
            ln.on('exit', () => {
                res.status(200).send();
            })
            apt.on('error', (err)=>{
                res.status(500).send(err);
            })        
        })
        pip.on('error', (err)=>{
            res.status(500).send(err);
        })    
    })
    apt.on('error', (err)=>{
        res.status(500).send(err);
    })
    /*
    console.log("Linked command");
    res.status("200").send();
    */
})

app.get("/pip/:pkg", (req, res) => {
    console.log(`Pip Install`);
    //let pip = child.exec(`pip install ${req.params.pkg}`);
    let pip = child.exec(`tiffin install ${req.params.pkg}`);
    pip.stdout.on('data', (data) => {
        console.log("pip:", data);
    });
    pip.on('exit', ()=>{
        res.status(200).send();
    })
    pip.on('error', (err)=>{
        res.status(500).send(err);
    })
})

app.get("/req", (req, res) => {
    console.log("Installing reqs");
    let pip = child.exec(`pip install -r /home/workspace/dev/requirements.txt`);
    pip.stdout.on('data', (data) => {
        console.log("req:", data);
    });
    pip.on('exit', ()=>{
        res.status(200).send();
    })
    pip.on('error', (err)=>{
        res.status(500).send(err);
    })
})

app.listen(8080, () => {
    console.log("Started on 8080");
})