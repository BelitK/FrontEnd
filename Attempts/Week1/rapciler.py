import json
rapcilar = []
def save_json(rap):
    """
     arg = list
     alinan listeyi dosyaya kaydeder
     """
    # with open('rapcilar.json,'a') as yazi: eklemeli versiyon
    with open('rapcilar.json','w') as yazi: # yeni dosya olarak acip yazma
        yazi.write(json.dumps(rap))
while True:
    choice = str(input("cikis icin 'q'"))
    if choice == "q":
        break

# kullanici icin inputlar
    isim = input('isim \n')
    soyad = input("soyad")
    cinsiyet = input("cinsiyet")
    ssn = input("ssn")
    dogum = input("dogum: ")
    olum = input("olum : ")
    adresi = input("adres :")
    yas = input ("yas")
    # dict kullanilarak deger ikilileri alinir
    rapci = {
    "isim": isim,
    "last_isim": soyad,
    "cinsiyet": cinsiyet,
    "SSN":ssn,
    "dogum":dogum,
    "olum":olum,
    "adres":adresi,
    "yas":yas
    }
    rapcilar.append(rapci)
print(rapcilar)
save_json(rapcilar)
