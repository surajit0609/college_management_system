from abc import ABC, abstractmethod
class BranchInterface(ABC):
    
    @abstractmethod
    def get_bid(self):
        return self.bid
        

    @abstractmethod
    def set_bid(self,bid):
        self.bid=bid
        

    @abstractmethod
    def get_bname(self):
        return self.bname
        

    @abstractmethod
    def set_bname(self,bname):
        self.bname=bname
        


