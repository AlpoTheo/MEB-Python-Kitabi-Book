"""""""""""""""""""""""""""""""""""""""""""""""
Resimlerde gösterilen şekilleri çizecek Python kodlarını yazınız.

1.
import turtle
yıldız = turtle.Turtle()
for i in range(5):
 yıldız.forward(100)
 yıldız.right(144)
turtle.done()
----------------
2.
import turtle
yıldız = turtle.Turtle()
for i in range(20):
 yıldız.forward(i * 10)
 yıldız.right(144)
turtle.done()
----------------
3.
import turtle
yıldız = turtle.Turtle()
for i in range(50):
 yıldız.forward(100)
 yıldız.right(123)
turtle.done()
----------------
4.
import turtle
kalem = turtle.Turtle()
kalem.penup()
for y in range(4):
 for i in range(4):
 kalem.dot()
 kalem.forward(20)
 kalem.backward(80)
 kalem.right(90)
 kalem.forward(20)
 kalem.left(90)
turtle.done()
---------------
5.
import turtle
kalem = turtle.Turtle()
for y in range(4):
 kalem.down()
 kalem.dot()
 for i in range(4):
 kalem.forward(20)
 kalem.dot()
 kalem.up()
 kalem.backward(80)
 kalem.right(90)
 kalem.forward(20)
 kalem.left(90)
turtle.done()
---------------
6.
import turtle
kalem = turtle.Turtle()
kalem.color("blue")
for k in range(5,106,25):
 print(k)
 for i in range(4):
 kalem.forward(k)
 kalem.left(90)
turtle.done()
----------------

"""""""""""""""""""""""""""""""""""""""