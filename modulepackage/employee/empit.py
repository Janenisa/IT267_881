
from employee import Employee

class EmpIT(Employee): #คือเอาทุกอย่างของคลาสแม่ (Employee) มา
    def __init__(self, id, name, salary) -> None:
        super().__init__(id, name, salary)
        self.skill = None #เพิ่มค่าไปจากตัวแม่
        self.experience = None
        self.department = 'IT'
    
    def add_skill(self,skill):
        self.skill = skill
        
    def add_experience(self,exp):
        self.experience = exp #กำหนดให้มันว่า experience = exp

    def emp_detail(self):
        super().emp_detail() #แสดง id,name
        #หากไม่ต้องการแสดง id กับ name ก็ไม่ต้องมี super().emp_detail()
        #overriding method

        print(f'skill: {self.skill}')
        print(f'experience: {self.experience}')

    def it_salary(self): #เขียนแบบนี้เพื่อจะได้สืบทอดไปได้อีก
        self._emp_salary() #ได้มาจาก employee