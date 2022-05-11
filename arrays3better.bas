10 DIM week$(7)
20 FOR i = 0 TO 6
30 READ week$(i) : REM Fill up the week array
40 NEXT i
50 DIM food$(7)
60 FOR i = 0 TO 6 : REM Fill up the food array
70 READ food$(i)
80 NEXT i
90 DATA "Sunday","Monday","Tuesday","Wednesday","Thursday","Friday", "Saturday"
100 DATA "Lamb","Burgers","Cheese","Sandwiches","Fruit","Fish","Salad"