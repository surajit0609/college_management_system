from abc import ABC, abstractmethod
class StudentInterface(ABC):
    
    @abstractmethod
    def get_roll(self):
        pass

    @abstractmethod
    def set_roll(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def set_name(self):
        pass


