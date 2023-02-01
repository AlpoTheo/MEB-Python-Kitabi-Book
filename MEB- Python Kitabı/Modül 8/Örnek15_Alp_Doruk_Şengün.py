import turtle
kalem=turtle.Turtle()
kalem.pencolor("red")#kalemin rengini kırmızıya çevirir.
kalem.pensize(3)# kalemin kalınlığını 3 e alır.
for i in range(4): # 4 kere döngü yapar.
 kalem.forward(100)# 100 birim ilerler.
 kalem.left(90)# 90 derece sola döner.
turtle.done()