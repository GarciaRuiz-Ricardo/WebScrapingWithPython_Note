import time
from urllib.request import urlretrieve
import subprocess
from selenium import webdriver

# Create new Selenium driver
# driver = webdriver.PhantomJS(executable_path='/opt/phantomjs/bin/phantomjs')
# Sometimes, this will not work. Then probably try this:
driver = webdriver.Firefox()

driver.get('https://www.amazon.com/War-Peace-Leo-Nikolayevich-Tolstoy/dp/1427030200')
time.sleep(2)

driver.find_element_by_id('sitbLogoImg').click()
imageList = set()

# Wait for the page to load
time.sleep(5)
# While the right arrow is available for clicking, turn through pages
while 'pointer' in driver.find_element_by_id('sitbReaderRightPageTurner').get_attribute('style'):
    driver.find_element_by_id('sitbReaderRightPageTurner').click()
    time.sleep(2)
    # Get any new pages that have loaded
    pages = driver.find_element_by_xpath("//div[@class='pageImage']/div/img")
    for page in pages:
        image = page.get_attribute('src')
        imageList.add(image)

driver.quit()

# Start processing the images we've collected URLs for with Tesseract
for image in sorted(imageList):
    urlretrieve(image, 'page.jpg')
    p = subprocess.Popen(['tesseract', 'page.jpg', 'page'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    f = open('page.txt', 'r')
    print(f.read())