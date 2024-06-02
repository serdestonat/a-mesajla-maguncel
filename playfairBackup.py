# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: latin-1 -*-

import random

def playfair_tablosu():
  """
  6x6'lık bir Playfair tablosu oluşturur ve Türkçe alfabeyi yerleştirir.
  Boş kalan 7 alana da nokta, virgül, noktalı virgül, iki nokta, 
  ünlem işareti, soru işareti ve "&" işaretlerini yerleştirir.
  """
  alfabe = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
  tablo = [[None for _ in range(6)] for _ in range(6)]

  # Harfleri tabloya yerleştirme
  row = 0
  col = 0
  for harf in alfabe:
    tablo[row][col] = harf
    col += 1
    if col == 6:
      col = 0
      row += 1

  # Boş kalan alanlara özel karakterleri yerleştirme
  boş_alanlar = ['.', ',', ';', ':', '!', '?', '&']
  for harf in boş_alanlar:
    while True:
      row = random.randint(0, 5)
      col = random.randint(0, 5)
      if tablo[row][col] is None:
        tablo[row][col] = harf
        break

  # Tabloyu çıktı olarak yazdırma
  for satir in tablo:
    print(' '.join(satir))

# Playfair tablosunu oluşturma ve yazdırma
playfair_tablosu()
