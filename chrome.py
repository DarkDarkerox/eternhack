import webbrowser


def abrir_chrome(url):
    """This function open Google Chrome"""
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)
