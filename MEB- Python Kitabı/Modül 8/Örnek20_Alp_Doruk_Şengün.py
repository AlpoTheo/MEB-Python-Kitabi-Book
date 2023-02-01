import turtle
def desen_çiz (kenar_uzunluğu=50, iç_kenar=3, tur_sayısı=3):#fonksiyon yazılır.
  if(tur_sayısı<1 or iç_kenar<3):
    print("Hatalı veri girdiniz.")
  else:
    kalem=turtle.Turtle()
    for i in range(tur_sayısı):#tur_sayısı kadar döngü döner.
      for j in range(iç_kenar):# iç_kenar kadar döngü döner.
        kalem.forward(kenar_uzunluğu)#kenar_uzunluğu birim ilerler.
        kalem.left(360/iç_kenar)# 360/iç_kenar derece sola döner.
      kalem.left(360/tur_sayısı)#360/tur_sayısı derece sola döner.
desen_çiz()#fonksiyon kullanılır.
desen_çiz(60,4,5)#fonksiyon kullanılır ve işlem yapılır.
desen_çiz(70,6,10)#fonksiyon kullanılır ve işlem yapılır.
turtle.done()