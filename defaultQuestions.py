import questionClasses

# this dictionary will hold all the questions and their options
# qnDict(questionNumber:questionclasses object
# each question has a number e.g question 1 was : Select your age bracket

qnDict = {}

# THis section will populate all the 25 questions

qnDict.update({1: questionClasses.SurveyQn.createSurveyQn("Select your age bracket", "19 -25 years", "26 - 45 years",
                                                          "46  -60 years", "Above 61 years", "Below 18 years")})
qnDict.update({2: questionClasses.SurveyQn.createSurveyQn("Select gender", "FEMALE", "MALE")})
qnDict.update({3: questionClasses.SurveyQn.createSurveyQn("Select highest educational level attained", "Graduate",
                                                          "Post graduate", "Primary", "Secondary", "Tertiary")})
qnDict.update({4: questionClasses.SurveyQn.createSurveyQn("Which is your occupation category", "Academia",
                                                          "Banking and financial sector", "Casual laborer",
                                                          "Catering and hospitality business",
                                                          "Entertainment Sector",
                                                          "Farming", "Health care and social workers", "journalism",
                                                          "Religious sector", "Retirees", "Sanitation Business",
                                                          "Security sector", "Students",
                                                          "Trade, manufacturing, construction business",
                                                          "Transportation sector")})
qnDict.update({5: questionClasses.SurveyQn.createSurveyQn("Choose most prevalent chronic illness if any", "Cancers",
                                                          "chronic Respiratory illnesses",
                                                          "Digestive disease or Disorders", "HIV/AIDS",
                                                          "low or high blood pressure", "none",
                                                          "other chronic illnesses")})
qnDict.update({6: questionClasses.SurveyQn.createSurveyQn("which vaccine type did you prefer", "Mixed or any",
                                                          "mRNA(Pfizer, Moderna)", "Protein subunit( Novavax)",
                                                          "Vector (Astra zenaca, Janssen/Johnson & Johnson")})
qnDict.update({7: questionClasses.SurveyQn.createSurveyQn("what determined your choice of vaccine", "Availability",
                                                          "Brand", "Recommendation", "Technology")})
qnDict.update({8: questionClasses.SurveyQn.createSurveyQn("How many vaccination doses have you received so far",
                                                          "3 or more", "one", "two")})
qnDict.update(
    {9: questionClasses.SurveyQn.createSurveyQn("which brand of vaccine did you receive for the first dose",
                                                "Astra Zeneca", "Jansen/johnson and johnson", "Moderna",
                                                "other",
                                                "Pfizer", "Sinovac", "Sinovac")})
qnDict.update({10: questionClasses.SurveyQn.createSurveyQn("What determined the choice of brand or type of vaccine",
                                                           "Other", "recommendation by colleague",
                                                           "The nature of side effects",
                                                           "The number of doses recommended",
                                                           "was available brand at facility")})
qnDict.update(
    {11: questionClasses.SurveyQn.createSurveyQn("Which level of side effects did you develop after dose1",
                                                 "Adverse (Required a visit to doctor or getting hospitalized)",
                                                 "Minor or None ( could go about usually daily activities)",
                                                 "Moderate ( noticeable with some effect to daily activities)")})
qnDict.update(
    {12: questionClasses.SurveyQn.createSurveyQn("when did effects show up after the jab 1", "after 24 hours",
                                                 "Immediately", "Not applicable", "within 12 hours")})
qnDict.update({13: questionClasses.SurveyQn.createSurveyQn("which was the most dominant side effect after jab 1",
                                                           "diarrhea and vomiting", "fatigue or general malaise",
                                                           "Fever or chills", "flu, cough or both", "Headache",
                                                           "none of the above or not applicable",
                                                           "other not listed",
                                                           "Pain at the injection site or muscle pain",
                                                           "respiratory discomfort ", "sex related side effects")})
qnDict.update({14: questionClasses.SurveyQn.createSurveyQn("how long did jab 1 side effects last", "1 Day",
                                                           "1 month or more", "3 Days")})
qnDict.update(
    {15: questionClasses.SurveyQn.createSurveyQn("which brand of vaccine did you receive for the second dose",
                                                 "Astra Zeneca", "Jansen/johnson and johnson", "Moderna",
                                                 "other", "Pfizer", "Sinovac", "Sinovac")})
qnDict.update(
    {16: questionClasses.SurveyQn.createSurveyQn("Which level of side effects did you develop after dose 2",
                                                 "Adverse (Required a visit to doctor or getting hospitalized)",
                                                 "Minor or None ( could go about usually daily activities)",
                                                 "Moderate ( noticeable with some effect to daily activities)")})
qnDict.update(
    {17: questionClasses.SurveyQn.createSurveyQn("when did effects show up after the jab 2", "after 24 hours",
                                                 "Immediately", "Not applicable", "wiithin 12 hours")})
qnDict.update({18: questionClasses.SurveyQn.createSurveyQn("which was the most dominant side effect after jab 2",
                                                           "diarrhea and vomiting", "fatigue or general malaise",
                                                           "Fever or chills", "flu, cough or both", "Headache",
                                                           "none of the above or not applicable",
                                                           "other not listed",
                                                           "Pain at the injection site or muscle pain",
                                                           "respiratory discomfort ", "sex related side effects")})
qnDict.update({19: questionClasses.SurveyQn.createSurveyQn("how long did jab 2 side effects last", "1 Day",
                                                           "1 month or more", "3 Days")})
qnDict.update(
    {20: questionClasses.SurveyQn.createSurveyQn("what your main source of infomation on the side effects",
                                                 "friends, family colleagues and the like", "Health workers",
                                                 "mass media", "personal experience ",
                                                 "search engines like Google", "social media")})
qnDict.update({21: questionClasses.SurveyQn.createSurveyQn("were given means to report side effects", "NO", "YES")})
qnDict.update({22: questionClasses.SurveyQn.createSurveyQn("were you scared of possible side effects of covid-19 "
                                                           "vaccine", "NO", "YES")})
qnDict.update(
    {23: questionClasses.SurveyQn.createSurveyQn("do you know anyone personally who died of covid-19", "NO",
                                                 "YES")})
qnDict.update({24: questionClasses.SurveyQn.createSurveyQn("i know someone who died from covid-19 despite being "
                                                           "vaccinated", "NO", "YES")})
qnDict.update(
    {25: questionClasses.SurveyQn.createSurveyQn("i know someone who died of covid-19 vaccine side effects",
                                                 "NO", "YES")})
