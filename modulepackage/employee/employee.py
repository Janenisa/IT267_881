class Employee:
    def __init__(self,id,name,salary) -> None:
        self.id = id
        self.name = name
        self._salary = salary
        
    def emp_detail(self):
        print(f'id: {self.id}')
        print(f'name: {self.name}')


    def _emp_salary(self): #เพราะมี#ข้างหน้าตอนในโจทย์เลยใช้ _ ถูกป้องกันไว้เพราะปกป้องข้อมูลคือสืบทอดได้ถึงแค่ลูกได้ทอดเดียวเท่านั้น
        print(f'salary: {self._salary}')
    