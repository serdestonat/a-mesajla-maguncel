#Burada Playfair algoritmasının çalışma mantığına göre tablomuz oluşuyor.


# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: latin-1 -*-
def create_playfair_alphabet(key):
    # Türk alfabesini belirleyin (J harfi yoktur, yerine I kullanılır)
    turkish_alphabet = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
    
    # Anahtar kelimeyi büyük harflere çevirin
    key = key.upper()
    
    # Anahtar kelimedeki tekrar eden harfleri kaldırın
    seen = set()
    key_unique = ""
    for char in key:
        if char not in seen and char in turkish_alphabet:
            seen.add(char)
            key_unique += char

    # Anahtar kelimenin harflerinden sonra gelen harfleri ekleyin
    playfair_alphabet = key_unique
    for char in turkish_alphabet:
        if char not in seen:
            playfair_alphabet += char
    
    return playfair_alphabet

# Kullanıcıdan anahtar kelimeyi alın
key = input("Anahtar kelimeyi girin: ")

# Playfair alfabesini oluşturun
playfair_alphabet = create_playfair_alphabet(key)

def playfair_tablosu(alfabe):
  """
  Verilen alfabeyi kullanarak 6x6'lık Playfair tablosu oluşturur.

  Parametreler:
    alfabe (str): Tabloda kullanılacak harfleri içeren string.

  Dönüş Değeri:
    tablo (list): 6x6 boyutunda, her hücresi bir harf içeren liste.
  """
  

  tablo = []
  for i in range(6):
    satir = []
    for j in range(6):
      if i * 6 + j < len(alfabe):
        satir.append(alfabe[i * 6 + j])
      else:
        # Noktalama işaretlerini, "&" ve ":" işaretlerini yerleştirme
        if i == 4 and j == 5: 
          satir.append("&")
        elif i == 5 and j == 0:
          satir.append(".")
        elif i == 5 and j == 1:
          satir.append(",")
        elif i == 5 and j == 2:
          satir.append(":") 
        elif i == 5 and j == 3:
          satir.append(";")
        elif i == 5 and j == 4:
          satir.append("!")
        elif i == 5 and j == 5:
          satir.append("?")
        else:
          satir.append("")
    tablo.append(satir)
  return tablo

alfabe = playfair_alphabet
tablo = playfair_tablosu(alfabe)

# Tabloyu yazdırma
for satir in tablo:
  print(" ".join(satir))

