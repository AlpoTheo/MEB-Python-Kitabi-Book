def toplamBul (sayiListesi): #fonksiyon tanımlanır.
 toplam=0
 for i in range (len(sayiListesi)):
    topla+=sayiListesi[i]
 return topla # fonksiyonlar içinde tanımlanmış değişkenler yerel (lokal) değişkenler olduğu için fonksiyon çağrılmazsa hata ile karşılaşılır. Nameerror alınır.
print (topla)