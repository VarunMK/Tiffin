from pydoc import doc
from time import sleep
import docker
import requests

client = docker.from_env()
def start(container):
    container = client.containers.start(container)
def create_cont(reqs,pyver):
    container = client.containers.run('panzerox123/tiffin_contain', detach = False, ports = {'3000/tcp':3000, '8080/tcp':8080})
    URL = "localhost:8080/pyinstall/"+pyver
    r = requests.get(url = URL)
def run(volume):
    #need to run from volume
    pass
def stop(container):
    container = client.containers.stop(container)
def destroy(container):
    pass

