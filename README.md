# 🛒 Amazon Fiyat Takip ve Bildirim Asistanı (Amazon Price Tracker)

Bu proje; **Python**, **Streamlit**, **Selenium** ve **SQLite** teknolojileri kullanılarak geliştirilmiş, e-ticaret sitelerindeki ürün fiyatlarını otomatik olarak takip eden ve hedef fiyata ulaşıldığında kullanıcıya anında e-posta bildirimi gönderen uçtan uca (end-to-end) bir otomasyon uygulamasıdır.

---

## ✨ Temel Özellikler

* **Modern Web Arayüzü (Streamlit):** Kullanıcı dostu arayüz üzerinden kolayca yeni ürün ekleme, hedef fiyat belirleme ve takip edilen ürünleri tablo halinde görüntüleme.
* **Güçlü Veri Kazıma (Selenium & BeautifulSoup):** Amazon'un gelişmiş bot korumalarını ve güvenlik duvarlarını aşarak ürün başlıklarını ve güncel fiyatları hatasız çekme.
* **Kalıcı Veri Yönetimi (SQLite):** Eklenen ürünlerin, URL'lerin, hedef fiyatların ve güncel fiyatların yerel bir veritabanında güvenle saklanması.
* **Akıllı E-Posta Bildirim Sistemi (`smtplib`):** Ürün fiyatı belirlenen hedef fiyatın altına düştüğünde veya eşitlendiğinde otomatik olarak e-posta gönderimi.
* **Otomasyon Desteği (`schedule`):** Arka planda periyodik olarak çalışan kontrol mekanizması ile fiyatları sürekli denetleme imkanı.

---

## 🛠️ Kullanılan Teknolojiler ve Kütüphaneler

* **Python 3.x**
* **Streamlit:** İnteraktif web dashboard tasarımı için.
* **Selenium & BeautifulSoup:** Dinamik web sayfalarından veri kazıma (Web Scraping) işlemleri için.
* **SQLite & Pandas:** Hafif veritabanı yönetimi ve veri analizi/gösterimi için.
* **`smtplib` / `email`:** E-posta bildirim altyapısı için.
* **`schedule`:** Zaman tabanlı otomasyon görevleri için.

---

## 📂 Proje Dosya Mimarisi

```text
📦 amazon-price-tracker
 ┣ 📜 app.py               # Streamlit web arayüzü ve kullanıcı paneli
 ┣ 📜 scraper.py           # Selenium ve BeautifulSoup tabanlı Amazon veri kazıma modülü
 ┣ 📜 database.py          # SQLite veritabanı bağlantı ve yönetim fonksiyonları
 ┣ 📜 check_prices.py      # Fiyatları periyodik kontrol eden ve e-posta atan otomasyon botu
 ┣ 📜 tracker.db           # SQLite veritabanı dosyası (Otomatik oluşur)
 ┗ 📜 README.md            # Proje dokümantasyonu
