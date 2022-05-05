from os.path import expanduser
import shutil, os
def main():

    home = expanduser("~")
    currentDir = os.getcwd()
    sourceDir = (currentDir + "/icon")
    destinationDir = (f"{home}/.crypto-icat/crypto-icons")
    shutil.copytree(sourceDir, destinationDir, dirs_exist_ok=True)

    shutil.rmtree(sourceDir)

    print("Images Copied 📲 ")
if __name__ == "__main__":
    main()
