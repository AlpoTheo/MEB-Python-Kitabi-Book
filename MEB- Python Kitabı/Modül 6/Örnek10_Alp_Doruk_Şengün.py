i=1
f=int(input("faktöriyeli alınacak sayıyı giriniz: ")) # f ye değer atanır.
sonuc=1
while i<=f: # i değişkeni f ye eşit ya da küçükse girintili kısımdan devam edilir.
 sonuc=sonuc*i # sonucla i nin çarpımı sonuc a atanır.
 i+=1 # i değişkenine +1 eklenir ve döngü sağlanır.
print(sonuc) # sonuc ekrana yazdırılır.