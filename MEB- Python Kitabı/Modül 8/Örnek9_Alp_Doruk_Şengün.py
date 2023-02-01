import turtle
kalem=turtle.Turtle()
mesafe=int(input("çizgi mesafesini giriniz")) #mesafe ye değişken atanır.
donus_açısı=int(input("dönüş açısını giriniz"))# donus_açısı ya değişken atanır.
kalem.forward(mesafe) #mesafe kadar ileri gider.
kalem.right(donus_açısı)# donus_açısı kadar sağ döner.
kalem.forward(mesafe)#mesafe kadar ileri gider.
turtle.done()#çizimin ekranda kalmasını sağlar.