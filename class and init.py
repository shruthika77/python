class student:
    def __init__(self,name,dept,gender,):#instances variables
        self.name=name
        self.gender=gender
        self.dept=dept

    def student_checking(self):
        return ("justprinting")

    def student_attributes(self):
        return f"{self.name}|{self.dept}|{self.gender}"

   
    def apple():
        return "I like to eat apple"

    
shruthika=student('shruthika','AIDS','F')
shruthika.dept='cse'
print(shruthika.name,shruthika.dept,shruthika.gender)
      
print(shruthika.student_attributes())

print(shruthika.student_checking)

print(shruthika.apple())
