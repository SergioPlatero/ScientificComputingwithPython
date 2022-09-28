def add_time(start_time, duration, opt = ""):
    """
    Add duration time to start time and return result.
    If result will be the next day, it should show (next day) after
    the time. If the result is more than 1 day later, it will show (n days later).

    Assumes start time is in "12:00" format, AM or PM specified.
    Assumes that duration minutes is less than 59, but hours could be any number.
    Third parameter is option-> it indicates the starting day of the week.
        If indicated, then the results will also show the ending day of the week.

    """

    weekdays = {1:"sunday", 2:"monday", 3:"tuesday", 4:"wednesday", 5:"thursday", 6:"friday", 7:"saturday"}
    mins = list(range(60))
    hour = list(range(13))

    start_time = start_time.split(" ")
    am_pm = start_time[1]
    am_pm = am_pm.upper()
    start_time = start_time[0].split(":")
    startHour = int(start_time[0])
    startMin = int(start_time[1])
    duration = duration.split(":")
    durationHour = int(duration[0])
    durationMin = int(duration[1])
    initialDay = opt.lower()
    startDayNum = 0
    addedDay = 0
    newDay = 0
    ender = ""

    
    if initialDay in weekdays.values():
        startDayNum = [key for key, value in weekdays.items() if value == initialDay]
        startDayNum = int(startDayNum[0])

    def update_durationHour(startMin, durationMin, durationHour):
        totalMin = startMin + durationMin
        hourCount = 0
        while totalMin >= 60:
            hourCount += 1
            totalMin -= 60

        durationHour += hourCount
        totalMin = str(totalMin)
        
        if len(totalMin) == 1:
            totalMin = "0"+totalMin
            
        
        return [durationHour, totalMin]
  

    def convert_time(startHour, durationHour):
        curTime = startHour + durationHour
        while curTime > 12:
            curTime -= 12
        return curTime

    sumTime = update_durationHour(startMin, durationMin, durationHour)
    durationHour = sumTime[0] #This is the total time in Hours past the inital input, including the min calculations
    newMin = sumTime[1] #This is the final min mark

    if am_pm == "PM":
        if (durationHour+startHour) > 12:
            ender = "(next day)"

    def addDay(startHour, durationHour):
        curTime = startHour+durationHour
        num = 0
        while curTime >= 12:
            curTime -= 12
            num += 1

        if num >= 2:
            addedDay = round(num/2)
        else:
            addedDay = 0
            
        return addedDay

    addedDay = addDay(startHour, durationHour)
    
    if initialDay in weekdays.values():
        for i in weekdays:
            if weekdays[i] == initialDay:
                startDayNum = i
                addedDay = addDay(startHour, durationHour)
                newDay = startDayNum + addedDay
                
    if addedDay > 1:
        ender = f"({addedDay} days later)"
    elif addedDay == 1:
        ender = f"(next day)"

        
    if newDay > 0:
        newDay = newDay % 7
        newDay = weekdays[newDay]
        newDay = newDay.capitalize() 
            

    def convert_am_pm(startHour, durationHour, am_pm):
        curTime = startHour+durationHour
        num = 0
        while curTime >= 12:
            curTime -= 12
            num += 1

        if am_pm == "AM":
            if num%2 == 0:
                pass
            else:
                am_pm = "PM"
        elif am_pm == "PM":
            if num%2 == 0:
                pass
            else:
                am_pm = "AM"

        am_pm_Final = am_pm
        return am_pm_Final



    newHour = convert_time(startHour, durationHour) #This is the new calculated hour, using the function defined above
    am_pm_Final = convert_am_pm(startHour, durationHour, am_pm) #This is the final AM or PM description, saved for final use.


    if opt.lower() in weekdays.values():
        if ender != "":
            new_time = f"{newHour}:{newMin} {am_pm_Final}, {newDay} {ender}"
        else:
            new_time = f"{newHour}:{newMin} {am_pm_Final}, {newDay}"
    else:
        if ender !="":
            new_time = f"{newHour}:{newMin} {am_pm_Final} {ender}"
        else:
            new_time = f"{newHour}:{newMin} {am_pm_Final}"



    return new_time
