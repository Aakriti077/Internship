from abc import ABC, abstractmethod


class Vehical(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehical):
    def start(self):
        pass

    def stop(self):
        pass

    
car = Car()