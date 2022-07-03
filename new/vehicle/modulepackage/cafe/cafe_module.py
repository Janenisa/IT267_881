class Desserts:
    def __init__(self) -> None:
        self.desserts = ['ข้อวเหนียวมะม่วง', 'ข้าวเหนียวทุเรียน','ไอศครีม'] #ใช้ เพราะสามารถเพิ่มหรือลดเมนูง่ายขึ้น

    def show_desserts(self):
        return f'Desserts Menu : {self.desserts}'

class Drinks:
    def __init__(self) -> None:
        self.drinks = ['กาแฟ','ชา','น้ำอัดลม','ไวน์']

    def add_drink(self,new_drink): #คือการทำเพิ่อเราอาจะเพิ่ม
        self.drinks.append(new_drink)

    def show_drinks(self):
        return f'Drinks Menu : {self.drinks}'