from horse import Houre
from donkey import Donkey

class Mule(Houre,Donkey):
    def __init__(self, name: str, color: str):
        super().__init__(name, color)


    def run(self):
        print (f'Mule is running')

    def show_info(self):
        print (f'Name:{self.name}')
        print (f'Color:{self.color}') 
        print (f'Max Hight:{Houre.max_height}') 
        print (f'Age:{self.age}')
        print (f'Weight:{self.weigth}')

    
         
        

  
