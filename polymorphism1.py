class Processor():
    def Type(self):
        print("Type")
class Samsung(Processor):
    def Snapdragon(self):
        print("Snapdragon Gen Elite")
class Redmi(Processor):
    def Octacore(self):
        print("Octacore")
r1=Redmi()
r1.Type()
r1.Octacore()