"""""""""""""""""""""""""""
1. Vize, final puanlarını ve yüzdelik oranlarını parametre olarak alan ve puanlar ile yüzdelik oranları 
çarparak toplayan ve sonucu döndüren bir fonksiyon tanımlayınız ve (50, 60, 30, 70) argümanlarıyla fonksiyonunuzu kullanınız. kullanın. Sonuç sizce kaç olur?

cevap=
def puanHesaplama (vizePuani, finalPuani, vizeYuzdesi, finalYuzdesi):
 return(vizePuani*vizeYuzdesi/100+finalPuani*finalYuzdesi/100 )
puanHesaplama(50, 60, 30, 70)
---------------------------------------
2. Bir liste halinde verilen sayılardan tek olanların toplamını döndüren bir fonksiyon yazınız. [1, 2, 3, 
4, 5, 6, 7, 9, 11, 1773, 1679] sayı listesiyle deneyiniz. Sonuç sizce kaç olur?

cevap=
def tekSayilariTopla(sayilar):
 sayilarinToplami=0
 for i in range(len(sayilar)):
 if sayilar[i]%2!=0:
 sayilarinToplami+=sayilar[i]
 return sayilarinToplami
tekSayilariTopla([1, 2, 3, 4, 5, 6, 7, 9, 11, 1773, 1679])
---------------------------------------
3. Aşağıdaki kodun ekran çıktısı sizce nasıl olur?
karsilamaMesaji='Merhaba'
kullaniciYasi=35
dogumGunuMu=True
if kullaniciYasi==35 and dogumGunuMu==True:
 karsilamaMesaji1='Yolun yarısı'
 kullaniciYasi+=1
 print(dogumGunuMu)
dogumGunuMu=False
print (kullaniciYasi)
print(dogumGunuMu)
print(karsilamaMesaji)


cevap=
True
36
False
Merhaba
---------------------------------

"""""""""""""""""""""""""""""""""""""""