import urllib.request
print(urllib.request.urlopen("http://ya.ru").read().decode("utf-8"))
