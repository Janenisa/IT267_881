class Donkey:
    def __init__(self,age:int,weigth:float):
        self.age = age
        self.weigth = weigth

    def sound(self):
        print (f'Donkey makes eeyore')

    def show_info(self):
        print(f'Agn:{self.age}-year-old')
        print(f'Weigth:{self.weigth} kg')