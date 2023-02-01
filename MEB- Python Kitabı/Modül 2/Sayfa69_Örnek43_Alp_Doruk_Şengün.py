# is operatörü iki değerin eşit olup olmadığını kontrol etmek için kullanılır. Değerler eşitse “True” değilse “False” değerini döndürür.
sayi1=5
print (sayi1 is 5) # sayi1 in değeri 5 değeri ile aynıysa True değilse False değerini ekrana yazdırır.
print (sayi1 is not 5) #is operatörünün tersini verir.

# “is” operatörü karakter dizisinde de kullanılabilir.
print ('elif' is 'Elif') # Büyük küçük harf duyarlılığından dolayı False çıkar ve ekrana yazdırılır.
adi='Elif'
print (adi is 'Elif') # Aynı değeler is operatörü ile sorgulandığı için True çıkar ve ekrana yazdırılır.
print (adi is not 'Elif') #is operatörünün tersini verir.