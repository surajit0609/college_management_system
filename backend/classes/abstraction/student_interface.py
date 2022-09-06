from abc import ABC, abstractmethod
from unicodedata import name
class StudentInterface(ABC):
    
    @abstractmethod
    def get_roll(self):
        return self.roll

    @abstractmethod
    def set_roll(self,roll):
        self.roll=roll

    @abstractmethod
    def get_name(self,name):
        return self.name

    @abstractmethod
    def set_name(self):
        self.name=name



