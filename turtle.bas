10 GRAPHICS 0
20 SPRITE 1 200,200,142
30 SPRITE 1 PENDOWN
40 size = 400
50 INPUT "How many sides? ", numberOfSides
60 FOR i = 1 TO numberOfSides
70 SPRITE 1 FORWARD size / numberOfSides 
80 SPRITE 1 TURN 360 / numberOfSides
90 NEXT i
