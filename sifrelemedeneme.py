from playfairdeneme import create_playfair_alphabet

def metni_parcala(metin, boyut=2):
    parcalar = []
    i = 0
    while i < len(metin):
        parca = metin[i:i+boyut]
        if len(parca) == 1:
            parca += 'A'  # Tek harf kalırsa A ekleyin
        elif parca[0] == parca[1]:
            parca = parca[0] + 'A'  # Aynı harf varsa araya A ekleyin
            i -= 1
        parcalar.append(parca)
        i += boyut
    return parcalar

def playfair_sifrele(metin, anahtar):
    metin = metin.upper().replace("J", "I")
    alfabe = create_playfair_alphabet(anahtar)
    kare = [alfabe[i:i+5] for i in range(0, len(alfabe), 5)]
    
    def konum_bul(harf):
        for satir in range(5):
            for sutun in range(5):
                if kare[satir][sutun] == harf:
                    return satir, sutun
        return None
    parcalar = metni_parcala(metin)
    sifreli_metin = ""

    for parca in parcalar:
        satir1, sutun1 = konum_bul(parca[0])
        satir2, sutun2 = konum_bul(parca[1])

        if satir1 is None or satir2 is None:
            raise ValueError(f"Karakter tablosunda bulunamadı: {parca[0]} veya {parca[1]}")

        if satir1 == satir2:
            sifreli_metin += kare[satir1][(sutun1 + 1) % 5] + kare[satir2][(sutun2 + 1) % 5]
        elif sutun1 == sutun2:
            sifreli_metin += kare[(satir1 + 1) % 5][sutun1] + kare[(satir2 + 1) % 5][sutun2]
        else:
            sifreli_metin += kare[satir1][sutun2] + kare[satir2][sutun1]

    return sifreli_metin

# Kullanıcıdan anahtar kelime ve şifrelenecek metni alın
anahtar = input("Anahtar kelimeyi girin: ")
acik_metin = input("Şifrelenecek metni girin: ")

# Playfair şifrelemesini gerçekleştirin
sifreli_metin = playfair_sifrele(acik_metin, anahtar)

print(f"Şifreli metin: {sifreli_metin}")