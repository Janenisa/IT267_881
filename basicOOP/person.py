class Person:#สร้าง class
    def __init__(self,name,gender,profession:str) -> None:
        self.name = name
        self.gender = gender
        self.profession = profession
        self.study = 0
     
    def work(self):
        print(f'{self.name} working as a {self.profession}')
    
    def study(self,hours):
       self.study = hours

    def show(self):
        print(f'Name: {self.name} Gender: {self.gender} Profession: {self.profession} Study: {self.study}')

#person1
jessa = Person('Jessa' , 'Female' , 'Softwere Engineer')
jessa.work()
jessa.show()

#person2
jon = Person('Jon' , 'Male' , 'Doctor' )
jon.study()
jon.work()
jon.show()

#person3
lisa = Person('lisa' , 'Female' , 'Korean Singer')
jon.study()
lisa.work()
lisa.show()