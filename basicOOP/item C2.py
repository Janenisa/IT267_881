class Item:

    def __init__(self,name :str,price:float,quantity=1) -> None: 
        
        #assert price assert quantity คือการตรวจสอบ price, quantity ว่าต้อง > 1
        assert price > 0,f"Price {price} must greater than 0" #คือไว้ตรวจสอบค่าต้องมากกว่า 0
        assert quantity > 0,f"Quantity {quantity} must greater than 0"  #คือถ้ามากกว่า 0 มันจะหยุดทำงานแล้ว Run คำสั่งต่อไปต่อ

        self.name = name
        self.price = price
        self.quantity = quantity

#Totle_price(self) คือ instance methode ต้องมีคำว่า self เสมอ 
#จะเรียกใช้ method นี้ได้ต้องมีการสร้าง object
    def total_price(self): #มันคือชื่อObject
        return self.price * self.quantity 
        #บรรทัดบนคือลดขั้นตอนมาเป็นบรรทัดเดียวจากที่ต้องเขียน 
        #self.totle = self.price * self.quantity
        #return self.total

    def __del__(self):
        print("Object was destroyed")

if __name__== "__main__":
    item1 = Item("Monitor",5600)
    item2 = Item("Mouse",1500,4)
    print("=== Total Price ==")
    print(f"{item1.name} : {item1.total_price():,.2f}")
    print(f"{item2.name} : {item2.total_price():,.2f}")
