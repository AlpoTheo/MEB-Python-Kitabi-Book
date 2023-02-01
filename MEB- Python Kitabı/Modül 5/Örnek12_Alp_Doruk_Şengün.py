liste = [1,2,3,4,5,6,7,8,9,10] # liste tanımlanır.
print(liste)
# 1. eleman ekrana yazdırır.
print(liste[0])
# 6. eleman ekrana yazdırır.
print(liste[5])
# Baştan 5. indekse kadar (dahil değil)
print(liste[:5])
# 1.indisten 5.indise kadar belirten kod aşşağıda belirtildiği gibi kullanılabilir. Ekrana yazdırır.
print(liste[1:7])
print(liste[5:]) # listede 6. eleman ve 6. elemandan sonrakileri ekrana yazdırır.


print(liste[::2]) # ilk liste elemanından 1 er 1 er eleman atlayarak liste de ilerler. Ekrana yazdırır.