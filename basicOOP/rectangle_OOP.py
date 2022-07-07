class Rectangle: #สร้างclass
    def __init__(self,width,length) -> None :
        self.width = width
        self.length = length
        self.area = 0
    def compute_area(self):
        self.area = self.width * self.length
    def print_area(self):
        print(f'Rectangle area = {self.area}')

if __name__ == "__main__": #ใช้เวลาจะปริ้นค่าอะไรเพื่อไม่ให้ไปซ้ำ
    rec = Rectangle(2,5)
    rec.compute_area()
    rec.print_area()
    