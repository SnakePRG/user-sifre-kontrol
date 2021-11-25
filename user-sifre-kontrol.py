#SnakePRG

#İmport komutu ile "time" ve "os" uygulamamıza ekledik
import time
import os

#Burada kullanıcının gireceği kısmı yapıyoruz ve girilenlere bi ad atıyoruz ki kayıtlı olanla karşılaştırabilelim."İsim Giriş"i kısaltıp isimg yaptım şifreyide aynı şekilde.
isimg = input("Kullanıcı adını giriniz : ")
sifreg = input("Şifrenizi giriniz : ")

#İsim adını "İsim Bilgi"yi kısaltıp isimb yaptım şifrede aynı şekilde. Tırnak işaretinin içine istediğiniz isim ve şifre değerini yazabilirsiniz.
isimb = ("SnakePRG")
sifreb = ("123")


#Şifre ve İsimi kontrol ediyoruz ve bunu if, elif kullanarak yapıyoruz.İki tane  "==" "eşittirse" demektir. Eğer başında "!" işareti varsa "eşit değilse" demek. 
if (isimg == isimb) and (sifreg != sifreb): #isimg, isimb'ye eşit ama sifreg, sifreb'ye eşit değil eğer böyle bi durumla karşılaşırsa ekrana "Şifre yanlış..." yazdırdık.
    print("Şifre yanlış...")
    exit()
elif (isimg != isimb) and (sifreg == sifreb):
    print("Kullannıcı Adı yanlış...")       #isimg, isimb'ye eşit değil ama sifreg, sifreb'ye eşit eğer böyle bi durumla karşılaşırsa ekrana "Kullanıcı Adı yanlış..." yazdırdık.
    exit()
elif (isimb != isimg) and (sifreg != sifreb):
    print("Kullanıcı Adı ve Şifre hatalı.") #Burda iki değer de yanlış eğer böyle bir durumla karşılaşırsa ekrana "Kullanıcı Adı ve Şifre hatalı." yazdırdık.
    exit()

elif (isimb == isimg) and (sifreb == sifreg):
    print("Giriş yapılıyor...")             #Burda kullanıcı adıda şifrede doğruysa ekrana "Giriş yapılıyor..." yazdırdık ve 3 saniye bekledikten sonra yolu belirlenmiş uygulamayı açmasını söyledim.(Bu uygulama herhangi bir uygulama olabilir istediğinizi yapabilirsiniz.)
    time.sleep(3)
    os.startfile("Açılacak uygulamanın yolu")
    exit()

