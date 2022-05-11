10 DIM a$(10) : REM Create an Array with 10 spaces in it.
20 FOR i = 0 TO 9 : REM Count from 0 to 9, putting the current value into i
30 a$(i) = CHR$(i+65) : REM Add i to 65 (which is A, remember), and store it in position i in the array.
40 NEXT i
50 FOR i = 0 TO 9 : REM Count from 0 to 9, putting the current value into i
60 PRINT a$(i) : REM Print out the letter stored at position i in the array.
70 NEXT i
