from random import randint, choice
from os.path import expanduser
import linecache , sys , json, os



def getIcon():
    home = expanduser("~")
    iconPath = (home + "./crypto-icat/crypto-icons")
    iconList = os.listdir(iconPath)

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
