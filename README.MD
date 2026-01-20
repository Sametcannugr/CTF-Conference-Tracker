# 🚩 CTF Yarışma Takip Projesi

Bu proje, **Açık Kaynak İşletim Sistemleri** dersi final ödevi olarak hazırlanmıştır. 
CTFTime sitesinden yaklaşan siber güvenlik yarışmalarını çeker ve listeler.

## ℹ️ Proje Hakkında
Python kullanarak geliştirdiğim bu araç, siber güvenlikçilerin yarışmaları takip etmesini kolaylaştırır. Verileri anlık olarak çeker ve sonuçları kaydeder.

## ✨ Özellikler
* 🐍 **Python ile Veri Çekme:** `BeautifulSoup` kütüphanesi ile web scraping yapar.
* 📄 **Loglama:** Sonuçları `ctf_sonuclar.txt` dosyasına otomatik kaydeder.
* 🐚 **Otomasyon:** Bash script ile tek komutla başlatılabilir.
* 🐧 **Cross-Platform:** Hem Windows hem Linux'ta çalışır.

## 🚀 Nasıl Çalıştırılır?

Projeyi indirdikten sonra terminalde şu komutu yazarak çalıştırabilirsiniz:

```bash
# Otomatik başlatma ve kontrol
./src/baslat.sh