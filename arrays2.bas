10 DIM a$(7)
20 FOR i = 0 TO 6
30 READ a$(i)
40 NEXT i
50 DATA "Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday" 
60 INPUT "What day of the week are you interested in (1-7)? ",number
70 PRINT a$(number-1)