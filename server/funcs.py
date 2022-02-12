from ctypes.wintypes import WORD
from pydoc import doc
from time import sleep
import docker
import requests
import os
import json
client = docker.from_env()

def start(contName):
    print("✨Starting environment", contName)
    with open("index.json", "r") as file:
        data = json.load(file)
        id = data[contName]["id"]
    container = client.containers.get(id)
    container.start()
    print("✅Done!")

def create_cont(reqs,pyver,contName):
    print("✨Creating Environment", contName)
    container = client.containers.run('panzerox123/tiffin_contain',volumes={os.getcwd():{"bind": '/home/workspace/dev', 'mode': 'rw'}}, detach = True, ports = {'3000/tcp':3000, '8080/tcp':8080})
    sleep(10)
    print("✨Installing Python", pyver)
    pyinstall_url = "http://localhost:8080/pyinstall/"+pyver[6:]
    pyinstall_r = requests.get(url = pyinstall_url)
    print("✨Installing Requirements")
    reqinstall_url = "http://localhost:8080/req"
    reqinstall_r = requests.get(url = reqinstall_url)
    new = {contName: {"python_version": pyver, "id": container.short_id, "path":workdir}}
    with open("index.json", "r+") as file:
        data = json.load(file)
        data.update(new)
        file.seek(0)
        json.dump(data, file)
    print("✅Done!")

def stop(contName):
    with open("index.json", "r") as file:
        data = json.load(file)
        id = data[contName]["id"]
    print("👋Stopping Environment")
    container = client.containers.get(id)
    container.stop()
    print("✅Done!")

# def destroy(contName):
#     '''
#     with open("index.json", "r+") as file:
#         data = json.load(file)
#         id = data[contName]["id"]
#         del data[contName]
#         file.seek(0)
#         json.dump(data, file)
#     '''
#     client.containers.prune({"id":"2d614fe634"})

create_cont("", "3.8", "TestContainer")
