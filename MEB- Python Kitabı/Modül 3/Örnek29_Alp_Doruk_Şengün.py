on_mesaj="Sayın "
mesaj_sonu=" nisan dönemi faturanız: "
abone_no=input("abone numaranız") # Kullanıcıdan değer alınır alınan değer abone_no değişkenine atanır.
tuketim=input("tuketim miktarı") # Kullanıcıdan değer alınır alınan değer tuketim değişkenine atanır.
tuketim_tutari=int(tuketim)*4.0  # tuketim değişkeninin değeri int veri tipine çevirlir ve 4.0 la çarpılarak tuketim_tutari değişkenine atanır.
mesaj=on_mesaj+abone_no+mesaj_sonu+tuketim+" tl dir." # on_mesaj+abone_no+mesaj_sonu+tuketim+" tl dir." mesaj değişkenine atanır.
print(mesaj)