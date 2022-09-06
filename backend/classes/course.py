from abstraction.student_interface import CourseInterface

'''
Course having cid,cname
'''


class Course(CourseInterface):
    def __init__(self,cid,cname):
        self.cid=cid
        self.cname=cname
    
    def get_cid(self):
        return self.cid

    
    def set_cid(self,cid):
        self.cid=cid

    
    def get_cname(self):
        return self.cname

    
    def set_cname(self,cname):
        self.cname=cname  

