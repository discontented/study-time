import re

class Time():
    def __init__(self, creditHours = 12, hoursPerCredit = 3):
        self.creditHours = creditHours
        self.hoursPerCredit = hoursPerCredit

    def studyTime(self):
        studyPerWeek = self.creditHours * self.hoursPerCredit
        return studyPerWeek

    def timeLeft(self, timeStudied):
        targetPerWeek = self.studyTime()
        return targetPerWeek - timeStudied

    def timePerDay(self):
        return round(self.studyTime() / 7, 2)

class Interface():
    semester = Time(None)

    def __init__(self, creditsPerClass = 4):
        self.creditsPerClass = creditsPerClass

    def getClasses(self):
        numClasses = input("How many classes are you taking this semester?\n")
        self.semester.creditHours = int(numClasses) * self.creditsPerClass
    
    def getCreditHours(self):
        answer = input("Is that %d credit hour(s) this semester?\n" % self.semester.creditHours)
        answer = answer.lower()
        if(answer == "yes"):
            print("Great!")
        elif(answer == "no"):
            self.semester.creditHours = int(input("How many total credit hours are you taking this semester?\n"))
        else:
            print("I'm sorry I couldn't understand that.")
            self.getCreditHours()

    def timeLeft(self):
        currentStudyInput = input("How much studying have you done this week?\n")
        currentStudyHours = int(re.search("\d+", currentStudyInput).group())
        studyingLeft = self.semester.timeLeft(currentStudyHours)
        print("That means you should study %d more hours this week." % studyingLeft)

    def printReport(self):
        print("Let's see...")
        print("You have a total of %d credit hours and it's usually around %d hours per credit to study." % (self.semester.creditHours, self.semester.hoursPerCredit))
        print("That means you should be dedicating %d hours per week to studying." % self.semester.studyTime())
        self.timeLeft()

menu = Interface()
menu.getClasses()
menu.getCreditHours()
menu.printReport()