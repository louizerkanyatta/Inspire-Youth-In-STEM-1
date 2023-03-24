class car:
    def _init_(self,model,make,year_of_man,enginecapacity):
        self.model= model
        self.make = make
        self.year_of_man = year_of_man
        self.enginecapacity = enginecapacity


#GETTERS
def get_model(self):
    return self.model

def get_year(self):
    return self.year_of_man

def get_year(self):
    return self.make



#OBJECTS : instance of the class 
car1 =car("demio","nissan",2018,1300)
car2=car("hilux","toyota",2020,3500)
car3=car("passat","vw",2009,2600)
        
print(car1.get_model())
print(car1.get_year())

print(car2.get_model())
print(car3.get_year())

#SETTERS

def set_model(self,model):
   self.model= model

def set_year_of_man(self,year_of_man):
   self.year_of_man= year_of_man

def set_make(self,make):
   self.make= make


