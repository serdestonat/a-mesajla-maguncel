import socket
import threading
from sifrelemedeneme import playfair_sifrele
from socket1 import wifi_ipv4_address

HOST = wifi_ipv4_address
PORT = 1234
KULLANICI_LIMITI = 5
ANAHTAR = "ANAHTAR"
aktif_kullanicilar = []

def mesajlari_al(kullanici, kullanici_adi):
    while 1:
        mesaj = kullanici.recv(2048).decode('utf-8')
        if mesaj != '':
            desifreli_mesaj = playfair_sifrele(mesaj, ANAHTAR)
            final_msj = kullanici_adi + '~' + desifreli_mesaj
            mesajlari_tumune_gonder(final_msj)
        else:
            print(f"{kullanici_adi} gönderdiği mesaj boş. ")

def kullaniciya_mesaj_gonder(kullanici, mesaj):
    kullanici.sendall(mesaj.encode())

def mesajlari_tumune_gonder(mesaj):
    for kullanici in aktif_kullanicilar:
        kullaniciya_mesaj_gonder(kullanici[1], mesaj)

def kullanici_isleyici(kullanici):
    while 1:
        kullaniciadi = kullanici.recv(2048).decode('utf-8')
        if kullaniciadi != '':
            aktif_kullanicilar.append((kullaniciadi, kullanici))
            bilgi_mesaji = "SERVER~" + f" {kullaniciadi} sohbete katıldı."
            mesajlari_tumune_gonder(bilgi_mesaji)
            break
        else:
            print("Kullanıcı adı boş")

    threading.Thread(target=mesajlari_al, args=(kullanici, kullaniciadi,)).start()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((HOST, PORT))
        print(f"Server bu konumda çalışıyor {HOST} {PORT}")
    except:
        print(f"{HOST} ana bilgisayarına ve {PORT} bağlantı noktasına bağlanılamıyor")

    server.listen(KULLANICI_LIMITI)

    while 1:
        kullanici, adres = server.accept()
        print(f"{adres[0]} {adres[1]} istemcisine başarıyla bağlanıldı")
        threading.Thread(target=kullanici_isleyici, args=(kullanici, )).start()

if __name__ == '__main__':
    main()

