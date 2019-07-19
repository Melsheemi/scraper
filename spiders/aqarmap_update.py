"""
Aqarmap spider
"""
import scrapy, lxml
from w3lib.url import url_query_parameter
from scrapy.settings.default_settings import FEED_EXPORT_ENCODING, FEED_EXPORTERS
import datetime

class aqarmap_update(scrapy.Spider):
    name = 'aqarmap_update'
    start_urls = ['https://egypt.aqarmap.com/ar/for-sale/property-type/cairo/el-sheikh-zayed-city/']

    def parse(self, response):
        div = response.xpath("/html/body/div[9]/div[2]/section/div[1]/ul//div[@class='small-card search-Result-Card col-lg-6 col-md-6 col-sm-12 col-xs-12']")
        urls = div.xpath("//div/div/div[1]/div[2]/a[@href]").get().split("/")[3].split('-')[0],
        for code in urls:
            yield scrapy.Request(code, meta = {'deltafetch_key': url_query_parameter(code, 'code')},
            callback= self.parse_element)
        
    def parse_element(self, response):
        div = response.xpath("/html/body/div[9]/div[2]/section/div[1]/ul//div[@class='small-card search-Result-Card col-lg-6 col-md-6 col-sm-12 col-xs-12']")
        counter = 1
        for d in div:
            yield {
            'unit': d.xpath("./div/div/div[1]/div[2]/div/a/div/label[4]/text()[2]").get().replace('\n','') if d.xpath("./div/div/div[1]/div[2]/div/a/div/label[4]/text()[2]").get() is not None else d.xpath("./div/div/div[1]/div[2]/div/a/div/label[2]/text()[2]").get().replace('\n',''),
            #'heading': d.xpath("./div/div/div[1]/div[2]/a/span[1]/text()").get(),
            'address':d.xpath("./div/div/div[1]/div[2]/p[2]/text()").get().replace('\n',''),
            'area': d.xpath("./div/div/div/div[2]/div/a/div[1]/label/text()[2]").get().replace('\n',''),
            'price':d.xpath("./div/div/div/div[2]/div/a/div[2]/span/text()").get(),
            'code': d.xpath("./div/div/div[1]/div[2]/a[@href]").get().split("/")[3].split('-')[0],
            'counter':counter
            }
            counter = counter + 1
        
        next_page = response.xpath("//div[@class = 'pagination']/span[@class = 'next']/a/@href").get()  # pagination object 
        if next_page is not None:
            yield response.follow(next_page, self.parse)  

