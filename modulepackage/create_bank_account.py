#การลองเรียกใช้ให้เพิ่มการใส่ account ดูชื่อและคำผิดถูกดีดี
#เรียกใช้ package เพื่อเข้าถึงตลาสของ Customer, Account
from Bank.customer import Customer
from Bank.account import Account

#สร้าง object ของ customer ชื่อ Paul
pual = Customer() #คือตั้งชื่อให้มันว่า พอลคือ คลาสโทเมอร์
pual.new_customer()

#สร้าง objec ของ account เพื่อเปิดบัญชีให้กับ paul
pual_acc = Account()
pual_acc.open_account(pual.name, 'Saving', '0123-4578',500)

#แสดงข้อมูล customerPaul
print(pual.cus_info())

#แสดงข้อมูลคงเหลือของบัญชี Paul #เรียก balance มาใช้
print(pual_acc.display_balance())
