import turtle
kalem=turtle.Turtle()
kalem.color("green")#kalemin rengi yeşil olur.
for i in range (6):# döngü 6 kez tekrarlanır.
 for j in range (6):#döngü 6 kez tekrarlanır.
    kalem.forward(50)# 50 birim ilerlenir.
 kalem.left(60) # iç döngü , 60 derece sola döner
 kalem.left(60)# dış döngü , 60 derece sola döner.
turtle.done()