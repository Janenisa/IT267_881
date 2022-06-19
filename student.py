class Student: #เรากำหนดชื่อ Class ตัวใหญ่เสมอ ช่อง 1
    def __init__(self,id :str,name:str,major="IT") -> None: #คือเราอยากได้ค่าอะไรบ้างอยู่ในช่อง 2 ที่ major="IT" คือเรากำหนดค่าเริ่มต้นไว้ก่อนถ้าเวลาprint เช่นชื่อ James มันจะเติมอัตโนมัติ
        self.id = id
        self.name = name
        self.major = major
     
    def Printdisplay_detail(self): #คือเรากำหนดชื่อฟังค์ชัน Printdisplay_detail(self)
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"major: {self.major}")

    def __del__(self):
        print("Object was destroyed") #ใช้คำนี้เสมอ

if __name__=="__main__":
    Jessica = Student(111,"Jessica","IT") 
    Jessica.Printdisplay_detail()

    John = Student(112,"John","MKT")
    John.Printdisplay_detail() #ใส่วงเล็บเสมอ หลัง . ให้ใส่ชื่อ ในบรรทัดที่ 7 มันคือการเรียกใช้
    
    James = Student(113,"James")
    James.Printdisplay_detail()