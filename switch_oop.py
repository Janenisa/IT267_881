class Switch():#คือการตั้งชื่อ Class ให้กับมันเพื่อเป็นต้นแบบ
    def __init__(self) -> None:
        self.switch_status = False

    def turnon(self):
        self.switch_status = True

    def turnoff(self):
        self.switch_status = False

    def show_status(self):#ตรวจสอบ Class
        if (self.switch_status): #ใช้ self.switch_status ตามชื่อให้มี self ข้างหน้า
            print(f"ไฟเปิด")
        else:
            print(f"ไฟปิด")

#การสร้าง วัตถุ (Object)
sobj = Switch() #sobj=Switchobject

if __name__ == "__main__":
    sobj.show_status()
    sobj.turnon()
    sobj.show_status()
    sobj.turnoff()
    sobj.show_status()
    sobj.turnoff()
    sobj.show_status()
    sobj.turnoff()
    sobj.show_status()






