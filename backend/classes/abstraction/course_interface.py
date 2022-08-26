from abc import ABC, abstractmethod
class CourseInterface(ABC):
    
    @abstractmethod
    def get_cid(self):
        pass

    @abstractmethod
    def set_cid(self):
        pass

    @abstractmethod
    def get_cname(self):
        pass

    @abstractmethod
    def set_cname(self):
        pass


