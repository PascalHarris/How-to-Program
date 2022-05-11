10 CLASS Player
20 ScreenWidth AS INTEGER
30 ScreenHeight AS INTEGER
40 SpriteNumber AS INTEGER
50 x AS INTEGER
60 distance AS INTEGER
70 SUB init(screen)
80 this.SpriteNumber = 1
90 this.ScreenWidth = screen(0)
100 this.ScreenHeight = screen(1)
110 this.x = this.ScreenWidth/2
120 this.distance = 3
130 REM SPRITE this.SpriteNumber, 0, "Spaceship.gif", this.x,0, 129 
140 SPRITE this.SpriteNumber this.x,this.ScreenHeight-40 ,142
145 SPRITE this.SpriteNumber PENUP
150 END SUB
160 SUB CurrentPosition()
170 CurrentPosition = this.x
180 END SUB
190 SUB MoveLeft()
195 IF this.x > 0+10
200 this.x = this.x - this.distance
210 SPRITE this.SpriteNumber LEFT this.distance
215 END IF
220 END SUB
230 SUB MoveRight()
235 IF this.x < this.ScreenWidth-10
240 this.x = this.x + this.distance
250 SPRITE this.SpriteNumber RIGHT this.distance
255 END IF
260 END SUB
270 END CLASS
275 GRAPHICS 0
280 DIM a AS NEW Player
290 DIM screen(2)
300 screen(0) = 640 : REM width
310 screen(1) = 480 : REM height
320 CALL a.init(screen)
330 running = TRUE
335 DIM i AS INTEGER
340 WHILE running
341 PRINT i
342 i=i+1
345 DOEVENTS()
350 IF macfunction("keydown",123) :REM Left Key pressed
360 CALL a.MoveLeft() 
370 END IF
380 IF macfunction("keydown",124) :REM Right Key pressed 
390 CALL a.MoveRight()
400 END IF
410 IF macfunction("keydown",12) :REM Q Key pressed
420 running = FALSE
430 END IF
435 FN SLEEP (0.01) 
440 WEND
