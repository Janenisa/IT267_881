class Car: #กำหนดชื่อ Class
    brand = "Toyota" #ชื่อแบรนด์

    def __init__(self,model :str,colour :str,year:int,price:int) -> None: #กำหนดว่ามีอะไรบ้างที่เราจะใช้ เลือกให้ โมเดลเป็นสตริง ปีเป็นint
        self.model = model #กำหนดว่า โมเดลคือ self.model เพื่อเวลาเรียก Object เรียกมันเอง
        self.colour = colour #
        self.year = year
        self.price = price
#มันคือ instance method def printCarDetail(self):
    def printCarDetail(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Colour: {self.colour}")
        print(f"Year:{self.year}")
        print(f"Price: {self.price: ,.2f}") #,.2f ใส่เพื่อให้ใส่ค่าเป็นทสนิยมได้ ตัว กำหนดเป็นค่าของมัน
#@staticmethod ไม่มีคำว่า self
    @staticmethod 
    def get_static_method():
        text = "static" #ตัวแปล Text ใช้ได้เแค่ใน get_static_method() เท่านั้น printCarDetail(self) ใช้ไม่ได้
        print(f"In {text} method") #{}คือใส่ค่าตัวแปลเป็น text
        
    def __del__(self):
        print("object was destroyed") #กำหนด print ให้ได้แบบไหนก็ได้

if __name__=="__main__":
    my_car = Car("Cross","White",2022,1500000) #กำหนดให้มันปริ้นค่านี้
    my_car.printCarDetail()

    #การเรียกใช้ static_method
    Car.get_static_method() #เรียกผ่าน Class
    my_car.get_static_method() #เรียกผ่าน instance/object