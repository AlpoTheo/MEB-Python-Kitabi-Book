import turtle
kalem=turtle.Turtle()
mesafe=float(input("çizgi mesafesini giriniz")) #mesafe ye değişken atanır.
kalem.forward(mesafe) # mesafe kadar ileri gider.
kalem.right(90) # 90 derece sağ döner.
kalem.forward(mesafe)# mesafe kadar ileri gider.
turtle.done()#çizimin ekranda kalmasını sağlar.