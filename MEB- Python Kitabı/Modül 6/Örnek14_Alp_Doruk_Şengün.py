yazi="Python üst düzey basit söz dizimine sahip, öğrenmesi oldukça kolay,modülerliği, okunabilirliği destekleyen, platform bağımsız nesne yönelimli yorumlanabilir bir script dilidir." 
sesli="aeıioöuü"
for i in yazi:#yazinin içerisindeki karakterler for döngüsüne alınarak i değişkenine atanır.
 if i in sesli: #seslinin içerisindeki karakter yaznin içersindeki karakterlerle karşılaştırılır aynı olanlar i değişkenine tanımlanır.
    print(i,end=",") #değişkenin değeri yazıldıktan sonra , işareti konularak ekrana yazdırılır.