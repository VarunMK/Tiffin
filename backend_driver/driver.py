import sys, argparse

parser = argparse.ArgumentParser(description="tiffin")

parser.add_argument('--create', dest = 'create', type=str, help='Name of command')
parser.add_argument('--run', dest = 'run', type=str, help='Name of command')
parser.add_argument('--update', dest = 'update', type=str, help='Name of command')
parser.add_argument('--stop', dest = 'create', type=str, help='Name of command')
parser.add_argument('--destroy', dest = 'create', type=str, help='Name of command')
parser.add_argument('--n', dest = 'create', type=str, help='Name of file')
parser.add_argument('--p', dest = 'create', type=str, help='path of file')

args = parser.parse_args()


def create(name, path="/src"):
    

if(args.create):
    create(args.n, args.path)
    pass
elif(args.run):
    run(args.run, args.n)
    pass
elif(args.update):
    pass
elif(args.stop):
    pass
elif(args.destroy):
    pass

