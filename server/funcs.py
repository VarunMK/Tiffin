from pydoc import doc
from time import sleep
import docker
import requests
import os
import json
client = docker.from_env()

def start(container):
    container = client.containers.start(container)
def create_cont(reqs,pyver,contName):
    container = client.containers.run('panzerox123/tiffin_contain',volumes={os.path.join(contName):{'bind':'/mnt/{contName}','mode':'rw'}}, detach = True, ports = {'3000/tcp':3000, '8080/tcp':8080})
    sleep(10)
    pyinstall_url = "http://localhost:8080/pyinstall/"+pyver
    pyinstall_r = requests.get(url = pyinstall_url)
    reqinstall_url = "http://localhost:8080/req"
    new = {contName: {"python_version": pyver, "id": container.short_id, "path": os.path.join(contName)}}
    with open("index.json", "r+") as file:
        data = json.load(file)
        data.update(new)
        file.seek(0)
        json.dump(data, file)
def run(volume):
    #need to run from volume
    pass
def stop(container):
    container = client.containers.stop(container)
def destroy(container):
    pass