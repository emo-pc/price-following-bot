# 🛒 Amazon Price Tracker & Notifier Bot

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B.svg)
![Selenium](https://img.shields.io/badge/Selenium-Scraping-43B02A.svg)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57.svg)

Bu proje; Amazon üzerindeki ürünlerin güncel fiyatlarını otomatik olarak takip eden, kullanıcı dostu bir web arayüzüne sahip ve belirlenen hedef fiyata ulaşıldığında anında e-posta ile bildirim gönderen **uçtan uca (end-to-end) bir web scraping ve otomasyon** uygulamasıdır.

---

## 🚀 Kurulum ve Çalıştırma Rehberi (Adım Adım)

Uygulamayı bilgisayarınızda sorunsuz çalıştırmak için terminalinizde aşağıdaki adımları sırasıyla uygulayın.

### 1. Projeyi Bilgisayarınıza İndirin
Öncelikle projeyi GitHub'dan klonlayın ve proje klasörünün içine girin:
```bash
git clone [https://github.com/KULLANICI_ADINIZ/amazon-price-tracker.git](https://github.com/KULLANICI_ADINIZ/amazon-price-tracker.git)
cd amazon-price-tracker
```

### 2. Sanal Ortam (Virtual Environment) Kurulumu
Kütüphanelerin bilgisayarınızdaki diğer projelerle çakışmaması için izole bir ortam oluşturun (macOS / Linux uyumlu):
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Gerekli Kütüphanelerin Yüklenmesi
Sanal ortamınız aktifken (terminalde `(venv)` yazar), uygulamanın ihtiyaç duyduğu tüm paketleri kurun:
```bash
pip install streamlit selenium webdriver-manager beautifulsoup4 pandas schedule requests
```

### 4. E-Posta Bildirim Ayarları
İndirim olduğunda botun size mail atabilmesi için `check_prices.py` dosyasını açın ve ilgili kısımları doldurun:
```python
EMAIL_ADRESIM = "senin.mailin@gmail.com"
EMAIL_SIFREM = "16_haneli_uygulama_sifreniz" 
```
> **⚠️ Güvenlik Notu:** Kendi kişisel Gmail şifrenizi **kullanmayın**. Google Hesabı ayarlarınızdan (Güvenlik > 2 Adımlı Doğrulama > Uygulama Şifreleri) bu bota özel 16 haneli bir "Uygulama Şifresi" oluşturup buraya yapıştırın.

---

## 💻 Uygulamayı Kullanma (Çift Terminal Sistemi)

Uygulamanın arayüzü ve arka plan botu eşzamanlı çalışır. Bunun için proje klasöründe **iki ayrı terminal sekmesi** açın ve ikisinde de `source venv/bin/activate` komutuyla sanal ortamı aktif edin.

### 1️⃣ Web Arayüzünü Başlatma
Birinci terminalde aşağıdaki komutu çalıştırarak Streamlit panelini başlatın:
```bash
streamlit run app.py
```
Tarayıcınızda açılan ekrandan takip etmek istediğiniz Amazon ürününün linkini ve beklediğiniz fiyatı kaydedin.

### 2️⃣ Otomasyon Botunu Başlatma
İkinci terminalde fiyat denetleme ve mail atma botunu başlatın:
```bash
python3 check_prices.py
```
Bu terminal açık kaldığı sürece sistem belirlediğiniz aralıklarla Amazon'u kontrol edecek ve fiyat hedefinize ulaştığında size anında e-posta gönderecektir.

---

## ✨ Projenin Temel Özellikleri

* **Kullanıcı Dostu Web Paneli:** Streamlit ile modern ve sade dashboard.
* **Gelişmiş Web Scraping:** Selenium ve BeautifulSoup ile Amazon bot korumalarını aşan güçlü veri çekme altyapısı.
* **Yerel Veritabanı (SQLite):** Takip edilen tüm ürünlerin, linklerin ve fiyat verilerinin güvenle saklanması.
* **Zamanlanmış Görevler:** `schedule` kütüphanesi ile insan müdahalesine gerek duymayan otomasyon döngüsü.

## 📂 Proje Mimarisi

```text
📦 amazon-price-tracker
 ┣ 📜 app.py               # Web arayüzünü başlatan ana dosya
 ┣ 📜 scraper.py           # Selenium tabanlı veri çekme motoru
 ┣ 📜 database.py          # SQLite veritabanı operasyonları
 ┣ 📜 check_prices.py      # Arka planda çalışan bildirim botu
 ┣ 📜 tracker.db           # Ürünlerin tutulduğu veritabanı (Otomatik oluşur)
 ┗ 📜 README.md            # Proje dokümantasyonu
```
