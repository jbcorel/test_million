from abc import ABC, abstractmethod

class Masker(ABC):
    
    @abstractmethod
    def __init__(self, symbol: str ) -> None:
        self.symbol = symbol
    
    @abstractmethod
    def mask():
        pass