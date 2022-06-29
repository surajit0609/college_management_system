class Department:
    def __init__(self,deptName:str,hod:str,courses:list):
        self.deptName=deptName
        self.hod=hod
        self.courses=courses
    def __str__(self):
        return self.deptName+' '+self.hod+' '+' '.join(self.courses)