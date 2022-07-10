class Houre:

    max_height:float = "200 เซนติเมตร"

    def __init__(self,name:str,color:str):
        self.name = name
        self.color = color   

    def run(self):
        return f'({self.name} is running)'
    
    def show_name(self):
        return f'Name : ({self.name})'

    def show_info(self):
        print (f'Name:{self.name}')
        print (f'Color:{self.color}')
        print (f'Hight:{Houre.max_height}')
