from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.PhantomJS(executable_path='/opt/phantomjs/bin/phantomjs')
driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
time.sleep(1)
# print(driver.find_element_by_id('content').text)
pageSource = driver.page_source
bsObj = BeautifulSoup(pageSource, 'lxml')
print(bsObj.find('', {'id':'content'}).get_text())
driver.close()