echo "CTF Taramasi Baslatiliyor..."

# 1. Programi calistir ve ciktilari kaydet
python main.py > ctf_sonuclar.txt

# 2. Auto Control (Otomatik Kontrol): Dosya olustu mu diye bakiyoruz
if [ -s ctf_sonuclar.txt ]; then
    echo "[BASARILI] Veriler ctf_sonuclar.txt dosyasina kaydedildi."
    echo "[SELF-CHECK] Sistem sorunsuz calisiyor."
else
    echo "[HATA] Veri cekilemedi veya dosya bos!"
fi