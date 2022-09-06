from abstraction.student_interface import StudentInterface

'''
Student having roll,name
'''


class Student(StudentInterface):
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        
    # def accepted(self,name,roll):
    #     ob=Student(name,roll)
    #     ls.append(ob)
sname=["surajit","rahul","bivas","pritam"]
sroll=[1,2,3,4]
ob=Student(sname,sroll)

    

