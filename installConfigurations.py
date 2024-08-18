import platform
import os

def main():
    print("Configuration files installation started!")

    os = platform.system()

    print("Initiating Operating system detection...")

    if(os == "Windows"):
        print(f"Operating system: Windows")
        windowsInstallation()

def windowsInstallation():
    createWindowsProgrammingDirectory()

def createWindowsProgrammingDirectory():
    print("Creating directories...")
        
    path = "C:/Users/jeanp/Documents/programming/configFiles"
    exists = os.path.exists(path)

    if(exists == False):
        os.makedirs(path)
        print(f"Directory '{path}' created")
    else:
        print(f"Error. Directory '{path}' already exists")

main()

