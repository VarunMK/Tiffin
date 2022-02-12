import os


while True:
    cmd = input(">")
    if cmd.strip().lower() == 'exit':
        print("Exiting ...")
        exit(0)
    comm = cmd.split()
    try:
        if(comm[0]=="tiffin"):
            if(comm[1]=="build"):
                os.system("python driver.py --create "+comm[2]) #comm2 is path to dockerfile
                pass
            elif(comm[1]=="create"):
                os.system("python driver.py --createim "+comm[2]) #comm2 is path to image
                pass
            elif(comm[2]=="run"):
                #figure out how to run from volume
                pass
            elif(comm[2]=="install"):
                pass
            elif(comm[2]=="stop"):
                pass
            elif(comm[2]=="destroy"):
                pass
        elif(comm[0]=="help"):
            pass
        else:
            print("Error in input, use the help command for help")
        pass
    except:
        print("Error in input, use the help command for help")
        continue  
