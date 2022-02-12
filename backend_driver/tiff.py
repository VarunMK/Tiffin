while True:
    cmd = input(">")
    if cmd.strip().lower() == 'exit':
        print("Exiting ...")
        exit(0)
    comm = cmd.split()
    try:
        if(comm[0]=="tiffin"):
            if(comm[1]=="create"):
                pass
            elif(comm[2]=="run"):
                pass
            elif(comm[2]=="update"):
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
