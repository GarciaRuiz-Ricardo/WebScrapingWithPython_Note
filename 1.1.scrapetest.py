from urllib.request import urlopen

url = "http://www.google.com"
request = urlopen(url)
html = request.read()

print(html)