import pstats


switch_status = False #ตั้งต้นสถานะให้เริ่มต้นไฟปิด 

def turnon(): #การกำหนดตัวแปรฟังก์ชันเปิดไฟ
    global switch_status #คือการประกาศว่าตัวแปร switch_status นี้สามารถใช้ได้ทั้งโปรแกรม
    switch_status = True #คือการเปิดไฟเพราะเราตั้งต้นว่าให้มันปิดเมื่อกดเปิดจะเป็น True
    print("ไฟเปิด")
def turnoff(): #การกำหนดตัวแปรฟังก์ชันปิดไฟ
    global switch_status #คือการประกาศว่าตัวแปร switch_status นี้สามารถใช้ได้ทั้งโปรแกรม
    switch_status = False #คือการปิดไฟเพราะเราตั้งต้นว่าให้มันปิดเมื่อกดปิดจะเป็น False
    print("ไฟปิด")

if __name__ == "__main__": #คือถ้าเรารันอันนี้เป็นหลักการเทสแต่ละ Module 
    print(f'สถานะไฟ : {switch_status} ') #คือการเรียกปริ้นสถานะไฟ
    turnon() #คือการเรียกใช้ฟังค์ชัน turnon() ไฟเปิด
    turnoff() #คือการเรียกใช้ฟังค์ชัน turnoff() ไฟปิด

    