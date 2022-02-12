import os
import sys, argparse
import docker

parser = argparse.ArgumentParser(description="tiffin")

parser.add_argument('--create', dest = 'create', type=str, help='Name of command') ##name of image, also needs path to docker file with -p
parser.add_argument('--createim', dest = 'createim', type=str, help='Name of command') #name of image
parser.add_argument('--start', dest = 'createim', type=str, help='start existing container') #container ID?
parser.add_argument('--run', dest = 'run', type=str, help='Name of command')
parser.add_argument('--install', dest = 'install', type=str, help='Name of command') # path to req.txt
parser.add_argument('--stop', dest = 'stop', type=str, help='Name of command') #name of container or id
parser.add_argument('--destroy', dest = 'destroy', type=str, help='Name of command')
parser.add_argument('--n', dest = 'n', type=str, help='Name of image')
parser.add_argument('--p', dest = 'p', type=str, help='path to dockerfile')

args = parser.parse_args()
client = docker.from_env()

if(args.start):
    container = client.container.start(args.start)
elif(args.createim):
    container = client.container.run(args.createim, detach = True)
elif(args.create):
    image = client.images.build(path = args.p, tag = args.create)
    container = client.container.run(image[0], detach = True)
elif(args.run):
    #need to run from volume
    pass
elif(args.install):
    f = open(args.install)
    lines = f.readlines()
    deps = []
    for line in lines:
        if line[0] == '#':
            continue
        else:
            deps.append( "pip install "+line.strip())
    container = client.container.run(args.n, detach = True, command = deps)
elif(args.stop):
    container = client.container.stop(args.stop)
elif(args.destroy):
    pass

