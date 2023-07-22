try:
    with open("path.txt","x") as f1:#x-creation mode
     print(f1.read())
except FileNotFoundError:
    print("file not found")
except FileExistsError:
    print("file already exists. cant craete a file")
except:
    print("some errors are occured")
