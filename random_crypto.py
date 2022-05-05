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
                if coin == i[:i.find(".")]:
                    print(coin + ".png")
    else:
        print(random.choice(iconList))




def main():
    getIcon()
    '''
    generation = evaluate_generation()

    home = expanduser("~")
    pokemon = linecache.getline(home + "/.pokemon-icat/nameslist.txt", evaluate_index(generation))[:-1]

    print(f"{pokemon} - {roman_numerals(generation)} Generation")
    '''
if __name__ == "__main__":
    main()
