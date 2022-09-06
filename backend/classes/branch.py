from abstraction.student_interface import BranchInterface

'''
Course having bid,bname
'''


class Branch(BranchInterface):
    def __init__(self,bid,bname):
        self.bid=bid
        self.bname=bname
       
    

