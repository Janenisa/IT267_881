from abc import ABC, abstractmethod
class Bank(ABC):
    def __init__(self,bankname:str) -> None:
        super().__init__()
        self.bankname = bankname
    
    @abstractmethod
    def flat_rate(self):
        pass
