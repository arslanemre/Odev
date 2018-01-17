import time

class Hayvanlar(): # Ana Sınıf Hayvanlar Oluşturuldu
    def __init__(self, ayak_sayisi="0", yetenek="Yok", özellikler="Yok"): #İnit metoduna kendimiz özel değerlerimizi atıyoruz.
        self.ayak_sayisi = ayak_sayisi
        self.yetenek = yetenek
        self.özellikler = özellikler


class Köpek(Hayvanlar):#Kökpek Sınıfı Hayvanlar Sınıfın'dan kalıtılarak oluşturuldu.
    def __init__(self, ayak_sayisi, yetenek, özellikler, tür="Yok", ülke="Yok"):#Burda iki tane yeni özellik eklendi "Tür ve Ülke Bilgisi"
        super().__init__(ayak_sayisi, yetenek, özellikler) #Super metodu ile miras aldığımız sınıfın özelliklerini eklemiş oluyoruz.
        self.tür = tür #tür ve Ülke özellikleri sınıf a tanımlanıyor.
        self.ülke = ülke

    def kopekekle(self, ayak, ytnk, ozellik, tur, ulke):#Burdaki fonksiyon ile parametreye denk gelen özellikleri bilgi girişi için eşitliyoruz.
        self.ayak_sayisi = ayak#input metodu ile bilgi girişi yapacağız.
        self.yetenek = ytnk
        self.özellikler = ozellik
        self.tür = tur
        self.ülke = ulke

    def bilgilerigoster(self):#bilgileri gostermek için bir fonksiyon
        print("Köpek Sınıfı Bilgileri..")
        print("Ayak Sayısı: {}\nYetenek: {}\nÖzellikler: {}\nTür: {}\nÜlke: {} ".format(self.ayak_sayisi, self.yetenek,
                                                                                        self.özellikler, self.tür,
                                                                                        self.ülke))


class Kus(Köpek, Hayvanlar):#Kuş sınıfı köpek ve hayvanlar sınıfınlarından türetilerek oluşturuluyor.
    def __init__(self, ayak_sayisi, yetenek, özellikler, tür, ülke, ses="Yok"):#burda eklediğimiz özellik ses.
        super().__init__(ayak_sayisi, yetenek, özellikler, tür, ülke)#Kalıtım sınıfından alarak ezdiğimiz verileri super metodu ile çağırıyoruz.
        self.ses = ses

    def kus_ekle(self, ayak, ytnk, ozellik, tur, ulke, ses):
        self.ayak_sayisi = ayak
        self.yetenek = ytnk
        self.özellikler = ozellik
        self.tür = tur
        self.ülke = ulke
        self.ses = ses

    def kus_bilgileri_goster(self):
        print("Kuş Sınıfı Bilgileri...")
        print("Ayak Sayısı: {}\nYetenek: {}\nÖzellikler:\nTür: {}\nÜlke: {}\nSes: {}".format(self.ayak_sayisi,
                                                                                             self.yetenek,
                                                                                             self.özellikler, self.tür,
                                                                                             self.ülke, self.ses))

class At(Köpek, Hayvanlar):
    def __init__(self, ayak_sayisi, yetenek, özellikler, tür, ülke, hız="0", boy="0"):
        super().__init__(ayak_sayisi, yetenek, özellikler, tür, ülke)
        self.hız = hız
        self.boy = boy

    def at_ekle(self, ayak, ytnk, ozellik, tur, ulke, hızı, boyu):
        self.ayak_sayisi = ayak
        self.yetenek = ytnk
        self.özellikler = ozellik
        self.tür = tur
        self.ülke = ulke
        self.hız = hızı
        self.boy = boyu

    def at_bilgileri_goster(self):
        print("At Sınıfı Bilgileri Gösteriliyor")
        print("Ayak Sayısı: {}\nYetenek: {}\nÖzellikler:\nTür: {}\nÜlke: {}\nHız: {}\n Boy: {}".format(self.ayak_sayisi,
                                                                                                       self.yetenek,
                                                                                                       self.özellikler,
                                                                                                       self.tür,
                                                                                                       self.ülke,
                                                                                                       self.hız,
                                                                                                       self.boy))
kopek = Köpek("4", "Yok", "Yok", "Yok", "Yok")#Sınıflardan yeni nesneler oluşturuyoruz. Ve parametre değerlerini veriyoruz.
kus = Kus("2", "Yok", "Yok", "Yok", "Yok", "Yok")
at = At("4","Yok","Yok","Yok","Yok","Yok","Yok")

print("""
*************************
Q. Çıkış için Q'ya basınız..
1. Köpek bilgisi girişi için
2. Köpek Bilgilerini Göstermek İçin
3. Kuş Bilgisi Girisi İçin
4. Kuş Bilgilerini Göstermek İçin
5. At Bilgilerinğin Girisi İçin
6. At Bilgilerini Göstermek İçin

Basınız...

************************
""")
while True:
    işlem = input("İşlem Seçiniz:")

    if işlem == "q":
        print("Program Sonlandırılıyor....")
        time.sleep(1.5)
        break
#Burada Giriş verileri isteniyor ve ilgili nesnenin ilgili fonksiyonu çalıştırılarak etkileşim sağlanıyor.
    elif işlem == "1":
        ayak_giris = input("Ayak Sayısı: ")
        yetenek_giris = input("Yeteneği: ")
        ozellik_giris = input("Özelliği: ")
        tur_giris = input("Türü: ")
        ulke_giris = input("Ülke: ")

        kopek.kopekekle(ayak_giris, yetenek_giris, ozellik_giris, tur_giris, ulke_giris)

    elif işlem == "2":
        kopek.bilgilerigoster()

    elif işlem == "3":
        ayak_giris = input("Ayak Sayısı: ")
        yetenek_giris = input("Yeteneği: ")
        ozellik_giris = input("Özelliği: ")
        tur_giris = input("Türü: ")
        ulke_giris = input("Ülke: ")
        ses_giris = input("Ses: ")

        kus.kus_ekle(ayak_giris, yetenek_giris, ozellik_giris, tur_giris, ulke_giris, ses_giris)

    elif işlem == "4":
        kus.bilgilerigoster()

    elif işlem == "5":
        ayak_giris = input("Ayak Sayısı: ")
        yetenek_giris = input("Yeteneği: ")
        ozellik_giris = input("Özelliği: ")
        tur_giris = input("Türü: ")
        ulke_giris = input("Ülke: ")
        hız_giris = input("Hız: ")
        boy_giris = input("Boy: ")

        at.at_ekle(ayak_giris, yetenek_giris, ozellik_giris, tur_giris, ulke_giris,hız_giris,boy_giris)

    elif işlem == "6":
        at.bilgilerigoster()
