metin=input("bir metin giriniz:") #bir metin girişi aldık
liste=metin.lower().split() #metni boşluklardan bölüp her kelimeyi bir string haline getirdik
print(f"toplam kelime sayisi: {len(liste)}") #burada uzunluk her karakteri yani her kelimeyi 1 alır yani kelime sayacı
print(f"toplam karakter sayisi: {len(metin)}") #metnin uzunluğuda her harfi ve boşluğu alır yani karakter sayacı
print(f"en uzun kelime: {len(max(liste))} harflidir.") #burda ise en uzun kelimeyi buluyoruz
sozluk={} #boş bir sözlük oluşturdum
for kelimeler in liste: #kelimeler değişkeni bir bir listedeki elemanların yerine geçecek
    if kelimeler in sozluk: #eğer listedeki kelimeler sözlükte varsa değeri 1 artar
        sozluk[kelimeler]+=1 #değer 1 arttı
    else: #eğer listedeki sözlükler yoksa eklenir ve değeri 1 olarak alınır
        sozluk[kelimeler]=1 #değer 1 alındı
print(sozluk) #en sonda sözlüğü yazdırıp her kelimenin değerine yani kaç kez geçtiğine bakarız

#büyük harf veya küçük harf farketmez kelimeyi aynı sayar hepsini lower ile küçük harflere çevirdik
    

