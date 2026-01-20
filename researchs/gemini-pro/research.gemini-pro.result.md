# CTF ve Konferans Takip Projesi - Teknik Analiz

## Proje Amacı
Bu proje, siber güvenlik uzmanlarının CTF (Capture The Flag) yarışmalarını terminal üzerinden takip etmesini sağlar.

## Teknik Yöntem
1. **Veri Kaynağı:** CTFTime.org (RSS ve HTML Parsing).
2. **Kütüphaneler:**
   - `requests`: HTTP istekleri için.
   - `BeautifulSoup4`: HTML verisini işlemek için.
3. **Arayüz:** CLI (Komut Satırı Arayüzü).

## Gemini Özel İsteği 1: Infografik (Akış Şeması)
Aşağıdaki şema projenin çalışma mantığını özetler:

```mermaid
graph TD
    A[Başlat] --> B{İnternet Var mı?}
    B -- Evet --> C[CTFTime.org'a Bağlan]
    B -- Hayır --> D[Hata Mesajı Göster]
    C --> E[Verileri Çek (Scraping)]
    E --> F[Verileri İşle (Parsing)]
    F --> G[Terminalde Listele]
```

```html
<!DOCTYPE html>
<html>
<head><title>CTF Takip</title></head>
<body>
    <h1>Yaklaşan CTF Yarışmaları</h1>
    <p>Veriler terminal üzerinden çekilmiştir.</p>
</body>
</html>
```