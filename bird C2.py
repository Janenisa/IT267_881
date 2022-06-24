class Bird:
    global bird_type #ถ้าไม่ใส่ global จะกลายเป็น Class variable ทันที
    bird_type = 'parrot'
    bird_name = 'Lori' #เป็น Class variable
    def __init__(self,color) -> None: 
        self.color = color
        name = 'Peter'
        print(f'{name} in init') 

if __name__=='__(main)__':
    my_bird = Bird('Green,Blue')

    #call instance variable ชื่อวัตถุ.instance_variable
    print(my_bird.color)

    #call class variable ชื่อวัตถุ.class_variable
    print(Bird.bird_name)

    #class glibal variable
    print(bird_type)

    #error
    #พยายามเรียก local variable
    #print(name)  #์Name : name 'name' is not defined
    
    #พยายามเรียก global variable
    #print(Bird.bird_typt)
    #type object 'Bird' has no attribute 'bird_type'