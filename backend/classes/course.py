from abstraction.student_interface import CourseInterface

'''
Course having cid,cname
'''


class Course(CourseInterface):
    def __init__(self,cid,cname):
        self.cid=cid
        self.cname=cname
        

