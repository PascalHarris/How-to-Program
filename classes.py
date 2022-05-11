class Equine:
    def __init__(self,species):
        self.species = species 
        self.characteristics = []
    def addCharacteristic(self,characteristic): 
        self.characteristics.append(characteristic)
    def showCharacteristics(self):
        print (self.species+" is "+str(self.characteristics)[1:-1])

a = Equine('Horse')
a.addCharacteristic('tall') 
a.addCharacteristic('tame') 
a.addCharacteristic('fond of sugar lumps') 
b = Equine('Donkey') 
b.addCharacteristic('short') 
b.addCharacteristic('grey') 
b.addCharacteristic('tame')
c = Equine('Zebra') 
c.addCharacteristic('stripy') 
c.addCharacteristic('wild')

a.showCharacteristics() 
b.showCharacteristics() 
c.showCharacteristics()
