from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

import re
import time

# start url
url = 'https://www.forklift-international.com/de/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=2&plz=&entfernung=1000'
url2 = 'https://www.forklift-international.com/de/e/staplersuche.php?bhvon=0&preisvon=0&fhvon=0&bhbis=20000&fhbis=10000&bjbis=2019&hatbild=0&masttypid=alle&antriebsart=*&reifen=*&typ=&sonderbit=0&hrs=100000&Bauart=alle&baujahr=0&tkvon=0&hhvon=0&landid=37&entfernung=0&Fabrikat=alle&preisbis=1000000&tkbis=200000&hhbis=50000&Treffer='
# start chrome web driver. This will need to be changed to headless to run in the background
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options)
driver.get(url)
time.sleep(3)
# //*[@id="cookieModal"]/div/div/div/h2/button
cookies_button = driver.find_element_by_xpath('//*[@id="cookieModal"]/div/div/div/h2/button')
if cookies_button:
    cookies_button.click()
time.sleep(3)
# button with number //*[@id="treffer"]
search_button_text = driver.find_element_by_xpath('//*[@id="treffer"]').text
# extract the number from the text
number = re.search('[^A-z.>]+', search_button_text)
# if the number is greater than 500 begin filtering the data to lower the search amount
if number.group().strip() == '500':
    # loop through a 2 lists and update the
    von_list = list(range(0, 20001, 1000))
    bis_list = list(range(1001, 20002, 1000))
    for von, bis in zip(von_list, bis_list):
        # clear field and enter a search number
        tragkraft_von = driver.find_element_by_xpath('//*[@id="tkvon"]').clear()
        tragkraft_von = driver.find_element_by_xpath('//*[@id="tkvon"]')
        tragkraft_von.send_keys(von)
        tragkraft_bis = driver.find_element_by_xpath('//*[@id="tkbis"]').clear()
        tragkraft_bis = driver.find_element_by_xpath('//*[@id="tkbis"]')
        tragkraft_bis.send_keys(bis)
        # submit search results
        search_button = driver.find_element_by_xpath('//*[@id="treffer"]').click()
        # pause to allow page to load
        time.sleep(10)
        # pass url to scrapy to parse
        page_url = driver.current_url
        file = open('page_urls.txt', 'a')
        file.write(page_url + "\n")
        file.close()

    driver.close()

# close the driver
driver.close()
# TODO: check if the amount of search results is no equal to 0
# TODO: begin adjusting the filters as per requirements until number is less than 500
# TODO: submit search and pass response URL to scrapy parser
# TODO: make sure the response URL gets the URLs for the forklift products and passes to get_product parser

# tragkraft_von = //*[@id="tkvon"]
# tragkraft_bis =  //*[@id="tkbis"]
# hubhohe_von = //*[@id="hhvon"]
# hubhohe_bis = //*[@id="bhbis"]