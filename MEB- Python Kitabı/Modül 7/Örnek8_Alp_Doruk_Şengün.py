def ortalamaBul(sayilar): # fonksiyon tanımlanır.
 sayilarinToplami=0
 sayilarinOrtalamasi=0
 for i in range(len(sayilar)):
    sayilarinToplami+=sayilar[i]
    sayilarinOrtalamasi=sayilarinToplami/len(sayilar)
    return sayilarinOrtalamasi

sayiAdedi=int(input('Kaç adet sayının ortalamasını alacaksınız: '))
sayilarim=[] # liste tanımlanır.
for i in range(0,sayiAdedi):
 print (i+1, '. sayıyı giriniz?') 
 # indis sıfırdan başladığı için +1 kullanırız.
 sayi=int(input())
 sayilarim.append(sayi) #sayilarım listesine sayi listesinden eleman eklenir. .append ile
ortalamaBul(sayilarim) # fonksiyon çağırılır ve işlem yapılır.