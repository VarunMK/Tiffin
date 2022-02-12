import os
import sys, argparse
import docker

parser = argparse.ArgumentParser(description="tiffin")

parser.add_argument('--create', dest = 'create', type=str, help='Name of command') ##name of image,
parser.add_argument('--start', dest = 'createim', type=str, help='start existing container') #container ID?
parser.add_argument('--run', dest = 'run', type=str, help='Name of command')
parser.add_argument('--stop', dest = 'stop', type=str, help='Name of command') #name of container or id
parser.add_argument('--destroy', dest = 'destroy', type=str, help='Name of command')
parser.add_argument('--n', dest = 'n', type=str, help='Name of image')

args = parser.parse_args()
client = docker.from_env()

if(args.start):
    container = client.container.start(args.start)
elif(args.create):
    container = client.container.run(args.create, detach = True)
elif(args.run):
    #need to run from volume
    pass
elif(args.stop):
    container = client.container.stop(args.stop)
elif(args.destroy):
    pass

