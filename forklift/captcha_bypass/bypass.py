import scrapy

class CaptchaSpider(scrapy.Spider):
    name = "captcha"

    def parse(self, response):
        are_you_human = response.css('body > form > h2::text').extract_first()
        # extracts image from the url to be downloaded in a folder
        image =  response.css('body > form > img').xpath('@src').extract_first()
        input_box =  response.css('body > form > input.t').extract_first()
        submit_button = response.css('body > form > input.b').extract_first()


