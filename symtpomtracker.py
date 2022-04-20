import matplotlib.pyplot as plt #this line is giving me an error, pip isn't allowing me to download matplotlib
import numpy as np

class DailyTracker():
    def __init__ (self, symptomTitles, behaviorTitles):
        #self.symptomTitles = [] #[headache, stomach ache]
        #self.dailyActivityTitles = [] #[miles walked]
        self.symptomTitles = symptomTitles #list of the names of the symptoms (not the data)
        self.dailyActivityTitles = behaviorTitles #list of the behaviors (but not the data)
        self.symptomData = [] #[5, 1]
        self.behaviorData = [] #[14.2]


def onboarding():
    """
    Onboards the user by prompting them to add symptoms & daily behaviors they want to track.
    Users can stop adding by entering -1.
    No parameters required, returns symptomTitles, behaviorTitles as lists
    """
    listOfDailyDataObjects = [] #this is what stores the DailyTrackerObjects objects, can access via indexing
    singleSymptom = 0
    i=0
    symptomTitles = []
    while (singleSymptom != "-1"):
        print("These are the symptoms you have added: ")
        for j in symptomTitles:
            #prints out already-entered symptoms
            print(j)
        print()
        print()
        singleSymptom = input("what symptoms do you want to track? (eg. headache, to stop adding symptoms enter -1)? ")
        if (singleSymptom!=-1):
            symptomTitles.append(singleSymptom)
        i=i+1

    i=0
    singleBehavior = ""
    behaviorTitles = []

    while (singleBehavior != "-1"):
        #prints out already-entered behaviors
        print("These are the behaviors you have added: ")
        for j in behaviorTitles:
            print(j)
        print()
        print()
        singleBehavior = input("what daily behaviors do you want to track (eg. hours of sleep, miles walked etc, to stop adding enter -1)? ")
        if (singleBehavior!= "-1"):
            behaviorTitles.append(singleBehavior)
        i=i+1

    print()
    print()

    return symptomTitles, behaviorTitles

def dailySymptomTracker(symptomTitles, behaviorTitles):
    """
    Keeps looping as individuals keep adding their daily data. User can data-input
    loop by entering "n" when prompted.
    """

    listOfDailyDataObjects = [] #this is what stores the DailyTrackerObjects objects, can access via indexing
    keepAdding = "y"
    while (keepAdding=="y"):
        #while loop to continue adding symptom data
        dailyData = DailyTracker(symptomTitles, behaviorTitles)
        p=0
        if (len(dailyData.symptomTitles)!=0):
            for p in range(0, (len(dailyData.symptomTitles)-1)):
                symptomSeverity = input("On a scale of 0-5, with 5 being the worst, what was your %s today? " %dailyData.symptomTitles[p])
                if symptomSeverity.isnumeric():
                    symptomSeverity = float(symptomSeverity)
                    dailyData.symptomData.append(symptomSeverity)
                    p=p+1
        q=0
        for q in dailyData.dailyActivityTitles:
            behaviorLevel = input("Describe your %s numerically: " %q)
            if behaviorLevel.isnumeric():
                behaviorLevel = float(behaviorLevel)
                dailyData.behaviorData.append(behaviorLevel)
                listOfDailyDataObjects.append(dailyData)
        keepAdding = input("Do you want to add another day? Enter y/n: ")

    return listOfDailyDataObjects

def getGraphs(listOfDailyDataObjects):
    if len(listOfDailyDataObjects) >= 3: #Only set to three for demonstration purposes.
        plot = input("Would you like to view plots based on the data you gave us? We will show correlations between symptoms and habits to inform you and your physician's next steps.")
        if plot.upper() == 'YES':
            for symptomIndex in range(len(listOfDailyDataObjects[0].symptomData)):  # x-axis
                for behaviorIndex in range(len(listOfDailyDataObjects[0].behaviorData)):  # y-axis
                    xList = []
                    yList = []  # xList, yList should be equal in length
                    for day in range(len(listOfDailyDataObjects)):
                        xList.append(listOfDailyDataObjects[day].symptomData[symptomIndex])
                        yList.append(listOfDailyDataObjects[day].behaviorData[behaviorIndex]) #do we ever convert the string type to the integer type?
                        #print(yList)
                    correlationCoefficient = np.corrcoef(xList, yList)
                    print("The correlation coefficient is: ", correlationCoefficient[0][0])
                    if (correlationCoefficient[0][0] > 0.49): #error is here because it says we're comparing a list
                        if (0.8 > correlationCoefficient[0][0] >= 0.5):
                            print(f'There is a moderate positive correlation between {listOfDailyDataObjects[0].symptomTitles[symptomIndex]} and {listOfDailyDataObjects[0].dailyActivityTitles[behaviorIndex]}; this should be explored further, as this may explain a causal relationship')
                            plt.plot(xList, yList)
                            plt.title(f'Correlation between {listOfDailyDataObjects[0].dailyActivityTitles[behaviorIndex]} and {listOfDailyDataObjects[0].symptomTitles[symptomIndex]}')
                            plt.xlabel(listOfDailyDataObjects[0].symptomTitles[symptomIndex])
                            plt.ylabel(listOfDailyDataObjects[0].dailyActivityTitles[behaviorIndex])
                            plt.show()
                        else:
                            print(f'There is a strong positive correlation between {listOfDailyDataObjects[0].symptomTitles[symptomIndex]} and {listOfDailyDataObjects[0].dailyActivityTitles[behaviorIndex]}; this should be explored further, as this may explain a causal relationship')
                            plt.plot(xList, yList)
                            plt.title(f'Correlation between {listOfDailyDataObjects[0].dailyActivityTitles[behaviorIndex]} and {listOfDailyDataObjects[0].symptomTitles[symptomIndex]}')
                            plt.xlabel(listOfDailyDataObjects[0].symptomTitles[symptomIndex])
                            plt.ylabel(listOfDailyDataObjects[0].dailyActivityTitles[behaviorIndex])
                            plt.show()
                    elif (correlationCoefficient[0][0] < -0.51):
                        if (-0.8 < correlationCoefficient[0][0] <= -0.5):
                            print(f'There is a moderate negative correlation between {listOfDailyDataObjects[0].symptomTitles[symptomIndex]} and {listOfDailyDataObjects[0].dailyActivityTitles[behaviorIndex]}; this should be explored further, as this may explain a causal relationship')
                            plt.plot(xList, yList)
                            plt.title(f'Correlation between {listOfDailyDataObjects[0].dailyActivityTitles[behaviorIndex]} and {listOfDailyDataObjects[0].symptomTitles[symptomIndex]}')
                            plt.xlabel(listOfDailyDataObjects[0].symptomTitles[symptomIndex])
                            plt.ylabel(listOfDailyDataObjects[0].dailyActivityTitles[behaviorIndex])
                            plt.show()
                        else:
                            print(f'There is a strong negative correlation between {listOfDailyDataObjects[0].symptomTitles[symptomIndex]} and {listOfDailyDataObjects[0].dailyActivityTitles[behaviorIndex]}; this should be explored further, as this may explain a causal relationship')
                            plt.plot(xList, yList)
                            plt.title(f'Correlation between {listOfDailyDataObjects[0].dailyActivityTitles[behaviorIndex]} and {listOfDailyDataObjects[0].symptomTitles[symptomIndex]}')
                            plt.xlabel(listOfDailyDataObjects[0].symptomTitles[symptomIndex])
                            plt.ylabel(listOfDailyDataObjects[0].dailyActivityTitles[behaviorIndex])
                            plt.show()
    else:
        print("insufficient data collected; we cannot provide you with statistically-sound graphs plotting correlation")

    return None




def main():
    symptomTitles, behaviorTitles = onboarding()
    listOfDailyDataObjects = dailySymptomTracker(symptomTitles, behaviorTitles)
    getGraphs(listOfDailyDataObjects)
main()


"""
Still need to fix the UI, just trying to get the data structure to work
onboarding edits would include making it clearer as to what to add as the data, could make a range of what the values would be between
add a more unique prompt that uses the range of values
add in the graphing component
add section to save most recent graph to print again?
can do some wireframing/mockups to include in the presentation

TO DO:
fix errors in graphing
commment code to describe it better
add in the type of data they are entering & overall more robust error checking
suggestion of graphs that are more useful: when i learn about machine learning can we suggest more graphs?
make them be able to create their own graphs
separate into different functions so its better organized
can i reach out to someone in CIL to see if i can get a mentor or support if i were to continue the project
add a welcome message
issue with downloading matplotlib and pip.... need to do more research to figure out what's going on :(

Notes from 3/5/22:

Fixed errors with passing data between functions
Added comments, broke the code up into functions for readability

Thought: can we change the data storage method to be a dictionary somehow to get
linear access time? Will it matter because we need to for loop through all objects
in the list/dict anyway?

Need to upload to github
"""
