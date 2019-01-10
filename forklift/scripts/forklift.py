from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import re
import time
# start url
url = 'https://www.forklift-international.com/de/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=2&plz=&entfernung=1000'
# start chrome web driver. This will need to be changed to headless to run in the background
driver = webdriver.Chrome()
driver.get(url)
time.sleep(25)
# //*[@id="cookieModal"]/div/div/div/h2/button
cookies_button = driver.find_element_by_xpath('//*[@id="cookieModal"]/div/div/div/h2/button')
if cookies_button:
    cookies_button.click()

# button with number //*[@id="treffer"]
search_button_text = driver.find_element_by_xpath('//*[@id="treffer"]').text
# extract the number from the text
number = re.search('[^A-z.>]+]', search_button_text)
# if the number is greater than 500 begin filtering the data to lower the search amount
if number.group().strip() == '500':
    pass
# TODO: begin adjusting the filters as per requirements until number is less than 500
# TODO: submit search and pass response URL to scrapy parser
# TODO: make sure the response URL gets the URLs for the forklift products and passes to get_product parser
