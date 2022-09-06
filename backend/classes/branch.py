from abstraction.student_interface import BranchInterface

'''
Course having bid,bname
'''


class Branch(BranchInterface):
    def __init__(self,bid,bname):
        self.bid=bid
        self.bname=bname
    def get_bid(self):
       return self.bid
        

   
    def set_bid(self,bid):
        self.bid=bid
        

    
    def get_bname(self):
        return self.bname
        

    
    def set_bname(self,bname):
        self.bname=bname
       
    

