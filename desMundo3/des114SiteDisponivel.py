print('-*-'*3, '\033[31mSITE ACESSÍVEL\033[m', '-*-'*3)
import urllib # Biblioteca que verifica se o site está acessível
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[31mO site Pudim não está acessível no momento. :(\033[m')
else:
    print('\033[36mVocê conseguiu acessar o site Pudim com sucesso. :)\033[m')
    print(site.read()) # Para trazer o html do site
