class Flight():
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.passengers = []
        
    def add_passenger(self, name):
        if not self.open_seat() :
            return False
        self.passengers.append(name)
        return True
       
         
        
    def open_seat(self):
        return self.capacity - len(self.passengers)        
        
        
        
        
flight =Flight(3)


people = ["Ren", "hed", "caleb", "kate", "Adu"]
for pers in people:
    
    if flight.add_passenger(pers):
        print(f"Added {pers} to flight Successfully")
    else:
        print(f"No available seat  for {pers}")
    
      
