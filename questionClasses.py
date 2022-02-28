# This file will template the survey question classes and methods that will handle the survey questions#

from dataclasses import dataclass


class SurveyQn:
    defaultQuestion = "No survey question supplied"

    def __init__(self, aQuestion=defaultQuestion, nbrOfOptions=None, theOptionNbrChosen=None, *optionsList):
        """
        This will create the instance of a survey question . Survey question will have the following options
        aQuestion => This is the actual survey question
        Note that default constructors have been provided through the use of class methods that will take in account
        the different number os scenarios that may appear during the creation of the survey question class.
        For example a survey question must have, a question, a number of options, the option chosen for an answer,
        and the list of options from which to choose from.
        I a new survey question is to be created , a class method the ony asks for the question has been provided.
        similarly, if survey question in complete , like when it is picked from a csv file or excel, and we want to
        populate it for display , a method class that constructs the object after: the question, number of options ,
        the option chosen, and the options list , have been provided is available.
        Generally, choose a class method depending on options you are going to provide.

        :param aQuestion: The survey question
        :param nbrOfOptions:The number of options this survey wuation will have
        :param theOptionNbrChosen:In case the question is answered , this will be the index of the answer in the list
        :param optionsList:

        """
        surveyQuestionsOptions = {}  # this will hold the survey Question options. using a dictionary
        self.surveyQuestion = aQuestion
        if nbrOfOptions == 0 or nbrOfOptions is None:
            self.numberOfOptions = int()
        else:
            self.numberOfOptions = nbrOfOptions

        surveyQuestionAnswer = None  # this will hold the string of question option

        self.__putOptionsListIntoDictionary(*optionsList)

        # if the option number chosen is not in the dictionary then make the survey question un answered
        # setting the surveyChosenOptionNbr = 0 or None
        # This will be achieved by checking to see if  the surveyChosenOptionNbr is present as a key in the
        # surveyQuestionsOptions dictionary
        # after the options have been put into the dictionary , we can then get a chance to test if the
        # surveyChosenOptionNbr is the list of keys of that dictionary. if the surveyChosenOptionNbr is not
        # in the keys, surveyChosenOptionNbr for that object instance will be set to zero to signify that the
        # question was not answered

        if theOptionNbrChosen == 0 or theOptionNbrChosen is None:
            self.surveyChosenOptionNbr = None
        elif theOptionNbrChosen not in self.surveyQuestionsOptions:
            self.surveyChosenOptionNbr = None
            # print("i have grabbed the key not present")
        else:
            # THis will hold the nbr of the option chosen in the list of options
            self.surveyChosenOptionNbr = theOptionNbrChosen

            # This class method will enable the instant creation of an object when survey question and answer are
            # applied.

    @classmethod
    def createSurveyQn(cls, qnString=defaultQuestion, *surveyQnOpts):
        """
        This will return an object of type which have a survey question and it's options where the question and options
        are the only supplied as parameters

        qn = createSurveyQn("HOW MANY ARE YOU","ONE","TWO"
        :param numberOfOptions:  the number of options the survey question will have
        :param qnString: what is the question
        :param surveyQnOpts: options is quotes separated by commas
        :return:
        """

        sQn = qnString
        # compute the number of options

        return cls(sQn, len(surveyQnOpts), None, *surveyQnOpts)

    @classmethod
    def createSurveyQnWithNbrOfOptions(cls, qnString=defaultQuestion, nbrOfOptions=int(), *surveyQnOpts):
        """
        This will create and return an object on the type survey when the survey question , number of options
        and the list of options are supplied, this will mainly be useful when picking data from the csv file
        :param qnString: the survey question
        :param nbrOfOptions: the number of options the survey questions has
        :param surveyQnOpts: the list of the options
        :return: surveyQn object instance
        """
        sQn = qnString
        return cls(sQn, len(surveyQnOpts), nbrOfOptions, *surveyQnOpts)

    @classmethod
    def createSurveyQnAndAnswer(cls, qnString=defaultQuestion, nbrOfOptions=int(), answerOptionNbr=None, *surveyQnOpts):
        """
        This will be used to create the full survey question with the number of options and the answer chosen.
        this will be most useful when creating the data structure that will be returned to the file as a complete
        survey response or when read from the file that will store the completed surveys
        :param answerOptionNbr: This will be the index or listing number of the options chosen as an answer to the Qn
        :param qnString: this will be the question string
        :param nbrOfOptions: this will be the number of options to choose from as answers to the question
        :param surveyQnOpts: this list will hold the options for the survey question
        :return: will return the surveyQn instance of the object but this object will have the qn, answer and options
        """
        return cls(qnString, len(surveyQnOpts), answerOptionNbr, *surveyQnOpts)
        pass

    @staticmethod
    def myNameIs(myobj: int):
        print(myobj.defaultQuestion)

    # To display the survey question for the object
    def whatIsTheSurveyQn(self):
        """ This will just show the survey question"""
        print(self.surveyQuestion)

    def print_surveyQuestionAnswer(self):
        """
        This will print the survey Question Answer
        :return:
        """
        if (self.surveyChosenOptionNbr == 0 or
                self.surveyChosenOptionNbr is None or
                self.surveyChosenOptionNbr not in self.surveyQuestionsOptions):
            print(str(self.surveyQuestion) + ":" + " has no valid answer set")
        else:
            print("Question     : " + self.surveyQuestion)
            print("Option chosen: " + str(self.surveyChosenOptionNbr))
            print("Option Answer: " + str(self.surveyQuestionsOptions.get(self.surveyChosenOptionNbr)))

    def set_surveyQuestion(self):
        self.surveyQuestion = str(input("Please enter the survey question:"))
        # please provide functionality to test if a blank question is entered
        # provide functionality in case one chooses to abort the entering a question
        #

    def get_surveyQuestionAnswer(self):
        """
        This will return, as string, the actual answer to the survey question
        :return:
        """
        if (self.surveyChosenOptionNbr == 0 or
                self.surveyChosenOptionNbr is None or
                self.surveyChosenOptionNbr not in self.surveyQuestionsOptions):
            return "Question Not Answer"
        else:
            return str(self.surveyQuestionsOptions.get(self.surveyChosenOptionNbr))
    # to enter the options for the survey questions at once
    def get_surveyQuestionOptionsAtOnce(self, *qnOptions):
        """
        This will get the list of options through and put them into the options' dictionary.
        Since this method takes a list as an argument, the options should be supplies in quotes
        and separarted by commas.
        THis method can also called after the method that will capture the options one by one
        from the user
        It does this by calling the __putOptionsListIntoDictionary() method.

        :param qnOptions:
        :return:
        """
        if len(qnOptions) == 0:
            print("No answer options entered")
        else:
            print(str(len(qnOptions)) + " : have been supplied and arranged in numbered dictionary ")
            self.__putOptionsListIntoDictionary(*qnOptions)
            print("and have now been put in dictionary")

    # to get the number of options the survey question we have the pass it
    # to the function that will capture those options in a step-by-step process
    def get_numberOfOptions(self):
        """
        This function give an opportunity to the user to specify the number of survey question options they want to
        supply to a particular survey Question.
        Since zero or 1 does not really offer a choice , entering 0 or 1 will signal the cancellation of the process
        :return:
        """
        input_value = input("Enter the number of options for survey Question(0 or 1 to cancel): ")
        # zero options or one option does not really give choice , does it?
        try:
            self.numberOfOptions = int(input_value)
        except ValueError:
            print(" This is not a whole number: ", input_value)
        else:
            # print(" This is a whole number: ")
            # print("before function call the type is : ",type(self.numberOfOptions))
            self.get_surveyQuestionOptionsByCount(self.numberOfOptions)

    def get_surveyQuestionOptionsByCount(self, nbrOfOptions):
        '''
        This function will get the numbers options specified by the nbrOfOptions argument passed.
        The variable will be tested to determine is it an integer using isinstance(var, int).
        if it is not an , the options will not be captured from the user and the function will exit.
        if the integer is zero 0 , still this wil imply that the user desired not to input options.
        :param nbrOfOptions:
        :return:

        '''

        if isinstance(nbrOfOptions, int):
            if nbrOfOptions == 0 or nbrOfOptions == 1:
                print("0 or 1 for cancel has been entered, survey options not captured.")
            else:
                print("Please enter ", nbrOfOptions, " options.")
                print("call the function that will capture the specified number of options at this point")
        else:
            print("value enter is of un wanted type: ", type(nbrOfOptions), ". only integer type wanted.")

    def __putOptionsListIntoDictionary(self, *listOfQnOptions):
        """
        This will put the list passed to it into numerical keyed dictionary starting from one.
        It wil also count the number of options in the list and set the value of the number of options that particular
        survey questions has
        :param listOfQnOptions:
        :return:
        """
        # This method will put the list of options passed, into the objects' options dictionary surveyQuestionsOptions
        self.surveyQuestionsOptions = {}
        self.numberOfOptions = len(listOfQnOptions)
        for ctr in range(len(listOfQnOptions)):
            # lists start from 0 but i want my keys in the dictionary to start from 1 that is why ctr+1
            # remove leading and trailing space and extra spaces in the string
            self.surveyQuestionsOptions[ctr + 1] = str.strip(listOfQnOptions[ctr])

    def print_surveyQuestionOptions(self):
        """
        This will print the options available to the survey question in a list format that is numbered
        :return:
        """
        # recall that range(1,5) will return 1 2 3 4 but not 5
        # I forced the first index to be 1 not 0 so that the dictionary would be listed starting with 1
        if len(self.surveyQuestionsOptions) == 0:
            print("This survey question has no options to print! ")
        else:
            lastItem = len(self.surveyQuestionsOptions) + 1
            for i in range(1, lastItem):
                print(str(i) + " : " + self.surveyQuestionsOptions.get(i))

    def surveyOptions(self):
        pass
    def get_surveyQuestion(self):
        """
        This will return the survey question  of the object. Their is a function called whatIsTheSurveyQuestion
        that print the survey question of the object but this function just returns the question as a string
        :return:
        """
        return self.surveyQuestion

    def print_surveyOptions(self):
        """
        This is print the options of the survey on one line
        :return:
        """
        if len(self.surveyQuestionsOptions) == 0:
            print("This survey question has no answer options.")
        elif len(self.surveyQuestionsOptions) == 1:
            print("This survey question has only on option please edit it")
        else:
            # print("Here you will print the survey options")
            print(self.surveyQuestionsOptions)
