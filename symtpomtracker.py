def main():
    listOfDailyDataObjects = [] #this is what stores the DailyTrackerObjects objects, can access via indexing

    class DailyTracker():
        def __init__ (self, listSymptomTitles, listBehaviorTitles):
            self.symptomTitles = []
            self.dailyActivityTitles = []
            self.symptomTitles = listSymptomTitles #list of the names of the symptoms (not the data)
            self.dailyActivityTitles = listBehaviorTitles #list of the behaviors (but not the data)
            self.symptomData = []
            self.behaviorData = []

        #ONBOARDING
    singleSymptom = 0
    i=0
    listSymptomTitles = []
    while (singleSymptom != "-1"):
        print("These are the symptoms you have added: ")
        for j in listSymptomTitles:
            print(j)
        print()
        print()
        singleSymptom = input("what symptoms do you want to track? (eg. headache, to stop adding symptoms enter -1)? ")
        if (singleSymptom!=-1):
            listSymptomTitles.append(singleSymptom)
        i=i+1
        
    i=0
    singleBehavior = 0
    listBehaviorTitles = []

    while (singleBehavior != "-1"):
        print("These are the behaviors you have added: ")
        for j in listBehaviorTitles:
            print(j)
        print()
        print()
        singleBehavior = input("what daily behaviors do you want to track (eg. hours of sleep, miles walked etc, to stop adding enter -1)? ")
        if (singleBehavior!=-1):
            listBehaviorTitles.append(singleBehavior)
        i=i+1


    print()
    print()
    dailyData = DailyTracker(listSymptomTitles, listBehaviorTitles)
    p=0
    if (len(dailyData.symptomTitles)!=0):
        for p in range(0, (len(dailyData.symptomTitles)-1)):
            symptomSeverity = input("On a scale of 0-5, with 5 being the worst, what was your %s today? " %dailyData.symptomTitles[p])
            dailyData.symptomData.append(symptomSeverity)
            p=p+1
    q=0
    for q in dailyData.dailyActivityTitles:
        behaviorLevel = input("Describe your %s: " %q)
        dailyData.behaviorData.append(behaviorLevel)
    listOfDailyDataObjects.append(dailyData)


main()

#Still need to fix the UI, just trying to get the data structure to work
#onboarding edits would include making it clearer as to what to add as the data, could make a range of what the values would be between
#add a more unique prompt that uses the range of values
#add in the graphing component
#add section to save most recent graph to print again?
#can do some wireframing/mockups to include in the presentation
