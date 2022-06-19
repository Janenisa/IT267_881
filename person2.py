class Person:#สร้าง class
    def __init__(self,name,gender,profession:str,study) -> None:
        self.name = name
        self.gender = gender
        self.profession = profession
        self.study = study
     
    def work(self):
        print(f'{self.name} working as a {self.profession}')
    

    def show(self):
        print(f'Name: {self.name} Gender: {self.gender} Profession: {self.profession} Study: {self.study}')
    def __del__(self):
            print("Object was destroyed")

if __name__=="__main__":
    #person1
    jessa = Person('Jessa' , 'Female' , 'Softwere Engineer',0)
    jessa.work()
    jessa.show()

    #person2
    jon = Person('Jon' , 'Male' , 'Doctor',15)
    jon.work()
    jon.show()

    #person3
    lisa = Person('lisa' , 'Female' , 'Korean Singer',10)
    lisa.work()
    lisa.show()