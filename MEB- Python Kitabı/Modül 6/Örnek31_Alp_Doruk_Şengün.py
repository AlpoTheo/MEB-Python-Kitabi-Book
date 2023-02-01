i=0
while i < 5: # i değişkeni 5 den küçük olduğu sürece döngü devam eder.
 i=i+1 #i değişkenine +1 eklenir.
 if i == 2 or i==4: # i değişkeni 2 veya 4 olduğu zaman girintili kısımdan devam edilir.
    continue #döngüyü başa alır.
 print(i)