from builtins import float, input, print


harcamalar = []

while True:
    print("\nHoş Geldiniz")
    print("1:Harcama Ekle")
    print("2:Harcamaları Listele")
    print("3:Kategoriye Göre Toplam Harcama")
    print("4:Çıkış")

    secim = input("İşlem Numaranız: ")

    if secim == "1":
        kategori = input("Kategori: ")
        tutar = float(input("Tutar: "))
        tarih = input("Tarih(Gün.Ay.Yıl): ")
        bilgiler = {
            "Kategori": kategori,
            "Tutar" : tutar,
            "Tarih" : tarih
            }      
        harcamalar.append(bilgiler)
        print("Ekleme Başarılı!")

    elif secim == "2":
        print("\nHarcamalar")
        for x in harcamalar:
            print(f"{x['Tarih']} {x['Kategori']} {x['Tutar']} TL")

    elif secim == "3":
         kategoriBul = input("Kategori: ")
         toplam = 0

         for x in harcamalar:
                if x["Kategori"] == kategoriBul:
                    toplam += x["Tutar"]

         print(f"{kategoriBul} Kategorisinde Toplam Harcama: {toplam} TL")

    elif secim == "4":
        print("Çıkış Yapılıyor...")
        break
    
    else:
        print("Geçersiz seçim")



