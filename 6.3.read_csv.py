from urllib.request import urlopen
from io import StringIO
import csv

url = 'http://pythonscraping.com/files/MontyPythonAlbums.csv'
request = urlopen(url)
data = request.read().decode('ascii', 'ignore')
# print(data)
dataFile = StringIO(data)
csvReader = csv.reader(dataFile)

# for row in csvReader:
#     print(row)
#
# for row in csvReader:
#     print('The album "' + row[0] + '" was released in ' + str(row[1]))