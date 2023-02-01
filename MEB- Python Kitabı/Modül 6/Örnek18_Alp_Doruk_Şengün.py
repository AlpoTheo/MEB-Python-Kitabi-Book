sayılar = [1,2,3,4,5,6,7,8,9]#liste tanımlanır.
toplam=0
for i in sayılar:# sayılar listesinin karakterleri for döngüsüne alınarak i değişkenine atanır.
 toplam=toplam+i #toplam değişkenine i değişkeni eklenerek toplam değişkenine atanır.
print("sayıların ortalaması: ",toplam/len(sayılar))# toplam değişkeni ve sayılar listesindeki karakter uzunluğu birbirine bölünür ve ekrana yazılır.