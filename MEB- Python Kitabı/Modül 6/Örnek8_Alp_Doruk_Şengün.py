liste=[] #liste tanımlanır.
while 1: #while 1 yani true döngüsü sağlanır.
    ürün=input("ürün adı giriniz:") # ürün değişkenine değer atanır.
    if ürün=="q": # ürün q ya eşit olursa girintili kısımdan devam edilir.
        break  # döngü kırılır
liste.append(ürün) # .append listeye eleman ekler.
print("girdiğiniz meyveler:",liste)