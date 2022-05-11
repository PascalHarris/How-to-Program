10 CLASS equine
40 characteristics$ AS STRING
50 species$ AS STRING
60 SUB init(SpeciesName$)
70 this.species$ = SpeciesName$
80 END SUB
90 SUB addCharacteristic(characteristic$)
100 this.characteristics$=this.characteristics$+","+characteristic$ 
150 END SUB
160 SUB showCharacteristics()
170 PRINT this.species$+" is "+this.characteristics$
220 END SUB
230 END CLASS
240 DIM a AS NEW equine
250 CALL a.init("Horse")
260 CALL a.addCharacteristic("tame")
270 CALL a.addCharacteristic("fond of sugar lumps")
280 DIM b AS NEW equine
290 CALL b.init("Donkey")
300 CALL b.addCharacteristic("short")
310 CALL b.addCharacteristic("grey") 
320 CALL b.addCharacteristic("tame") 
330 DIM c AS NEW equine
340 CALL c.init("Zebra")
350 CALL c.addCharacteristic("stripy") 
360 CALL c.addCharacteristic("wild") 
370 CALL a.showCharacteristics()
380 CALL b.showCharacteristics()
390 CALL c.showCharacteristics()