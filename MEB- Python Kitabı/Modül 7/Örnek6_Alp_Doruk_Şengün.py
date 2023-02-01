def agacCiz(agacinYuksekligi, karakter='*'): #fonksiyon tanımlanır.
 b=agacinYuksekligi
 for i in range(1,agacinYuksekligi+1): # range içerisindek işlemler yapılır o 1 ile diğer aralıktaki sayılar alınır for döngüsünde i ye tanımlanır.
    print(b*' ',(2*i-1)*karakter)
 b-=1
agacYuksekligi=int(input("Ağacın yüksekliği kaç satır olsun? : "))
agacKarakteri=input("Ağaç için bir sembol veya karakter girin? : ")
if agacKarakteri!='' and agacYuksekligi>=1:
 agacCiz(agacYuksekligi, agacKarakteri[0]) # fonkisyon çağırılır ve işlem yapılır.
elif agacKarakteri=='' and agacYuksekligi>=1:
 agacCiz(agacYuksekligi) # fonkisyon çağırılır ve işlem yapılır.
else: print('Hatalı giriş')
