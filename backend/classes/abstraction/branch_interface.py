from abc import ABC, abstractmethod
class BranchInterface(ABC):
    
    @abstractmethod
    def get_bid(self):
       pass
        

    @abstractmethod
    def set_bid(self,bid):
        pass
        

    @abstractmethod
    def get_bname(self):
        pass
        

    @abstractmethod
    def set_bname(self,bname):
        pass
        


