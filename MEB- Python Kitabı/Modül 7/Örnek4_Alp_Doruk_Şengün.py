def asalMi(sayi):
 sayac=2 # tüm sayılar 1'e bölüneceğinden 2 ile başlattık
 while sayac<=int(sayi/2): # işlemler yapılır döngü başlar.
    if sayi%sayac==0: #sayi sayac a kalansız bölünüyorsa girintiden devam edilir.
        return False # return fonksiyondan dışarı değer döndürmeye yaramaktadır. ancak false olduğu için engellenir.
 sayac+=1 # sayac +1 eklenir.
 return True
#Fonksiyonu çağırma
asalMi(113) 