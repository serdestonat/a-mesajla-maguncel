# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: latin-1 -*-

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

alfabe = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
tablo = playfair_tablosu(alfabe)

# Tabloyu yazdırma
for satir in tablo:
  print(" ".join(satir))
