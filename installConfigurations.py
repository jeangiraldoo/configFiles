import platform 
import os 
def main(): 
    print("Configuration files installation started!") 
    operatingSystem = platform.system() 
    user = os.getlogin()
    print("Initiating Operating system detection...")

    if(operatingSystem == "Windows"):
        print(f"Operating system: Windows")
        print(f"User: {user}")
        windowsInstallation(user)

def windowsInstallation(user):
    createWindowsProgrammingDirectory(user)
    files = {"init.lua":f"C:/Users/{user}/Desktop"}
    for fileName in(files):
        moveConfigurationFile(fileName, files[fileName]) 

def createDirectory(path):
    exists = os.path.exists(path)
    if(exists == False):
        os.makedirs(path)
        print(f"Directory '{path}' created")
    else:
        print(f"Error. Directory '{path}' already exists")

def moveConfigurationFile(fileName, path):
    print(f"Moving {fileName} to {path}")
    print(path)
    os.system(f"move {fileName} {path}")

def createWindowsProgrammingDirectory(user):
    print("Creating directories...")
        
    path = f"C:/Users/{user}/Documents/programming/configFiles"
    createDirectory(path)

main()

