import socket
import threading


HOST = '127.0.0.1'
PORT = 1234
KULLANICI_LIMITI = 5
aktif_kullanicilar = []

def mesajlari_al(kullanici, kullanici_adi):

    while 1:
        mesaj = kullanici.recv(2048).decode('utf-8')
        if mesaj != '':

            final_msj = kullanici_adi + '~' + mesaj
            send_messages_to_all(final_msj)
        else:
            print(f"{kullanici_adi} gönderdiği mesaj boş. ")

def kullaniciya_mesaj_gonder(kullanici, mesaj):

    kullanici.sendall(mesaj.encode())

def send_messages_to_all(mesaj):

    for kullanici in aktif_kullanicilar:

        kullaniciya_mesaj_gonder(kullanici[1], mesaj)




def k_isleyici(kullanici):

    while 1:
        kullaniciadi = kullanici.recv(2048).decode('utf-8')
        if kullaniciadi != '':
            aktif_kullanicilar.append((kullaniciadi, kullanici))
            bilgi_mesaji = "SERVER~" + f"{kullaniciadi} sohbete katıldı."
            send_messages_to_all(bilgi_mesaji)
            break
        else:
            print("Kullanici adi boş")


    threading.Thread(target=mesajlari_al, args=(kullanici, kullaniciadi,)).start()

def main():

    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        server.bind((HOST,PORT))
        print(f"Server bu konumda çalışıyor {HOST} {PORT}")
    except:
        print(f"{HOST} ana bilgisayarına ve {PORT} bağlantı noktasına bağlanılamıyor")

    server.listen(KULLANICI_LIMITI)

    while 1:

        kullanici, adres = server.accept()
        print(f"{adres[0]} {adres[1]} istemcisine başarıyla bağlanıldı")

        threading.Thread(target = k_isleyici, args=(kullanici, )).start()

if __name__ == '__main__' :
    main()