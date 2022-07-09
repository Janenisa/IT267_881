#สร้างพนักงานของ IT
from empit import EmpIT
mike = EmpIT('001','Mike',60000)
mike.add_skill('Python,JavaScript')
mike.add_experience(5)
mike.emp_detail()
#mike.it_salary()

from empmkt import Empmkt
anna = Empmkt('002', 'Anna', 35000)
anna.emp_detail()
anna._emp_salary()

#jess 003 เงินเดือน 45000 ทำงานอยู่ที่ Chiang Mai คอมมิชชั่น 35%
jess = Empmkt('003', 'Jess', 45000)
jess.add_location ('Chiang Mai') #เปลี่ยนโลเคชั่นเลยเลือกตั้งต้นว่าเป็น Bangkok เราต้องเปลี่ยนเป็น Chiang Mai
jess.add_commission(35)  #เปลี่ยนค่าคอมมิชชั่นเป็น 35%
jess.emp_detail #เรียกดู ดีเทล
jess._emp_salary