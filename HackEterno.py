import time
import requests
from tracker import book_track, get_time
from bs4 import BeautifulSoup
from requests.exceptions import Timeout, ConnectionError, ConnectTimeout

palabras_clave = ["Novelas Eternas","Eternas", "Novelas"]

while True:
    try:
        URL = "https://tushoppi.com.mx/collections/novedades?sort_by=created-descending"
        headers = {
            "User-Agent": """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"""}
        page = requests.get(URL, headers=headers, timeout=1)
    except (Timeout, ConnectionError, ConnectTimeout):
        print('Intentando reconectar................{}'.format(get_time()))
        time.sleep(3)
    else:
        soup = BeautifulSoup(page.content, 'html.parser')
        box = soup.find("div", {"class": "main_box"})
        title = box.find("div", {"class": "desc"})
        book_track(title, palabras_clave)
        time.sleep(3)
