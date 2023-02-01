yazi="Python üst düzey basit sözdizimine sahip, öğrenmesi oldukça kolay,modülerliği, okunabilirliği desktekeyen, platform bağımsız nesne yönelimli yorumlanabilir bir script dilidir."
harf="a"
sayac=0
for i in yazi: #yazi içerisindeki karakterler for döngüsüne alınarak i değişkenine atanır.
 if i=="a": # i değişkeni a ya eşitse girintili kısımdan devam edilir.
    sayac=sayac+1 # sayac a her seferde +1 değeri eklenir.
print("cümle içerisinde geçen a harfi sayısı: ",sayac) # cümle içersinde geçen a harfi sayısı ekrana yazdırılır.