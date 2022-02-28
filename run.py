import questionClasses
import pandas
from menus import *
import os

surveys = {}


def main():
    mainMenuChoice = 10
    while mainMenuChoice > 0:
        mainMenuChoice = mainMenu()
        # print(str(mainMenuChoice) + " selected")

        print("Menu for : " + mainMenuDict.get(mainMenuChoice))

        os.system("cls")

        if mainMenuChoice == 1:
            useDefaultSurveyMenuChoice = useDefaultSurveyMenu()
            if useDefaultSurveyMenuChoice == 0:
                print("Move back to main menu")
                mainMenu()
            else:
                print("program quit...")

        else:
            print("Program exited....")


if __name__ == "__main__":
    main()

