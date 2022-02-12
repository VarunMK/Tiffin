from pydoc import doc


client = docker.from_env()
def start(container):
    container = client.container.start(container)
def create_cont(image):
    container = client.container.run(image, detach = True)
def create_new(dock_path, iname):
    image = client.images.build(path = dock_path, tag = iname)
    container = client.container.run(image[0], detach = True)
def run(volume):
    #need to run from volume
    pass
def install(reqs, iname):
    f = open(reqs)
    lines = f.readlines()
    deps = []
    for line in lines:
        if line[0] == '#':
            continue
        else:
            deps.append( "pip install "+line.strip())
    container = client.container.run(iname, detach = True, command = deps)
def stop(container):
    container = client.container.stop(container)
def destroy(container):
    pass
