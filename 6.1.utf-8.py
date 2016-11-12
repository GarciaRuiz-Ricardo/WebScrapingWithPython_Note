from urllib.request import urlopen

url = 'http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt'
request = urlopen(url)
html = request.read()
# print(html)
print(str(html, 'utf-8'))