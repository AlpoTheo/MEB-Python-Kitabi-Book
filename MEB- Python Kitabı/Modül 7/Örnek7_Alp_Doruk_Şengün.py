def faktoriyelAl(sayi): #fonksiyon tanımlanır.
 sonuc=1
 if (sayi==0 or sayi==1): # sayi 0 veya 1 e eşitse girintili kısımdan devam edilir.
    sonuc=1
 elif sayi>1: #sayi 1 den büyükse girintili kısımdan devam edilir.
    for i in range(1, sayi+1, 1): # 1 ile sayi+1 arasındaki sayıları alarak for döngüsünde i değişkenine tanımlarız.
        sonuc*=i
 else: sonuc=-1 #hatalı bir işlem olduğunu anlamak için -1 değerini veririz.
 return sonuc