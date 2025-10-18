class Kitap:
    def __init__(self, ad, yazar, syf, yil):
        self.__ad = ad  # Kapsülleme
        self.yazar = yazar
        self.yil = yil
        self.durum = "Müsait"

    def get_ad(self): return self.__ad
    def set_durum(self, d): self.durum = d
    
    def __str__(self): return f"'{self.__ad}' - {self.yazar} ({self.yil}) [{self.durum}]"

class Uye:
    def __init__(self, isim, no, rol="Standart"):
        self.isim = isim
        self.no = no
        self.rol = rol
        self.odunc = []

    def islem(self, kitap, tur):
        if tur == "al":
            if kitap.durum == "Müsait":
                kitap.set_durum("Ödünç verildi")
                self.odunc.append(kitap)
                print(f"BAŞARILI: '{kitap.get_ad()}' alındı.")
            else: print("HATA: Kitap müsait değil.")
        elif tur == "ver":
            if kitap in self.odunc:
                kitap.set_durum("Müsait")
                self.odunc.remove(kitap)
                print(f"BAŞARILI: '{kitap.get_ad()}' iade edildi.")
            else: print("HATA: Bu kitap sizde yok.")

    def bilgi_goster(self):
        print(f"--- {self.isim} ({self.rol}) --- ID: {self.no} --- Kitaplar: {len(self.odunc)}")

class Yonetici(Uye):
    def __init__(self, isim, no):
        super().__init__(isim, no, "Yönetici")
        self.departman = "Yönetim" # Otomatik atama

    def sil(self, kutuphane, k_adi):
        if kutuphane.kitap_sil(k_adi): # Eğer silerse True döner
            print(f"ADMİN İŞLEMİ: '{k_adi}' {self.isim} tarafından silindi.")

class Kutuphane:
    def __init__(self):
        self.kitaplar = []

    def ekle(self, k): self.kitaplar.append(k); print("Kitap Eklendi.")
    
    def kitap_bul(self, k_adi):
        for k in self.kitaplar:
            if k.get_ad().lower() == k_adi.lower(): return k
        return None

    def kitap_sil(self, k_adi):
        kitap = self.kitap_bul(k_adi)
        if kitap:
            self.kitaplar.remove(kitap)
            return True # Silindi
        print("Sistemde böyle bir kitap yok."); return False  

    def listele(self):
        print("\n--- KİTAPLAR ---")
        if not self.kitaplar: print("(Boş)")
        else:
            for k in self.kitaplar: print(k)

#  ANA PROGRAM 
def main():
    lib = Kutuphane()
    uyeler = []

    while True:
        print("""
      ========================================
              KÜTÜPHANE YÖNETİM PANELİ
      ========================================
        1.Kitap Ekle  
        2.Üye Ekle  
        3.Listele  
        4.Kitap Ödünç Ver  
        5.Kitap İadesi 
        6.Bilgi  
        7.Sil (Admin)  
        8.Çık
        """)
        sec = input("Seçim: ")

        if sec == '1':
            try:
                lib.ekle(Kitap(input("Ad: "), input("Yazar: "), int(input("Syf: ")), int(input("Yıl: "))))
            except: print("HATA: Sayısal değer giriniz.")

        elif sec == '2':
            ad, no = input("Ad: "), input("No: ")
            if input("Yönetici mi? (e/h): ").lower() == 'e':
                uyeler.append(Yonetici(ad, no))
                print("Yönetici eklendi.")
            else:
                uyeler.append(Uye(ad, no))
                print("Üye eklendi.")

        elif sec == '3': lib.listele()

        elif sec in ['4', '5']: # Ödünç Al ve Ver 
            kisi = input("Üye Adı: ")
            # Üyeyi bul
            aktif_uye = None
            for u in uyeler:
                if u.isim.lower() == kisi.lower(): aktif_uye = u; break
            
            if aktif_uye:
                kitap = lib.kitap_bul(input("Kitap Adı: "))
                if kitap: aktif_uye.islem(kitap, "al" if sec == '4' else "ver")
                else: print("Kitap bulunamadı.")
            else: print("Üye bulunamadı.")

        elif sec == '6': 
            kisi = input("Kişi Adı: ")
            bulundu = False # Başta bulamadık varsayıyoruz
            for u in uyeler:
                if u.isim.lower() == kisi.lower():
                    u.bilgi_goster()
                    bulundu = True # Bulduk 
                    break # Bulunca çık
            if not bulundu: print("Kayıtlı kişi bulunamadı.")

        elif sec == '7':
            admin_adi = input("Admin Adı: ")
            yetkili = None
            for u in uyeler:
                if u.isim.lower() == admin_adi.lower() and isinstance(u, Yonetici):
                    yetkili = u; break
            
            if yetkili: # Sadece yetkili varsa kitap sor
                yetkili.sil(lib, input("Silinecek Kitap: "))
            else: # Yoksa başa dön
                print("Yetkisiz işlem veya kullanıcı bulunamadı.")
                continue

        elif sec == '8': break
        else: print("Geçersiz işlem.")

if __name__ == "__main__": main()