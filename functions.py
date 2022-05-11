def dayOfTheWeek(_dayNumber):
    _weekDays = ["Sun", "Mon", "Tues", "Wednes", "Thurs", "Fri", "Satur"] 
    return _weekDays[_dayNumber-1]+”day”

dayNumber = input("What day of the week are you interested in? ") 
print ("Day "+str(dayNumber)+" is "+dayOfTheWeek(dayNumber))