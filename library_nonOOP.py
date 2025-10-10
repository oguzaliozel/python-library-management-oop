import sys
books = []

def main():
    while True:
        print("\n*** Kütüphane ***")
        print(" 1-Ekle ")
        print(" 2-Sil ")
        print(" 3-Listele")
        print(" 4-Ödünç Ver ")
        print(" 5-İade ")
        print(" 6-Çık")
        
       
        secım = input("işlem: ")

        if secım == '1':
            isim = input("Kitap: ")
            yazar = input("Yazar: ")
            sayfa = input("Sayfa Sayısı: ") 
            
            books.append({
                "isim": isim, 
                "yazar": yazar, 
                "sayfa": sayfa, 
                "durum": 0 
            })
            print("Kitap Eklendi.")

        elif secım == '2':
            aranan = input("Silinecek isimi gir: ")
            bulundu = False
 
            for b in books:
                if b["isim"] == aranan:
                    books.remove(b)
                    print("Kitap Silindi.")
                    bulundu = True
                    break #döngüyü kırmak 
            
            if not bulundu:
                print("Kitap Bulunamadı.")

        elif secım == '3':
            print("--- Liste ---")
            if len(books) == 0:
                print("Boş.")
            else:
                for i, b in enumerate(books):
                    st = "Müsait"
                    if b["durum"] == 1: st = "Yok"
                    print(str(i+1) + ") " + b["isim"] + " - " + st)

        elif secım == '4':
            k = input("Ödünç Verilecek kitap: ")
            flag = 0 # Kontrol değişkeni
            for b in books:
                if b["isim"] == k:
                    flag = 1
                    if b["durum"] == 0:
                        b["durum"] = 1
                        print("Verildi.")
                    else:
                        print("Zaten yok.")
            
            if flag == 0: print("Kitap sistemde yok.")

        elif secım == '5':
            k = input("İade edilen kitap: ")
            for b in books:
                if b["isim"] == k:
                    b["durum"] = 0
                    print("İade alındı.")

        elif secım == '6':
            print("Bye.")
            sys.exit() 
            
        else:
            print("Yanlış tuş.")
main()  # procedural refactoring for OOP layout
