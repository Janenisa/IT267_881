from cusorder import customer,order #เรียกแพคเกจกับไฟล์

cus = customer.Customer("Jame", "Nonthaburi")
ord = order.Order("15-06-2022","packed")

print(f'Order of {cus.cus_name} on {ord.date} is {ord.status}') #เรียกใช้ ฟังค์ชัน cus_name ใน Customer เรียกใช้ ฟังค์ชัน date กับ status ใน Order