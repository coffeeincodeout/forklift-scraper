import scrapy
from scrapy.selector import Selector
from scrapy.crawler import CrawlerProcess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import sys
import os
import re


class ForkliftSpider(scrapy.Spider):
    name = "forklift"
    start_urls = [
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=37&plz=&entfernung=1000',
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=2&plz=&entfernung=1000',
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=7&plz=&entfernung=1000',
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=41&plz=&entfernung=1000',
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=15&plz=&entfernung=1000',
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=3&plz=&entfernung=1000',
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=1&plz=&entfernung=1000',
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=23&plz=&entfernung=1000',
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=29&plz=&entfernung=1000',
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=11&plz=&entfernung=1000',
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=16&plz=&entfernung=1000',
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=20&plz=&entfernung=1000',
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=21&plz=&entfernung=1000',
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=47&plz=&entfernung=1000',
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=18&plz=&entfernung=1000',
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=35&plz=&entfernung=1000',
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=5&plz=&entfernung=1000',
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=19&plz=&entfernung=1000',
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=57&plz=&entfernung=1000',
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=59&plz=&entfernung=1000',
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=33&plz=&entfernung=1000',
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=4&plz=&entfernung=1000',
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=27&plz=&entfernung=1000',
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=6&plz=&entfernung=1000',
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=24&plz=&entfernung=1000',
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=14&plz=&entfernung=1000',
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=63&plz=&entfernung=1000',
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=26&plz=&entfernung=1000',
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=12&plz=&entfernung=1000',
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=65&plz=&entfernung=1000',
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=25&plz=&entfernung=1000',
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=13&plz=&entfernung=1000',
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=10&plz=&entfernung=1000',
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=61&plz=&entfernung=1000',
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=8&plz=&entfernung=1000',
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=32&plz=&entfernung=1000',
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=22&plz=&entfernung=1000',
        'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0&hatbild=0&reifen=*&preisbis=1000000&landid=31&plz=&entfernung=1000',

    ]

    TMP_FILE = os.path.join(os.path.dirname(sys.modules['forklift'].__file__), 'tmp/forklift.csv')

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': TMP_FILE,
        'DOWNLOAD_DELAY': 8,
        'CONCURRENT_REQUESTS': 1,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
        'AUTOTHROTTLE_ENABLED': True,
        'AUTOTHROTTLE_START_DELAY': 8,
    }

    # parse data from the first page
    def parse(self, response):
        url = response.url
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
        time.sleep(2)
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
                time.sleep(5)
                # pass url to scrapy to parse
                page_url = driver.current_url
                yield scrapy.Request(page_url, callback=self.pageFollow)

            driver.close()
        else:
            # close the driver
            driver.close()
            url = response.url
            yield scrapy.Request(url, callback=self.pageFollow)


    # second function to parse pages
    def pageFollow(self, response):
        # get individual urls for each forklift
        for url in response.css('div.card > a.btn.detail.haslink::attr(href)').extract():
            products_url = response.urljoin(url)
            yield scrapy.Request(products_url, callback=self.get_product)
        # parse pagination
        pagination = response.css('ul.pagination > li > a[aria-label="Next"]::attr(href)').extract_first()
        if pagination is not None:
            pagination = response.urljoin(pagination)
            yield scrapy.Request(pagination, callback=self.pageFollow)

    # third parser for the products page
    def get_product(self, response):
        # page url
        page_url = response.url
        company = response.css("div > div.panel-body.panel-contact > p:nth-child(2)::text").extract_first()
        location = response.xpath('//div/div[2]/p[2]/text()[2]').extract_first()
        # machine data
        make = response.css('div:nth-child(2) > span.tcontent::text').extract_first()
        forklift_type = response.css('div:nth-child(3) > span.tcontent::text').extract_first()
        model = response.css('div:nth-child(4) > span.tcontent::text').extract_first()
        engine_type = response.css('div:nth-child(5) > span.tcontent::text').extract_first()
        capacity = response.css('div:nth-child(6) > span.tcontent::text').extract_first()
        year_yom = response.css('div:nth-child(8) > span.tcontent::text').extract_first()
        running_hours = response.css('div:nth-child(9) > span.tcontent::text').extract_first()
        price_excl_vat = response.css('div:nth-child(16) > span.tcontent::text').extract_first()
        # lifting mast
        mast_type = response.css('div:nth-child(1) > div:nth-child(2) > span.tcontent::text').extract_first()
        lift_height = response.css('div:nth-child(1) > div:nth-child(3) > span.tcontent::text').extract_first()
        closed_height = response.css('div:nth-child(1) > div:nth-child(4) > span.tcontent::text').extract_first()
        free_lift = response.css('div:nth-child(1) > div:nth-child(5) > span.tcontent::text').extract_first()
        fork_carriage = response.css('div:nth-child(1) > div:nth-child(6) > span.tcontent::text').extract_first()
        fork_length = response.css('div:nth-child(1) > div:nth-child(7) > span.tcontent::text').extract_first()
        forks = response.css('div:nth-child(1) > div:nth-child(8) > span.tcontent::text').extract_first()
        # general info
        engine_charger = response.css(
            'div.col-12.offset-lg-1.col-lg-4 > div:nth-child(2) > span.tcontent::text').extract_first()
        transmission = response.css(

            'div.col-12.offset-lg-1.col-lg-4 > div:nth-child(3) > span.tcontent::text').extract_first()
        battery_size_age = response.css(
            'div.col-12.offset-lg-1.col-lg-4 > div:nth-child(4) > span.tcontent::text').extract_first()
        tyres = response.css('div.col-12.offset-lg-1.col-lg-4 > div:nth-child(5) > span.tcontent::text').extract_first()
        front_tyres = response.css(
            'div.col-12.offset-lg-1.col-lg-4 > div:nth-child(6) > span.tcontent::text').extract_first()
        rear_tyres = response.css(
            'div.col-12.offset-lg-1.col-lg-4 > div:nth-child(7) > span.tcontent::text').extract_first()
        length = response.css(
            'div.col-12.offset-lg-1.col-lg-4 > div:nth-child(8) > span.tcontent::text').extract_first()
        width = response.css(
            'div.col-12.offset-lg-1.col-lg-4 > div:nth-child(9) > span.tcontent::text').extract_first()
        weight = response.css(
            'div.col-12.offset-lg-1.col-lg-4 > div:nth-child(10) > span.tcontent::text').extract_first()

        yield {
            'url': page_url,
            'company': company,
            'location': location,
            'price': price_excl_vat,
            'make': make,
            'model': model,
            'year': year_yom,
            'running hours': running_hours,
            'type': forklift_type,
            'engine_type': engine_type,
            'capacity': capacity,
            'mast type': mast_type,
            'lift height': lift_height,
            'closed height': closed_height,
            'free lift': free_lift,
            'fork carriage': fork_carriage,
            'fork length': fork_length,
            'forks': forks,
            'engine charger': engine_charger,
            'transmission': transmission,
            'battery size age': battery_size_age,
            'tyres': tyres,
            'front tyres': front_tyres,
            'rear tyres': rear_tyres,
            'length': length,
            'width': width,
            'weight': weight
        }


class MascusSpider(scrapy.Spider):
    name = "mascus"
    base_url = "https://www.mascus.com"
    TMP_FILE = os.path.join(os.path.dirname(sys.modules['forklift'].__file__), 'tmp/mascus.csv')
    FIELDS = [
        'url',
        'Company',
        'Location',
        'Price Excluding Tax',
        'Brand / model',
        'Category',
        'Year',
        'Hours',
        'Country',
        'Mascus ID',
        'Unit Number',
        'Serial Number',
        'Maximum lift capacity',
        'Maximum lift height',
        'Overall Lowered Height',
        'Fork length',
        'Tire type',
        'Transmission',
        'Additional Information'
    ]

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': TMP_FILE,
        'FEED_EXPORT_FIELDS': FIELDS,
        'DOWNLOAD_DELAY': 20,
        'CONCURRENT_REQUESTS': 1,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
        'AUTOTHROTTLE_ENABLED': True,
        'AUTOTHROTTLE_START_DELAY': 8,

    }

    def start_requests(self):
        yield scrapy.Request("https://www.mascus.com/material-handling,1,relevance,for-sale.html?currency=EUR",
                             callback=self.url_pagination)
        # yield scrapy.Request("https://www.mascus.com/material-handling,1,relevance,for-sale.html?currency=EUR",
        #                      callback=self.parse)

    # extracts the products url
    def parse(self, response):
        # gets the product url
        mascus_product_url = response.css('td.result-info > h3 > a::attr(href)').extract()
        # loops through the list of urls
        for url in mascus_product_url:
            # creates full url using base url with product url
            product_url = self.base_url + url
            # pause to prevent captcha
            time.sleep(2)
            yield scrapy.Request(product_url, callback=self.forklift_detail_parse)

    # extracts the product information from the page and outputs
    def forklift_detail_parse(self, response):
        product_details_list = []
        # get the table with html tr and td
        table_list = response.css('div.block-wrapp.full-title.product-info > span > div > table > tr').extract()
        # check if the table is empyt
        if len(table_list) == 0:
            message = response.css('body > form > h2::text').extract_first()
            image_urls = response.css('body > form > img').xpath('@src').extract_first()
            product_details_list.append(['url', response.url])
            product_details_list.append(['message', message])
            product_details_list.append(['image_urls', image_urls])

        # extract the company name
        company_name = response.css(
            'div.seller-details > div.seller-name.title-font::text').re_first(r'[A-Z]\w+.*[^\n\r]')
        product_url = response.url
        # append product url and company name to list
        product_details_list.append(['url', product_url])
        product_details_list.append(['Company', company_name])
        # turns the table list into a list with rows as a sublist
        for rows in table_list:
            # row elements are extracted and added to a list
            row_list = Selector(text=rows).css(
                'td::text, td > span::text, #pc-price > span:nth-child(1)::text, tr > td > div::text').extract()
            # append rows as a sublist
            if len(row_list) == 2:
                product_details_list.append(row_list)
            if len(row_list[1:]) > 1:
                row_list[1] = ''.join(row_list[1:])
                del row_list[2:]
                product_details_list.append(row_list)
        # update the dictionaly with the list
        final = dict(product_details_list)
        # del final_dict['Tax']
        # del final_dict['Price Including Tax']
        # del final_dict['images']

        yield final

    # creates number of urls needed to crawl and creates a list
    def url_pagination(self, response):
        # starts from page 1
        depth = response.css('div.mar-b.page-numbers-wrap > ul > li:nth-child(7) > a::text').extract_first()
        counter = 0
        page_depth = int(depth)

        while counter < page_depth:
            counter += 1
            pagination = str(counter)
            site_url = 'https://www.mascus.com/material-handling,' + pagination + ',relevance,for-sale.html'
            yield scrapy.Request(site_url, callback=self.parse)


class TradusSpider(scrapy.Spider):
    name = 'tradus'
    base_url = 'https://www.tradus.com'
    start_urls = [
        'https://www.tradus.com/en/search/material-handling-equipment-c4014/forklifts-t8/'
    ]
    TMP_FILE = os.path.join(os.path.dirname(sys.modules['forklift'].__file__), 'tmp/tradus.csv')

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': TMP_FILE,
        'DOWNLOAD_DELAY': 8,
        'CONCURRENT_REQUESTS': 1,
        'AUTOTHROTTLE_ENABLED': True,
        'AUTOTHROTTLE_START_DELAY': 5,

    }

    def parse(self, response):
        # next page link
        next_link = response.css(
            'div.search__footer > nav > div.pager__control.pager__control--next > a::attr(href)').extract_first()
        # combines site base url with the product url
        next_page_link = self.base_url + next_link
        # pass to parser to get the next page
        yield scrapy.Request(next_page_link, callback=self.parse)
        # product urls in list
        product_links = response.css('div.offer-result__name > h3 > a::attr(href)').extract()
        # loop through to get all the links out of list, combines with base url and parse
        for product_url in product_links:
            yield scrapy.Request(self.base_url + product_url, callback=self.product_parse)


    def product_parse(self, response):
        # company name
        company_name = response.css(
            'div.column.column-6.column-md-2.d-flex.f-wrap.mb-1.mb-md-0 > div > a > h2::text').extract_first().strip()
        # product price
        price = response.css(
            '#swipe_detect > header > dl.offer-header__meta-list > dd > span::text').re_first(r'[0-9].+[^€]')
        # dict with all the final details from the page
        product_details = {'url': response.url, 'company': company_name, 'price': price}
        # a list with all the details from the page
        details_list = response.css('#swipe_detect > section.offer-details > dl > dt::text, '
                                '#offer-overview > section > div > div > div > section:nth-child(1) > dl > dt::text, '
                                '#offer-overview > section > div > div > div > section:nth-child(2) > dl > dt::text, '
                                '#swipe_detect > section.offer-details > dl > dd::text, '
                                '#swipe_detect > section.offer-details > dl > dd > span::text, '
                                '#offer-overview > section > div > div > div > section:nth-child(1) > dl > dd::text, '
                                '#offer-overview > section > div > div > div > section:nth-child(1) > dl > dd > span::text,'
                                '#offer-overview > section > div > div > div > section:nth-child(2) > dl > dd::text'
                                ).extract()
        # list containing the description in a list
        description_list = response.css('section > div:nth-child(3)::text').extract()
        # looping through details and description list and adding to product details dict
        for k, v in zip(details_list[::2], details_list[1::2]):
            product_details[k.strip()] = v.strip()

        # empty variable that will store the description in one long string
        description = ""
        for items in description_list:
            description += items

        product_details['description'] = description

        yield {
            'url': product_details.get('url'),
            'company': product_details.get('company'),
            'location': product_details.get('Location'),
            'price': product_details.get('price'),
            'price type': product_details.get('Price type'),
            'make': product_details.get('Make'),
            'model': product_details.get('Model'),
            'year': product_details.get('Year'),
            'running hours': product_details.get('Hours run'),
            'mileage': product_details.get('Mileage'),
            'engine': product_details.get('Engine'),
            'condition': product_details.get('Condition'),
            'description': product_details.get('description'),
        }


class SupraliftSpider(scrapy.Spider):
    name = 'supralift'
    base_url = 'https://www.supralift.com'
    start_urls = [
        'https://www.supralift.com/uk/itemsearch/results/2?&pageNumber=0&sortCrit=ePriceDef&sortMod=asc&pageSize=10'
    ]

    TMP_FILE = os.path.join(os.path.dirname(sys.modules['forklift'].__file__), 'tmp/supralift.csv')
    FIELDS = [
        'url',
        'company',
        'location',
        'Price',
        'model',
        'Year of manufacture',
        'Power unit',
        'Type of truck',
        'Capacity (kg)',
        'Lift height (mm)',
        'Supralift product no.',
        'Mast type',
        'Comment',
    ]

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': TMP_FILE,
        'FEED_EXPORT_FIELDS': FIELDS,
        'DOWNLOAD_DELAY': 8,
        'CONCURRENT_REQUESTS': 1,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
        'AUTOTHROTTLE_ENABLED': True,
        'AUTOTHROTTLE_START_DELAY': 8,

    }

    def parse(self, response):
        next_page = self.base_url + response.css('form > div:nth-child(4) > div > a::attr(href)').extract_first()
        yield scrapy.Request(next_page, callback=self.parse)
        # a list with all the urls
        forklift_url_list = response.css('div > div:nth-child(1) > h3 > a::attr(href)').extract()
        # loop through both lists to filter out the products that are no a forklift
        for links in forklift_url_list:
            forklift_url = self.base_url + links
            yield scrapy.Request(forklift_url, callback=self.forklift_parse)

    def forklift_parse(self, response):

        company = response.css(
            'div.content_element.bg_blue.padding_small.margin_bottom_small > div > p:nth-child(1) > strong::text')\
            .extract_first()
        location = response.xpath('normalize-space(//div[1]/div/p[2]/text()[3])').extract_first()
        model = response.css('div:nth-child(1) > div:nth-child(1) > h2::text').extract_first()
        page_url = response.url
        product_details = response.css(
            'div > div:nth-child(2) > div > div.data_table_row > div.data_table_column, '
            'div > div:nth-child(2) > div > div.data_table_row > div.data_table_column > span, '
            'div > div:nth-child(9) > div:nth-child(2) > span.undel').xpath(
            'normalize-space(text())').re(r'[A-Z0-9].+[^\xa0]')
        product_details.remove('Quality rating')
        product_details.remove('Warranty')
        product_details.remove('Prices excluding VAT')
        final = {'url': page_url, 'company': company, 'location': location, 'model': model}
        for k, v in zip(product_details[::2], product_details[1::2]):
            final[k.strip()] = v.strip()

        yield final
# TMP_FILE = os.path.join(os.path.dirname(sys.modules['forklift'].__file__), 'tmp/allforklift.csv')
# FIELDS = ['url', 'company', 'location', 'price', 'make', 'model', 'year']
process = CrawlerProcess({
    # 'FEED_FORMAT': 'csv',
    # 'FEED_URI': TMP_FILE,
    # 'FEED_EXPORT_FIELDS': FIELDS,
})
process.crawl(ForkliftSpider)
# process.crawl(TradusSpider)
# process.crawl(MascusSpider)
process.crawl(SupraliftSpider)
process.start()
