from turtle import Turtle
from random import randint

#สร้าง Object
leo = Turtle()
leo.color("blue")
leo.shape("turtle")
leo.penup()
leo.goto(-160,100)
leo.pendown()

dona = Turtle()
dona.color("purple")
dona.shape("turtle")
dona.penup()
dona.goto(-160,70)
dona.pendown()

raph = Turtle()
raph.color("red")
raph.shape("turtle")
raph.penup()
raph.goto(-160,40)
raph.pendown()

mike = Turtle()
mike.color("orange")
mike.shape("turtle")
mike.penup()
mike.goto(-160,10)
mike.pendown()


for movement in range(100):
    leo.forward(random(1,5)) #ให้ลีโอวิ่ง 5 ก้าวไปข้างหน้า
    dona.forward(random(1,5))
    raph.forward(random(1,5))
    mike.forward(random(1,5))