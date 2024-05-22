def playfair_sifrele(metin, anahtar):
    alfabe = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
    alfabe = ''.join(sorted(set(anahtar + alfabe), key=lambda x: (anahtar + alfabe).index(x)))

    matris = [alfabe[i:i+5] for i in range(0, 25, 5)]

    def pozisyon(harf):
        for i, satir in enumerate(matris):
            if harf in satir:
                return (i, satir.index(harf))
        return None  # Eğer harf matris içinde bulunmuyorsa None döndür

    metin = metin.replace(' ', '').upper()
    metin = [metin[i:i+2] for i in range(0, len(metin), 2)]

    if len(metin[-1]) == 1:
        metin[-1] += 'X'

    sifreli_metin = ""
    for cift in metin:
        p1 = pozisyon(cift[0])
        p2 = pozisyon(cift[1])

        if p1 is not None and p2 is not None:  # Her iki harf de matris içinde bulunuyorsa işlem yap
            if p1[0] == p2[0]:
                sifreli_metin += matris[p1[0]][(p1[1]+1)%5] + matris[p2[0]][(p2[1]+1)%5]
            elif p1[1] == p2[1]:
                sifreli_metin += matris[(p1[0]+1)%5][p1[1]] + matris[(p2[0]+1)%5][p2[1]]
            else:
                sifreli_metin += matris[p1[0]][p2[1]] + matris[p2[0]][p1[1]]
        else:
            if p1 is None:
                sifreli_metin += cift[0]
            if p2 is None:
                sifreli_metin += cift[1]

    return sifreli_metin

def pozisyon(harf,matris):
    for i, satir in enumerate(matris):
        if harf in satir:
            return (i, satir.index(harf))
    return None

def playfair_desifrele(sifreli_metin, anahtar):
    alfabe = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
    alfabe = ''.join(sorted(set(anahtar + alfabe), key=lambda x: (anahtar + alfabe).index(x)))

    matris = [alfabe[i:i+5] for i in range(0, 25, 5)]

    sifreli_metin = [sifreli_metin[i:i+2] for i in range(0, len(sifreli_metin), 2)]

    metin = ""
    for cift in sifreli_metin:
        if len(cift) == 2:  # Eğer cift uzunluğu 2 ise
            p1 = pozisyon(cift[0],matris)
            p2 = pozisyon(cift[1],matris)

            if p1 is not None and p2 is not None:
                if p1[0] == p2[0]:
                    metin += matris[p1[0]][(p1[1]-1)%5] + matris[p2[0]][(p2[1]-1)%5]
                elif p1[1] == p2[1]:
                    metin += matris[(p1[0]-1)%5][p1[1]] + matris[(p2[0]-1)%5][p2[1]]
                else:
                    metin += matris[p1[0]][p2[1]] + matris[p2[0]][p1[1]]
            else:
                if p1 is None and p2 is None:
                    metin += cift  # Eğer her iki harf de matris içinde bulunmuyorsa, orijinal çifti metne ekle
                elif p1 is None:  # Eğer birinci harf matris içinde bulunmuyorsa, sadece birinci harfi metne ekle
                    metin += cift[0]
                elif p2 is None:  # Eğer ikinci harf matris içinde bulunmuyorsa, sadece ikinci harfi metne ekle
                    metin += cift[1]
        else:
            metin += cift[0]  # Eğer cift uzunluğu 1 ise, sadece birinci harfi metne ekle

    return metin
