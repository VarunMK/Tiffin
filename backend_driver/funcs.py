from pydoc import doc
from time import sleep
import docker
import requests
import json
client = docker.from_env()
def start(container):
    container = client.containers.start(container)
def create_cont(reqs,pyver):
    container = client.containers.run('panzerox123/tiffin_contain', detach = True, ports = {'3000/tcp':3000, '8080/tcp':8080})
    sleep(10)
    URL = "http://localhost:8080/pyinstall/"+pyver
    r = requests.get(url = URL)
    new = {container.short_id: reqs}
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
