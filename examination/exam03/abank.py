from code import interact
from bank import Bank

class ABank(Bank):
    def __init__(self, bankname: str) -> None:
        super().__init__(bankname)
        self.__loanamount:int = 0
        self.__loanyear:int = 0
        self.__loanrate:float = 0
        self.interest:float = 0
        self.monthlypay:float = 0

    @property
    def loanamount(self):
        return self.__loanamount
    
    @loanamount.setter
    def loanamount(self,value):
        self.__loanamount = value

    @property
    def loanyear(self):
        return self.__loanyear
    
    @loanyear.setter
    def loanyear(self,value):
        self.__loanyear = value

    @property
    def loanrate(self):
        return self.__loanrate
    
    @loanyear.setter
    def loanrate(self,value):
        self.__loanrate = value

    def flat_rate(self):
        self.interast = ({self.loanamount}*{self.loanrate}*{self.loanyear})
        self.mothlypay = (({self.loanamount} + {self.interast})/{self.monthlypay})
        return super().flat_rate()
        
    def display_interest(self):
        print("********** SCB Loan info ***********")
        print(f'Loan:{self.loanamount}Baht')
        print(f'Rate: {self.loanrate}%')
        print(f'Year:{self.loanyear}')
        print(f'--Interest--')
        print(f'Interest:{self.interest}Baht')
        print(f'Monthly Repayment:{self.monthlypay}Baht')
        
    
    
        
       



