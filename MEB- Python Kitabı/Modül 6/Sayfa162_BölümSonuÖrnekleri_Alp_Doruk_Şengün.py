"""""""""""""""""""""""""""
1. Girilen sayının asal olup olmadığını bulan programı yazınız.

cevap=
a=int(input("bir sayı giriniz"))
asal=0
for i in range (2,a):
 if a%i==0:
 asal+=1
if asal==0:
 print("girdiğiniz sayı asal")
else:
 print("girdiğiniz sayı asal değil")
 --------------------------------------------
 2. Kullanıcıdan değer alarak ağaç şekli çizen programı yazınız.
 
 cevap=
 a=int(input("ağacın yükseliği"))
b=a
for i in range(1,a+1):
 print(b*" ",(2*i-1)*"*")
 b-=1
 --------------------------------------------
 3. Bir listede bulunan sayıların en büyüğünü ve en küçüğünü bulan programı yazınız.
 
 cevap=
 liste=[5,9,7,1,2,3,6,4]
buyuk=0
kucuk=999
for i in range(len(liste)):
 if liste[i]>buyuk:
 buyuk=liste[i]
 if liste[i]<kucuk:
 kucuk=liste[i]
print(""girilen sayıların en büyüğü= {} girilen sayıların en küçüğü= {}"".format(buyuk,kucuk))
---------------------------------------------
4. Elinizde bulunan iki adet listeyi birleştirerek 3. oluşturan programı yazınız.

cevap=
liste1=[1,2,3,4,5,6,7]
liste2=["python","java","c","c++","c#","pascal","cobol"]
liste3=[]
for i in range(len(liste1)):
 liste3.append((liste1[i],liste2[i])) #.append listeye ekler.
print(liste3)
---------------------------------------------
5. Bir cümledeki boşlukları kaldıran programı yazınız.

cevap=
a="m e r h a b a"
for i in a:
 if i!=" ":
    print(i,end="")
---------------------------------------------


"""""""""""""""""""""""""""""




 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
