from employee import Employee

class Empmkt(Employee):
    def __init__(self, id, name, salary) -> None:
        super().__init__(id, name, salary)
        self.location = 'Bangkok'
        self.commission = 30
        self.department = 'Marketing'

    def add_location(self,location:str):
        self.location = location

    def add_commission(self,commission:int): 
        self.commission = commission

    def emp_detail(self):
        super().emp_detail()
        print(f'location: {self.location}')
        print(f'commission: {self.commission} %')