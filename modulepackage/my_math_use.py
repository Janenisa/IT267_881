#วิธีที่ 1 การเรียกโดยใช้ from
from my_math import sqrt,circle_area #คือการที่เรานำ my_math เข้ามาใช้

print(f'sqart of 5 = {sqrt(5)}')
print(f'circle area = {circle_area(2):,.2f}')

#วิธี 2 ใช้การ import ตามด้วยชื่อ MOdule
import  my_math as my
print ("*****วิธีที่ 2*****")

print(f'sqart of 5 = {my.sqrt(5)}')
print(f'circle area = {my.circle_area(2):,.2f}')
