# create links to all the european countries to crawl
country_list = [
        37,
        2,
        7,
        41,
        15,
        3,
        1,
        23,
        29,
        11,
        16,
        20,
        21,
        47,
        18,
        35,
        5,
        19,
        57,
        59,
        33,
        4,
        27,
        6,
        24,
        14,
        63,
        26,
        12,
        65,
        25,
        13,
        10,
        61,
        8,
        32,
        22,
        31
                ]

for n in country_list:
    url = 'https://www.forklift-international.com/en/e/staplersuche.php?sortorder=14&Bauart=alle' \
          '&Fabrikat=alle&sonderbit=0&typ=&antriebsart=*&masttypid=alle&tkvon=0&tkbis=200000&hhvon=0' \
          '&hhbis=50000&bhvon=0&bhbis=20000&fhvon=0&fhbis=10000&bjbis=2019&baujahr=0&hrs=100000&preisvon=0' \
          '&hatbild=0&reifen=*&preisbis=1000000&landid='+ str(n) +'&plz=&entfernung=1000'
    file = open('crawl_links.txt', 'a')
    file.write(url + "\n")
    file.close()