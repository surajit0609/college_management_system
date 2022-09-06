from unicodedata import name
from abstraction.student_interface import StudentInterface

'''
Student having roll,name
'''


class Student(StudentInterface):
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    
    def get_roll(self):
        return self.roll

   
    def set_roll(self,roll):
        self.roll=roll

   
    def get_name(self,name):
        return self.name


    def set_name(self):
        self.name=name

        
    # def accepted(self,name,roll):
    #     ob=Student(name,roll)
    #     ls.append(ob)

    

