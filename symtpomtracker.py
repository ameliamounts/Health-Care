def main():


    class DailyTracker():
        def __init__ (listSymptomTitles, listBehaviorTitles):
            symptomTitles = listSymptomTitles #list of the names of the symptoms (not the data)
            dailyActivityTitles = listBehaviorTitles #list of the behaviors (but not the data)
            symptomData = []
            behaviorData = []
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


    k=0
    dailyData = DailyTracker(listSymptomTitles, listBehaviorTitles)
    p=0
    for p in dailyData.symptomTitles:
        symptomSeverity = input("On a scale of 0-5, with 5 being the worst, was your %s today?", dailyData.symptomTitles[p])
        dailyData.symptomData[p]=symptomSeverity
    q=0
    for q in dailyData.behaviorTitles[q]:
        behaviorLevel = input("Add behavior... ")
        dailyData.behaviorData[q]=behaviorLevel
    listOfDailyDataObjects[k]= dailyData
    k=k+1

main()


        #this is the main loop that keeps running and adding data to the data structure, at the end we can create graphs each day as long as day is over 10??
