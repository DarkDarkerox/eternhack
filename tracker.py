import time
from pygame import mixer
from mail import send_email
from chrome import abrir_chrome
from currentTime import get_time
mixer.init()
notifiacion = mixer.Sound('C:/Users/masan/Desktop/Hack/sound/notificacion.mp3')
alarma = mixer.Sound('C:/Users/masan/Desktop/Hack/sound/megatron.mp3')

def book_track(titulo, keywords):
    print("El ultimo lanzamiento es: ")
    for each in titulo.findAll('a'):
        href = each.get('href')
        print(each.string + "   +--------->   Hora: {}".format(get_time()))
        # notifiacion.play()
    for palabra_clave in keywords:
        if palabra_clave.casefold() in each.string.casefold():
            alarma.play()
            send_email(href)
            abrir_chrome("tushoppi.com.mx" + href)
            time.sleep(5)
            alarma.play()
            time.sleep(5)
            alarma.play()
            print("Adios bbcita")
            time.sleep(10)
            quit()

