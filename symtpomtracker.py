def main():
    listOfDailyDataObjects = []

    class DailyTracker():
        def __init__ (self, listSymptomTitles, listBehaviorTitles):
            self.symptomTitles = []
            self.dailyActivityTitles = []
            self.symptomTitles = listSymptomTitles #list of the names of the symptoms (not the data)
            self.dailyActivityTitles = listBehaviorTitles #list of the behaviors (but not the data)
            self.symptomData = []
            self.behaviorData = []
        def addSymptomSeverity(listSymptomData, listBehaviorData):
            symptomData = listSymptomData
            behaviorData = listBehaviorData

        #ONBOARDING
    singleSymptom = 0
    i=0
    listSymptomTitles = []
    while (singleSymptom != "-1"):
        print("These are the symptoms you have added: ")
        for j in listSymptomTitles:
            print(j)
        singleSymptom = input("what symptoms do you want to track? (eg. headache, stomach pain, etc, to stop adding symptoms enter -1)? ")
        listSymptomTitles.append(singleSymptom)
        i=i+1
    i=0
    singleBehavior = 0
    listBehaviorTitles = []
    while (singleBehavior != "-1"):
        for j in listBehaviorTitles:
            print(j)
        singleBehavior = input("what daily behaviors do you want to track (eg. hours of sleep, caloric intake, etc, to stop adding enter -1)? ")
        listBehaviorTitles.append(singleBehavior)
        i=i+1



    dailyData = DailyTracker(listSymptomTitles, listBehaviorTitles)
    p=0
    if (len(dailyData.symptomTitles)!=0):
        for p in range(0, (len(dailyData.symptomTitles)-1)):
            symptomSeverity = input("On a scale of 0-5, with 5 being the worst, was your %s today?"% p)
            dailyData.symptomData[p] = symptomSeverity
            p=p+1
    q=0
    for q in dailyData.dailyActivityTitles[q]:
        behaviorLevel = input("Add behavior... ")
        dailyData.behaviorData.append(behaviorLevel)
    listOfDailyDataObjects.append(dailyData)


main()

#Still need to fix the UI, just trying to get the data structure to work

