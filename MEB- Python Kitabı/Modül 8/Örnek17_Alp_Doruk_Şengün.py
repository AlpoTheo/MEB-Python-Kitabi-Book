import turtle
kalem=turtle.Turtle()
kalem.pencolor("red")#kalemin rengi kırmızı olur.
kalem.pensize(3)# kalemin kalınlığı 3 e alınır.
kenar_sayısı=int(input(" çizmek istediğiniz çokgenin kenar sayısını giriniz")) #kenar_sayısı değişkeni atanır.
for i in range(kenar_sayısı):# kenar_sayısı kadar döngü döner.
 kalem.forward(50)# 50 birim ileri ilerler.
 kalem.left(360/kenar_sayısı)# 360/kenar_sayısı kadar derece sola döner.
turtle.done()