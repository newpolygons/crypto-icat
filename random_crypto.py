from random import randint, choice
from os.path import expanduser
import linecache , sys , json, os, random



def getIcon():
    home = expanduser("~")
    iconPath = (home + "/.crypto-icat/crypto-icons")
    iconList = os.listdir(iconPath)

    if len(sys.argv) > 1:

        crypto = sys.argv[1]
        if crypto == "--crypto" or crypto == "-c":
            coin = sys.argv[2:]
            for i in iconList:
                file = i[:i.find(".")]
                if coin[0] == file:
                    print(coin[0] + ".png")
    else:
        print(random.choice(iconList))




def main():
    getIcon()
    
if __name__ == "__main__":
    main()
