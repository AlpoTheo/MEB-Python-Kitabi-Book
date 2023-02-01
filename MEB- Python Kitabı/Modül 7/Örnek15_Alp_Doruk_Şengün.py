topla=0
def toplamBul (sayiListesi): #fonksiyon şimdi çağırılabilir oldu.
 topla=0
 for i in range (len(sayiListesi)):
    topla+=sayiListesi[i]
 return topla  # global bir değişken yazılarak önceki örnekteki hata giderilmiş oldu.