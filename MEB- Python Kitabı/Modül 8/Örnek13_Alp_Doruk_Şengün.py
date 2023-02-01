import turtle
kalem=turtle.Turtle()
kalem.shape("turtle")#kalemin şekli kaplumbağaya döner.
kalem.forward(100)# 100 birim ileri gider.
kalem.penup()#kalemi kaldırır.
kalem.goto(0,100) # 0,100 noktasına gider.
for i in range(5):#5 defa 20 birimde bir nokta koyar.
 kalem.dot()
 kalem.forward(20)
turtle.done()