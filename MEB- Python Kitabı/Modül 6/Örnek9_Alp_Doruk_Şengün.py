Sayi=45
sayaç=0
print("1-100 arası bir sayı tuttum tahmin et")
while 1==1:
    sayaç+=1 # sayac a her döngüde +1 eklenir.
    cevap=int(input("1-100 arası bir sayı girin: ")) # Cevap değişkeni atanır.
    if cevap>Sayi: # cevap Sayi dan büyükse girintili kısımdan devam edilir.
        print("daha küçük bir sayı girmelisin")
    elif cevap<Sayi: # cevap Sayi dan küçükse girintili kısımdan devam edilir.
        print("daha büyük bir sayı girmelisin")
    else: # değilse buradaki girintili kısımdandan devam edilir.
        print("tebrikler tuttuğum sayıyı bildin")
        break
print("tebrikler {} seferde sayıyı bulabildin".format(sayaç)) # sayac her seferde kaçıncı kez denediğini ölçerek ekrana yazdırır.