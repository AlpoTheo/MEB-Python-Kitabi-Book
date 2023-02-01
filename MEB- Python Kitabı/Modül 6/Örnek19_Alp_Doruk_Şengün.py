sayılar = [5,8,12,17,25,36,41,49,60,72]#liste tanımlanır.
for i in sayılar:# sayılar listesi for döngüsüne alınarak i değişkenine atanır.
 if i%3==0: # i listesinin içersindeki sayılardan 3 e tam bölünen sayılar girintili kısımdan devam ederler.
    print(i,end=",")