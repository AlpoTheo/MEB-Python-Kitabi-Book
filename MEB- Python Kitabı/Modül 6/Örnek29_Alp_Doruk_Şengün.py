a=int(input("tablonun satır uzunluğunu giriniz"))# a değişkeni atanır.
b=int(input("tablonun sütun uzunluğu giriniz")) # b değişkeni atanır.
for i in range(1,a+1): # 1 den a+1 değişkenine olan kısım alınır ve for döngüsünde i değişkenine atanır.
 for j in range(1,b+1): # 1 den b+1 değişkenine olan kısım alınır ve for döngüsünden j değişkenine atanır.
    print(j,end=" ")
    print( )