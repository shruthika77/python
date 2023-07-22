class vehicle:
    def __init__(self):
        pass
    def usecase(self):
        return "used for transportation"


class car(vehicle):
    def __init__(self,mode_transportation):
        self.mode_transportation=mode_transportation
        
    def get_mode_transportation(self):
        return f"{self.mode_transportation}"
    
    def usecase(self):
      return super().usecase()#super is used to access the parent
     # return "used for road transporation"
mini_coopper=car("land:road")
print(mini_coopper.get_mode_transportation())
print(mini_coopper.usecase())
