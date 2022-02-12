import os
import sys, argparse
import docker

parser = argparse.ArgumentParser(description="tiffin")

parser.add_argument('--create', dest = 'create', type=str, help='Name of command')
parser.add_argument('--createim', dest = 'createim', type=str, help='Name of command')
parser.add_argument('--run', dest = 'run', type=str, help='Name of command')
parser.add_argument('--update', dest = 'update', type=str, help='Name of command')
parser.add_argument('--stop', dest = 'stop', type=str, help='Name of command')
parser.add_argument('--destroy', dest = 'destroy', type=str, help='Name of command')
parser.add_argument('--n', dest = 'n', type=str, help='Name of image')
parser.add_argument('--p', dest = 'p', type=str, help='path of file')

args = parser.parse_args()
client = docker.from_env()

def create(name, path="/src"):
    
    pass

if(args.create):
    pass
elif(args.run):
    pass
elif(args.update):
    pass
elif(args.stop):
    pass
elif(args.destroy):
    pass

