#มีวิธีนี้วิธีเดียว ใช้ mobj
from secrets import choice
from pip import main
from measure import Measure

if __name__ == '__main__':
    mobj = Measure()
    #ให้ User เลือกได้ว่าอยากได้เป็น inch หรือ cm กำหนดเป็นเลขให้มัน
    choice = input('Chooose menu to convert (1: inch, 2:cm):')
    #รับค่าตัวเลขจาก User ได้ว่าต้องการใช้เป็นเลขตัวไหน
    number = float(input('Enter number: '))
    
    if choice == '1': #1 ต้องใส่ '' เพราะเป็นการรับค่าที่เป็นอักษรไม่ถือเป็นเลข
        print(f'{number} cm = {mobj.cm_inch(number):,.2f} inch')
    elif choice == '2':
        print(f'{number} inch = {mobj.inch_cm(number):,.2f} cm ')
    else:
        print ('Choose wrong menu')

    

#print(f'(5.5) cm = {mobj.cm_inch(5.5):,.2f} inch')
#print(f'(47) inch = {mobj.inch_cm(47):,.2f} cm ')