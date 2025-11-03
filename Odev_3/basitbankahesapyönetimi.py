class hesap:
    def __init__(self,ad="-",soyad="-",no="-",bakiye=0): #kullanici icin fonksiyon tanimladim
        self.ad= ad
        self.soyad= soyad
        self.hesapno= no
        self.bakiye = bakiye
    def para_yatir(self,para): #para yatırma fonksiyonu
        self.bakiye += para #ileride bir değişkeni paraya atayacağız
        print(f"yeni bakiyeniz {self.bakiye} TL'dir.")
    def para_cek(self,para): #para cekme fonksiyonu
        if para<self.bakiye: #bakiyemiz çekeceğimiz değerden büyükse işlemi uyguluyor
            self.bakiye -= para
            print(f"yeni bakiyeniz {self.bakiye} TL'dir.")
        else: #eğer küçükse işlem uygulanmıyor 
            print("bakiye yetersiz")

print("hesap olusturunuz:")
bakiye=0 #burada 0 almayı seçtim yani yeni bir hesap olduğu için bakiyemiz 0 olacak
ad=input("ad giriniz:")
soyad=input("soyad giriniz:")
no=input("hesap no giriniz:") #burada yeni değişkenler oluşturdum 
print("hosgeldiniz!")
print("bakiyeniz: 0 TL")
kullanici=hesap(ad,soyad,no,bakiye) #burada da o değişkenleri kullanıcımın bilgilerine atıyorum
print(kullanici.ad,"-",kullanici.soyad,"-",kullanici.hesapno) #burada kullanıcı bilgilerini görsün istedim

while True: #burada biz isteyene kadar devam edecek döngüye giriyoruz
    f=input("para cekmek icin - yatirmak için + basin: ") #kullanıcıdan işlem seçmesini istiyoruz
    if f=="+": 
        miktar=float(input("yatiracaginiz miktari giriniz: "))
        kullanici.para_yatir(para=miktar) #fonksiyondaki işlemler gerçekleştirilir ve miktarı paraya atıyoruz
    elif f=="-":
        miktar=float(input("cekeceginiz miktari giriniz: ")) 
        kullanici.para_cek(para=miktar) #fonksiyondaki işlemler gerçekleştirilir ve miktarı paraya atıyoruz
    else:
        print("yanlis girdi, tekrar deneyiniz") #eğer + veya - girilmediyse işlem yapılmaz
    ans=input("tekrar islem yapmak istiyorsaniz evet yaziniz: ").lower() #kullanıcı evet derse devam eder sürekli lower sayesinde EVET de yazabilir
    if ans!="evet": #evet dışı herhangi bir kelimede döngüden çıkar
        break
print("iyi günler dileriz!") #kullanıcıya iyi günler dileriz
       







        
