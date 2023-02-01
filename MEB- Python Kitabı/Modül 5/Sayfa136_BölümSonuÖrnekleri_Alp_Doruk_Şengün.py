"""""""""""""""""""""""""""""""""
1.   Harfler adıyla bir liste oluşturup içine ‘a’, ‘e’, ‘i’, ‘o’, ‘i’, ‘u’ elemanları kaydediniz. Bu listede i ve p harflerinin sayısını ekrana yazdırınız.

cevap=
harfler = ['a', 'e', 'i', 'o', 'i', 'u']
count = harfler.count('i')
print('i harflerinin sayısı:', count)
count = harfler.count('p')
print('p harflerinin sayısı:', count)
---------------------------------------------------
2.    Liste1, liste2, liste3 ve liste4 adında dört adet liste oluşturup aynı satırda olacak şekilde tanımlayıp, her bir listeye birer adet eleman girip listeleyiniz.

cevap=
liste1,liste2,liste3,liste4= ['a',100,3.14,'python']
print(liste1)
print(liste2)
print(liste3)
print(liste4)
---------------------------------------------------
3.     İki adet liste tanımlayarak bu iki listeyi “+” operatörü ile toplama işlemi yaptırılıp, üçüncü bir listeye atama işlemini yapınız. Son listeyi ekrana yazdırınız.

cevap=
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
---------------------------------------------------
4.     Aşağıdaki listeyi hem küçükten büyüğe hem de büyükten küçüğe doğru sıralanacak şekilde ekrana listeleyiniz. 
liste = [34,1,56,334,23,2,3,19]

cevap=
liste = [34,1,56,334,23,2,3,19]
liste.sort()
print('küçükten büyüğe doğru',liste)
liste.reverse()
print('büyükten küçüğe doğru',liste)
---------------------------------------------------
5.      Aşağıdaki kodları verilen liste örneğinde ekran çıktısını yazınız.
listem= ["Merhaba", "Türkiye", "Nasılsın", "Tebrikler"]
print(listem[-1])
print(listem[-3])
print(listem[-4])

cevap=
Tebrikler
Türkiye
Merhaba
---------------------------------------------------
6.     Aşağıdaki örnekte liste tanımlanmış ve ekran çıktısı verilmiştir. Ekran çıktısının aşağıdaki gibi olması için boş kalan kısımları tamamlayınız.
liste = [1, 2, 3, 4, 5, 6, 7]

cevap=
liste = [1, 2, 3, 4, 5, 6, 7]
print(liste[1:3])
print(liste[:3])
print(liste[3:])
print(liste[:])
--------------------------------------------------
7.      Aşağıda verilen örnekte boş kalan kısımları doldurunuz.
isimler = ['ali','veli','ayşe']
……………………………………………………..
ad_soy1 = isimler[0] +' '+ soyisimler[0]
……………………………………………………………
ad_soy3 = isimler[2] +' '+ soyisimler[2]
print(ad_soy1)
………………………….
print(ad_soy3)

cevap=
isimler = ['ali','veli','ayşe']
soyisimler = ['türk','izci','erel']
ad_soy1 = isimler[0] +' '+ soyisimler[0]
ad_soy2 = isimler[1] +' '+ soyisimler[1]
ad_soy3 = isimler[2] +' '+ soyisimler[2]
print(ad_soy1)
print(ad_soy2)
print(ad_soy3)
--------------------------------------------------
8.      liste = ['bir','iki','dört']
print(liste)
['bir', 'iki', 'dört'] şeklinde ekran çıktısı olmaktadır. Ama ['bir', 'iki', 'üç','dört', 'beş'] olacak şekilde listeyi güncelleyiniz.

cevap=
liste = ['bir','iki','dört']
liste[2]='üç'
liste.insert(3,'dört')
liste.insert(4,'beş')
print(liste)
-------------------------------------------------
9.     Aşağıdaki listede listenin ilk ve son verilerine ulaşmak ve listelemek için gerekli kodları yazınız.
liste=["birinci veri", "ikinci veri", "üçüncü veri ", "dördüncü veri","beşinci veri"]

cevap=
liste=["birinci veri","ikinci veri","üçüncü veri ","dördüncü veri","beşinci 
veri"]
#beş elemanlı listenin ilk verisi
print(liste[0])
#beş elemanlı listenin son verisi
print(liste[4])
-------------------------------------------------






























""""""""""""""""""""""""""""""""""