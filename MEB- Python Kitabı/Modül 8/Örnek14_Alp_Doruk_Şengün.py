import turtle
kalem=turtle.Turtle()
kalem.shape("turtle") # kalemin şekli kaplumbağaya döner.
for i in range(4): # 4 defa döngü sürer.
 kalem.up()#kalemi kaldırır.
 kalem.forward(20)# 20 birim ilerler.
 kalem.dot()# nokta koyar.
 kalem.down()# kalem çizmeye başlar.
 kalem.forward(20)#20 birim ilerler.
 kalem.dot()#nokta koyar.
turtle.done()