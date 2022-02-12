from pydoc import doc
from time import sleep
import docker

client = docker.from_env()
def start(container):
    container = client.containers.start(container)
def create_cont(reqs, image,pyver):
    container = client.containers.run(image, detach = False, ports = {'3000/tcp':3000, '8080/tcp':8080})
    install(reqs, image, pyver)
def run(volume):
    #need to run from volume
    pass
def install(reqs, iname,pyver):
    f = open(reqs)
    lines = f.readlines()
    container = client.containers.run(iname, ports = {'3000/tcp':3000, '8080/tcp':8080})
    sleep(5)
    
def stop(container):
    container = client.containers.stop(container)
def destroy(container):
    pass

create_cont('reqs.txt', 'panzerox123/tiffin_contain', )