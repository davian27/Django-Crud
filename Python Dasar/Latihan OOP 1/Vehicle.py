class vehicle(object):
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"Menyalakan Mesin {self.model} {self.year} {self.make}")

class Car(vehicle):
    def start_engine(self):
     print(f"Menyalakan Mesin {self.model} {self.year} {self.make}")

class motorcycle(vehicle):
   def start_engine(self):
      print(f"Menyalakan Mesin {self.model} {self.year} {self.make}")