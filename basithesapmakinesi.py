while True: #bu biz komut verene kadar döngü devam edecek demek
 while True:
  try: #burada bir hata varmı bakıyor yoksa break ile bu döngüden çıkar
   a=float(input("birinci sayiyi giriniz:")) #sayı girdisi
   b=float(input("ikinci sayiyi giriniz:")) #sayı girdisi
   break
  except: #eğer hata varsa yazdırcak ve hata olduğu sürece döngüden çıkmayacak
    print("girdi hatali!!!")
 islem=input("bir islem seciniz(+,-,/,*):") #işlem girdisi
 if islem in ("+","-","/","*"): #burada işlem girdisi istediğimiz gibi mi bakıyoruz
    if islem=="+": # + ise
        print(f"sonuc: {a+b}") # topla ve yazdır
    elif islem=="-": # - ise
        print(f"sonuc: {a-b}") # çıkar ve yazdır
    elif islem=="/": # / ise
        if b==0: #tanımsızlık kontrolü
            print("bu islem tanimsizdir.") #tanımsız yazdır
        else: #değilse
         print(f"sonuc: {a/b}") #böl ve yazdır
    elif islem=="*": # * ise
        print(f"sonuc: {a*b}") #çarp ve yazdır
 else: #işlem girişi hatalıysa 
    print("hatali islem secimi.") #hatalı yazdır
 c=input("devam etmek istiyorsaniz 'y' yaziniz yoksa işlem sonlanacak: ") #y alırsak devam edecek
 if c!="y": #eğer y değilse
    break #döngüyü kır
