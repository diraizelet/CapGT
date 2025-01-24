class car:
    def __init__(self,name):
        self.brand=name
    
class Skoda(car):
    def setWheels(self,wheel):
        self.wheelSize=wheel
    def setDoors(self,doors):
        self.countDoor=doors
    def setEngine(self, engine):
        self.engineType=engine
    
if __name__ =="__main__":
    s = Skoda("Skoda")
    s.setDoors("Double Doors")
    s.setEngine("V4")
    s.setWheels(84) 
    print(s.brand+" "+s.countDoor+" "+s.engineType)