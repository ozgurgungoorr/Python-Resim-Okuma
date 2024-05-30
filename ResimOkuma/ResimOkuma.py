from PIL import Image
import pytesseract
from gtts import gTTS

# Tesseract'ın yolunu belirtin
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# OCR işlemi: Resimden yazıyı okuma
resim = Image.open('frame.png')
metin = pytesseract.image_to_string(resim, lang='tur')

# OCR ile okunan metni yazdırma
print(metin)

# Metin boş değilse sese çevirme
if metin.strip():
    tts = gTTS(text=metin, lang='tr')
    tts.save("metin.mp3")
    print("Resimdeki yazı ses dosyasına dönüştürüldü ve 'metin.mp3' olarak kaydedildi.")
else:
    print("Resimde yazı bulunamadı veya okunamadı.")
