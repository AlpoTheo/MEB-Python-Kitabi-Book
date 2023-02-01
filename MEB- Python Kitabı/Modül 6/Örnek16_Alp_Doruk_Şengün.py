sesli_harfler = "aeıioöuü"
sessiz_harfler = "bcçdfgğhjklmnprsştvyz"
sesliler=""
sessizler=""
a=input("bir metin giriniz")# a değişkeni tanımlanır.
for i in a: # a değişkeni içerisindeki karakterler for döngüsüne alınarak i değişkenine atanır.
 if i in sesli_harfler: # i değişkeninin içersinde bulunan karakterler sesli_harfler karakterleriyle örtüşürse girintili kısımdan devam edilir.
    sesliler=sesliler+i # sesliler değişkenine +1 eklenir.
 if i in sessiz_harfler:# i değişkeninin içersinde bulunan karakterler sessiz_harfler karakterleriyle örtüşürse girintili kısımdan devam edilir.
    sessizler=sessizler+i #sessizler değişkenine +1 eklenir.
print("sesli harfler",sesliler) # sesliler ekrana yazılır.
print("sessiz harfler",sessizler) #sessizler ekrana yazılır.