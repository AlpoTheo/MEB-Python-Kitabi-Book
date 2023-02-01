import turtle
kalem=turtle.Turtle()
kalem.up()#kalemi kaldırır çizmez.
for i in range(5):# 5 defa 20 birimde bir nokta bırakır ve ok çizer.
 kalem.dot()
 kalem.forward(20)
turtle.done()