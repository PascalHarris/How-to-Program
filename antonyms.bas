10 DIM antonyms$(10,2) : REM The antonyms array contains 10 arrays of 2 strings.
20 FOR i = 0 TO 9
30 FOR j = 0 TO 1 : REM We already used i in the previous line - so we'll use j to keep track of this inside loop.
40 READ antonyms$(i,j) 
50 NEXT j
60 NEXT i
70 FOR i = 0 TO 9
80 PRINT "The antonym of",antonyms$(i,0),"is",antonyms$(i,1)
90 NEXT I
100 DATA "Hello","Goodbye","Yes","No","Day","Night","Dark","Light","Easy","Hard","Wet"," Dry","Full","Empty","Clever","Stupid","Nasty","Nice","Fast","Slow"