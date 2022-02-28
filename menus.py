import os
from defaultSurvey import *

mainMenuDict = {0: "Quit Program",
                1: "Use Default Survey(available)",
                2: "Edit Survey",
                3: "Create survey",
                4: "Analyze survey",
                5: "organize Survey",
                }
useDefaultSurveyMenuDict = {0: "Previous menu(Main menu)",
                            1: "Edit survey",
                            2: "Analyze survey for actionable insights (available)",
                            3: "View survey details(available)",
                            4: "save survey questions to file",
                            5: "Load survey questions from file"
                            }

viewSurveyDetailsMenuDict = {0: "Back to previous menu",
                             1: "Display all questions",
                             2: "Display a particular question",
                             3: "Display all questions and options",
                             4: "Display a particular question and its options"
                             }
analyzeSurveyMenuDict = {0: "Back to previous menu",
                         1: "View summary by Survey response",
                         2: "View summary by question(available)",
                         3: "View complete survey summary"

                         }


def useDefaultSurveyMenu():
    """
    this will load the menu for use the in built survey
    :return:
    """
    useDefaultSurveyMenu_selection = 100
    os.system('cls')
    while useDefaultSurveyMenu_selection > 0:
        os.system('cls')
        print("Please select an option:")
        for i in range(len(useDefaultSurveyMenuDict)):
            print(str(i) + " : " + useDefaultSurveyMenuDict.get(i))

        try:
            useDefaultSurveyMenu_selection = int(input("Please Enter selection: "))
        except:
            useDefaultSurveyMenu_selection = 0
        else:
            if useDefaultSurveyMenu_selection not in useDefaultSurveyMenuDict:
                os.system('cls')
                useDefaultSurveyMenu_selection = 100  # this will  make the menu of this section appear again
            else:
                os.system('cls')
                print("another menu then analysis")
                print_analyzeSurveyMenu()

    return useDefaultSurveyMenu_selection


def print_analyzeSurveyMenu():
    analyzeSurveyMenuDict_selection = 100
    while analyzeSurveyMenuDict_selection > 0:
        os.system('cls')
        print("The following are the analysis options available")
        for key in analyzeSurveyMenuDict.keys():
            print(key, " : " + analyzeSurveyMenuDict[key])

        try:
            analyzeSurveyMenuDict_selection = int(input("Enter analysis option :"))
        except:
            analyzeSurveyMenuDict_selection = 0
        else:
            os.system('cls')
            if analyzeSurveyMenuDict_selection not in analyzeSurveyMenuDict.keys():
                analyzeSurveyMenuDict_selection = 100
                print("Please select again")
            else:
                os.system('cls')
                if analyzeSurveyMenuDict_selection == 2 : viewSummaryByQuestion()

                print("Please call the analysis functions as selected")
                viewCompleteSurveySummary()


def mainMenu():
    """
    This will display the main menu of the program:
    :return:
    """
    os.system('cls')
    print("Please select an option(invalid choice crashes program):")
    for key in mainMenuDict.keys():
        print(key, " : " + mainMenuDict[key])
    try:
        mainMenuSelection = int(input("Please Enter selection: "))
    except:
        mainMenuSelection = 0

    if mainMenuSelection not in mainMenuDict.keys():mainMenuSelection = 0

    return mainMenuSelection
