import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Comparison_of_text_editors'
request = urlopen(url)
bsObj = BeautifulSoup(request, 'lxml')

# The main compasion table is currently the first table on the page
table = bsObj.findAll('table', {'class': 'wikitable'})[0]
rows = table.findAll('tr')
# print(rows)

csvFile = open('files/5.3.editors.csv', 'wt')
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()