sinavPuani=int(input('Puanınız giriniz (0-100): '))
if sinavPuani>=85: # sinavPuani değişkeni 85 veya 85 den büyükse girintiden devam edilir. Değilse Elif e atlar.
 print('Pek iyi')
elif sinavPuani>=70: # sinavPuani değişkeni 70 veya 70 den büyükse girintiden devam edilir. Değilse diğer Elif e atlar.
 print('İyi')
elif sinavPuani>=55: # sinavPuani değişkeni 55 veya 55 den büyükse girintiden devam edilir. Değilse diğer Elif e atlar.
 print('Orta')
elif sinavPuani>=45: #sinavPuani değişkeni 45 veya 45 den büyükse girintiden devam edilir. Değilse else den devam eder.
 print('geçer')
else: print('Kaldı')