class Bird:
    global bird_type #global variable
    #ถ้าไม่ใส่คำว่า global ตัวแปร bird_type จะกลายเป็น class variable
    bird_type = 'parrot'
    bird_name = 'Lori' #class variable
    
    def __init__(self,color) -> None:
        self.color = color #instance variable
        name = 'Peter' #local variable
        print(f'{name} in init') #call local variable

if __name__ == '__main__':
    my_bird = Bird('Green,Blue')

    #call instance variable ชื่อวัตถุ.instance_variable
    print(my_bird.color)

    #call class variable ชื่อคลาส.class_variable
    print(Bird.bird_name)

    #call global variable เรียกชื่อตัวแปรได้เลย
    print(bird_type) 

    #error
    #พยายามเรียก local varibale
    #print(name)#NameError: name 'name' is not defined
    
    #พยายามเรียก global varibale ผ่าน class
    #print(Bird.bird_type)
    #type object 'Bird' has no attribute 'bird_type'.