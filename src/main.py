import requests
from bs4 import BeautifulSoup

def verileri_cek():
    url = "https://ctftime.org/event/list/upcoming"
    
    
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    print("Veriler cekiliyor...")

    
    cevap = requests.get(url, headers=header)

    if cevap.status_code == 200:
        soup = BeautifulSoup(cevap.content, "html.parser")
        
        
        satirlar = soup.find_all("tr")

        print("ISIM | TARIH | FORMAT")
        print("-" * 50)

        sayac = 0
        for satir in satirlar:
            
            sutunlar = satir.find_all("td")
            
           
            if len(sutunlar) > 0:
                isim = sutunlar[0].text.strip()
                tarih = sutunlar[1].text.strip()
                tur = sutunlar[2].text.strip()
                
                
                print(f"{isim} - {tarih} ({tur})")
                
                sayac += 1
                
                if sayac >= 10:
                    break
    else:
        print("Siteye baglanamadi hata var.")

if __name__ == "__main__":
    verileri_cek()
    input("Cikmak icin enter'a bas")