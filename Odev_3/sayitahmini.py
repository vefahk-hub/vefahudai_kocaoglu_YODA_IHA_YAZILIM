import random #rastegle sayı almak için random modülünü aldık
denemesayisi=0 #bir değişken atadım deneme sayısını bulmak için
for i in range (10): #10 defa tekrarlayacak döngüye giriyoruz
    number=random.randint(1,100) #number değişkenime 1-100 arası rastgele sayı atadım
    girilen=int(input("1 ile 100 arasinda(1-100 dahil)bir sayi tutunuz:")) #bir sayı girişi istedim ve tam sayı olmasını istedim yoksa hata verir
    denemesayisi+=1 #bu döngü her tekrarladığında bu değişken bir artacak başta o yüzden 0 verdik
    if girilen<=100 and girilen>=1: #burada sayımın 1ile 100 arasında olmasını istiyorum 1-100 dahil  
     if number==girilen: #eğer doğruyu bulduysak
      print(f"{denemesayisi} denemede dogru bildiniz.") #burada onu söylüyor
      break #ve artık döngüden çıkıyoruz
     else: #girilen değer yanlışsa
       print("yanlis") #yanlış olduğunu söylüyor
    else: # 1<=sayı<=100 değilse
       print("gecersiz deger") #hatalı olduğunu belirtiyor
       break #ve çıktık 
else: #eğer else demeseydik doğru bilseydik de bu print'i yazardı biz ise 10 defa tekrarladıktan sonra yazmasını istiyoruz
  print(" deneme hakkiniz bitti")
         

         
  
