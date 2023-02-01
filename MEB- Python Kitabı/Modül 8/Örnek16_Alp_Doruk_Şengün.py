import turtle
kalem=turtle.Turtle()
kalem.pencolor("blue")# kalemin rengini mavi yapar.
kalem.pensize(3)# kalemin kalınlığını 3 e alır.
for i in range(6): # 6 kere döngü döner.
 kalem.forward(100)# 100 birim ilerler.
 kalem.left(60)# 60 derece sola döner.
turtle.done()