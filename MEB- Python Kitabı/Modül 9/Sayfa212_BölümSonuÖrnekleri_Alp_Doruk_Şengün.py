""""""""""""""""
1.   5 ve 6 elemanlı olacak şekilde iki adet demet tanımlayınız. Bu iki adet demeti önce birleştirip sonra eleman sayılarını bulan programı yapınız.

cevap=
aylar =("ocak","şubat","mart","nisan","mayıs","haziran")
mevsimler = ("kış","ilkbahar","yaz","sonbahar")
yeni_demet=tuple(mevsimler+aylar)
print(len(yeni_demet))
----------------------------------
2. Sayilar=(20,24,25,79,40,39,50) demet olarak tanımlanmıştır. Bu demet’te 5’e bölünenleri ekrana yazdıran programı yapınız.

cevap=
sayilar=(20,24,25,79,40,39,50)
for meyve in sayilar:
if meyve%5 ==0:
print(meyve)
----------------------------------
3. Aşağıdaki kod çalıştırıldığında ekran çıktısı nedir?
demet = ("hasan","ali","c","mehmet","deniz","f","fatma")
yenidemet = demet[3:5]
print(yenidemet)

cevap=
('mehmet', 'deniz')
----------------------------------
4. Uygulama=("ali","veli","ayşe","Fatma","Hayriye","ali","deniz") şeklinde tanımlanmış bir demet’te ali adlı öğenin kaç adet olduğunu bulunuz.

cevap=
uygulama=("ali","veli","ayşe","Fatma","Hayriye","ali","deniz")
print(uygulama.count("ali"))
----------------------------------
5. Aşağıdaki kod çalıştırıldığında ekran çıktısı nedir?
sozluk = {'renk': 'mavi', 'kıyafet': 'pantolon', 'beden': 'M'}
for anahtar in sozluk:
print(anahtar)

cevap=
renk
kıyafet
beden
----------------------------------
6. Aşağıdaki kod çalıştırıldığında ekran çıktısı nedir?
sozluk = {'renk': 'mavi', 'kıyafet': 'pantolon', 'beden': 'M'}
for anahtar in sozluk:
 print(anahtar,sozluk[anahtar])
sozluk_bilesenleri=sozluk.items()
for bilesen in sozluk_bilesenleri :
print(bilesen)
print(type(bilesen))# demet veri tipinde oluyor

cevap=
renk mavi
kıyafet pantolon
beden M
('renk', 'mavi')
<class 'tuple'>
('kıyafet', 'pantolon')
<class 'tuple'>
('beden', 'M')
<class 'tuple'>
---------------------------------

"""""""""""""""
