10 SUB dayOfTheWeek$(dayNumber) 
20 DIM weekDays$(7)
30 FOR i = 0 TO 6
40 READ weekDays$(i)
50 NEXT i
60 dayOfTheWeek$=weekDays$(dayNumber-1)+"day"
70 END SUB
80 INPUT "What day of the week are you interested in? ",dayNumber 
90 PRINT "Day "+STR$(dayNumber)+" is "+dayOfTheWeek$(dayNumber) 
100 END
110 DATA "Sun","Mon","Tues","Wednes","Thurs","Fri","Satur"
