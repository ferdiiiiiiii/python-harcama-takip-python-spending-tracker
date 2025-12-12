# 💰 Kişisel Harcama Takip Sistemi (Spending Tracker)

Python kullanarak geliştirdiğim, kullanıcıların günlük harcamalarını kayıt altına alıp analiz edebileceği interaktif bir terminal (CLI) uygulaması.

## 🚀 Projenin Özellikleri ve İşlevleri

Bu proje, temel veri yapıları ve algoritma mantığı kullanılarak şu işlevleri yerine getirir:

### 1. ➕ Harcama Ekleme (`Input & Data Storage`)
* Kullanıcıdan **Kategori**, **Tutar** ve **Tarih** bilgilerini dinamik olarak alır.
* Alınan verileri bir sözlük (`dictionary`) yapısında düzenler ve ana listeye (`list`) ekler.
* *Örnek:* Market, 150.5, 12.12.2025

### 2. 📜 Harcamaları Listeleme (`Iteration`)
* Hafızada tutulan tüm harcama kayıtlarını `for` döngüsü ile gezer.
* Verileri kullanıcı dostu bir formatta (f-strings kullanarak) ekrana yazdırır.

### 3. 📊 Kategori Bazlı Toplam Hesaplama (`Filtering & Aggregation`)
* Kullanıcıdan bir kategori ismi ister (Örn: "Gıda").
* Liste içindeki tüm kayıtları tarar, sadece o kategoriye ait olanları bulur (`if` koşulu).
* İlgili harcamaların tutarlarını toplayarak o kategoride ne kadar harcama yapıldığını raporlar.

### 4. 🔄 Sürekli İşlem Menüsü (`Control Flow`)
* `While True` döngüsü ile kullanıcı "Çıkış" diyene kadar programın çalışmasını sağlar.
* Hatalı seçimlerde kullanıcıyı uyarır.

---

## 🛠️ Teknik Detaylar
Bu projede aşağıdaki Python konseptleri kullanılmıştır:
- **Veri Yapıları:** Listeler (`[]`) ve Sözlükler (`{}`)
- **Döngüler:** `while` (menü için) ve `for` (listeleme/hesaplama için)
- **Koşul Yapıları:** `if-elif-else` blokları
- **Tip Dönüşümleri:** `float()` ve `input()` kullanımı

## 💻 Nasıl Çalıştırılır?
Terminal veya komut satırında proje klasörüne gelip şu komutu yazın:

```bash
python spending_tracker.py
