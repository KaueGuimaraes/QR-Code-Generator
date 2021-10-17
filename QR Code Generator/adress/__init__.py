import urllib
import urllib.request


def verify(adress):
    adress = verify_https(adress)
    
    try:
        site = urllib.request.urlopen(adress)
    except urllib.error.URLError:
        return False
    else:
        return True


def verify_https(adress):
    if adress[0:8] == 'https://':
        return adress
    else:
        return 'https://' + adress