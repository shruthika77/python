class dog:
    #pass
 def __init__(self,name,color,age,birth_place):
    self.name_= name
    self.color_=color
    self.age_=age
    self.birth_place_=birth_place

    def sitting(self):
        print(f"{self.name} is sitting")

    def __str__(self):
        return self,breed_
        
    @staticmethod
    def bark():
        print("dog is barking")
    
husky=dog("rose","black&white",14,"siberia")
rajapalayam=dog("jimmy","white",18,"tamilnadu")

for dog_breed in[husky,rajapalyam]:
    print(dog_breed.name_)
    print(dog_breed.age_)


#husk=dog()
#rajapalayam=dog()

#husky.orgin_place="siberia"
#rajapalayam.origin_place="tamil nadu"
