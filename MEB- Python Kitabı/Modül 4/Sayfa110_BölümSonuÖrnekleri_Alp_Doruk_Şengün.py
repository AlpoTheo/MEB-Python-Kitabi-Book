"""""""""""""""""""""
1.  Kullanıcının girdiği tam sayının “Negatif”, “Pozitif” ya da “Sıfır” olduğunu yazdıran programın kodlarını yazınız

cevap=
sayi = input('Sayı : ')
if(int(sayi)<0):
 print("Sayı Negatif")
elif(int(sayi)>0):
 print("Sayı Pozitif")
else:
 print("Sayı Sıfır")
 -------------------------------
 2.  Öğrencinin sınav ortalamalarını kullanıcıdan alan ortalama en az 50 ise geçti değilse kaldı yazan programı yapınız.

cevap=
ort = input('Ortalamanızı Girin : ')
if(int(ort)>=50):
 print("Geçtiniz")
else:
 print("Kaldınız")
 -------------------------------
 3.   Kullanıcın girdiği iki sayıyı karşılaştırarak sayı sayıdan büyüktür, küçüktür veya sayılar eşittir mesajı veren kodları sadece “if” koşul yapısını kullanarak yazınız.

cevap=
sayi1= int(input('1. sayıyı giriniz: '))
sayi2= int(input('2. sayıyı giriniz: '))
if sayi1>sayi2:
 print('1. sayı 2. sayıdan büyüktür.')
if sayi1<sayi2:
 print ('1.sayi 2. sayıdan küçüktür.')
if sayi1==sayi2:
 print ('Sayılar eşittir.')
 --------------------------------
 4.   Yukarıdaki programı “if-elif-else” koşul yapısını kullanarak yazınız.
 
 cevap=
 sayi1= int(input('1. sayıyı giriniz: '))
sayi2= int(input('2. sayıyı giriniz: '))
if sayi1>sayi2:
 print('1. sayı 2. sayıdan büyüktür.')
elif sayi1<sayi2:
 print ('1.sayi 2. sayıdan küçüktür.')
else: print ('Sayılar eşittir.')
--------------------------------
5.    Aşağıdaki kodun çıktısı ne olur?
sayi1=12
sayi2=60
toplam=0
if sayi1<=sayi2:
 if sayi1%2==0:
 sayi1=sayi2
 toplam=sayi1+sayi2
 else: toplam=sayi2-sayi1
toplam+=toplam
print(toplam)

cevap=
240
-------------------------------
6.    Yukarıdaki kodda sayi1=40 sayi2=13 değerleri için kodun çıktısı kaç olur?

cevap=
1
-------------------------------
7.    Kullanıcıdan (1-4) arasında sayı alınacak, bu sayıya göre sırasıyla İlkbahar-yaz-sonbahar-kış yazan programın kodlarını yazınız.

cevap=
a=int(input("Mevsim No:"))
if(a==1):
 print("İlkbahar")
elif(a==2):
 print("Yaz")
elif(a==3):
 print("Sonbahar")
elif(a==4):
 print("Kış")
else: print("Aralıkta olmayan bir değer girdiniz")
------------------------------
8.     Kullanıcıdan alınan dört kenar uzunluğuna göre şeklin kare, dikdörtgen veya diğer dörtgenlerden olduğunu belirten kodu yazınız.

cevap=
a=int(input("1. kenar:"))
b=int(input("2. kenar:"))
c=int(input("3. kenar:"))
d=int(input("4. kenar:"))
if(a==b==c==d):
 print("Kare!")
elif(a==c and b==d or a==b and c==d ):
 print("Dikdörtgen")
else: print("Diğer Dörtgen")
------------------------------
9.     Kenar uzunlukları girilen üçgenin çeşidini bulan programın kodlarını yazınız.

cevap=
a=int(input("1. kenar:"))
b=int(input("2. kenar:"))
c=int(input("3. kenar:"))
if(a!=b and a!=c and b!=c):
 print("Çeşitkenar Üçgen!")
elif(a==b==c):
 print("Eşkenar Üçgen!")
else: print("İkizkenar Üçgen")
------------------------------
10.     Beden kitle endeksini kilo/(boy**2) formülü ile hesaplanarak bireyin kilo durumunu kontrol eden programın kodlarını aşağıdaki aralık durumlarına göre yazınız.

cevap=
boy = float(input("Boy: Örnek 1.73----:"))
kilo = float(input("Kilo: Örnek: 78.40----:"))
endeks = kilo/(boy**2)
if endeks<18.5:
 print("Zayıfsınız")
elif endeks > 18.5 and endeks <=25 :
 print("Normalsiniz")
elif endeks > 25 and endeks <=30:
 print("Kilolusunuz")
elif endeks > 30:
 print("Dikkat! obez")
 ----------------------------
































"""""""""""""""""""""""""""