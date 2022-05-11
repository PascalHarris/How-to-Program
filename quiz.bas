10 REM Set up Variables
20 numberofquestions = 3
30 score = 0
40 correctanswer = TRUE
50 DIM questions$(numberofquestions,2)
60 REM Fill the questions and answers Array 
70 FOR i = 0 TO numberofquestions-1
80 FOR j = 0 TO 1 : REM We already used i in the previous line - so we'll use j to keep track of this inside loop.
90 READ questions$(i,j)
100 NEXT j
110 NEXT i
120 WHILE correctanswer : REM This means that questions will keep being asked until the player gets one wrong - with only three questions, this could be a very boring game!
130 questionnumber = RND(numberofquestions)
140 PRINT questions$(questionnumber,0)
150 INPUT answer$
160 IF answer$ = questions$(questionnumber,1) THEN correctanswer = 1 : ELSE correctanswer = FALSE
170 IF NOT correctanswer THEN PRINT "No - the correct answer is ";questions$(questionnumber,1) : ELSE PRINT "Well Done"
180 score = score+correctanswer
190 WEND
200 PRINT "You Scored ";score
210 END : REM A convenient marker for the end of your program.
220 DATA "What continent did Christopher Columbus Discover","America","In which city is Nelson's Column","London","What is the Capital city of France","Paris"