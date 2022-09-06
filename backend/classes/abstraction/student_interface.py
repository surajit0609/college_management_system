from abc import ABC, abstractmethod
from unicodedata import name
class StudentInterface(ABC):
    
    @abstractmethod
    def get_roll(self):
        pass

    @abstractmethod
    def set_roll(self,roll):
        pass

    @abstractmethod
    def get_name(self,name):
        pass

    @abstractmethod
    def set_name(self):
        pass



