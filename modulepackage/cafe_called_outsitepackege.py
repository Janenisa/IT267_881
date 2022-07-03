#วิธี 1
from cafe.cafe_module import Desserts
from cafe.cafe_module import Drinks #คือการเรียกโมดูลเฉพาะเจาะจงว่าจะเอา cafe_module เลือกเป็น Desserts

#วิธี 2
#from cafe_module import Desserts,Drink
from cafe import cafe_module
desserts = Desserts() #desserts เป็นออปเจคถูกเรียกใช้งานโดยคลาส Desserts()
print(desserts.show_desserts())

drinks = Drinks() #คือการให้มันรันค่าโดยดึงข้อมูลจาก module
print(drinks.show_drinks()) #คือการเพิ่มเมนู สมูทตี้ ไปต่อท้ายเมนูปกติ
drinks.add_drink('สมูทตี้')
print(drinks.show_drinks())
drinks.add_drink('น้ำผลไม้') #คือการเพิ่มเมนู น้ำผลไม้ ไปต่อท้ายเมนูปกติ
print(drinks.show_drinks())



