from abc import ABC, abstractmethod
class CourseInterface(ABC):
    
    @abstractmethod
    def get_cid(self):
        return self.cid

    @abstractmethod
    def set_cid(self,cid):
        self.cid=cid

    @abstractmethod
    def get_cname(self):
        return self.cname

    @abstractmethod
    def set_cname(self,cname):
        self.cname=cname


