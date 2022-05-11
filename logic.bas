10 a = TRUE
20 b = FALSE
30 IF a THEN PRINT "1. True" : REM This will print True because a has been set to TRUE.
40 IF b THEN PRINT "2. True" : REM This line prints nothing because b isn't TRUE.
50 IF NOT b THEN PRINT "3. True" : REM This line will print True because b is NOT TRUE.
60 IF a AND b THEN PRINT "4. True" : REM This line prints nothing because a is TRUE but b isn't.
70 IF a OR b THEN PRINT "5. True" : REM This line prints "True" because a is TRUE even though b isn't.
