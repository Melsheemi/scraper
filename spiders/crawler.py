import scrapy, lxml
#from scraper.spiders.urls import urls
from scraper.spiders import paths
#from scraper.items import ScraperItem 
import datetime
# from scrapy.exceptions import DropItem
from scrapy.crawler import CrawlerProcess
# from scrapy.settings.default_settings import FEED_EXPORT_ENCODING, FEED_EXPORTERS

class crawler(scrapy.Spider):
    name = 'crawler'
    start_urls = urls 

    def parse(self, response):
        items = ScraperItem()
        heading = response.xpath("/html/body/div[10]/div[4]/div/section/div[1]/div/div[1]/h1/text()").get().replace('\n','')
        level1 =  response.xpath("/html/body/div[10]/div[4]/div/div[1]/ul/li[4]/a/span/text()").get().replace('\n','')
        level2 = response.xpath("/html/body/div[10]/div[4]/div/div[1]/ul/li[5]/a/span/text()").get().replace('\n','')
        level3 = response.xpath("/html/body/div[10]/div[4]/div/div[1]/ul/li[6]/a/span/text()").get().replace('\n','') if response.xpath("/html/body/div[10]/div[4]/div/div[1]/ul/li[6]/a/span").get() is not None else None ,
        level4 = response.xpath("/html/body/div[10]/div[4]/div/div[1]/ul/li[7]/a/span/text()").get().replace('\n','') if response.xpath("/html/body/div[10]/div[4]/div/div[1]/ul/li[7]/a/span").get() is not None else None,
        level5 = response.xpath("/html/body/div[10]/div[4]/div/div[1]/ul/li[8]/a/span/text()").get() if response.xpath("/html/body/div[10]/div[4]/div/div[1]/ul/li[8]/a/span").get() is not None else None,
        unit = response.xpath(paths.unit).get().replace('\n','')
        t1 = response.xpath(paths.d1).get()
        v1 = response.xpath(paths.v1).get()
        t2 = response.xpath(paths.d2).get()
        v2 = response.xpath(paths.v2).get()
        t3 = response.xpath(paths.d3).get()
        v3 = response.xpath(paths.v3).get()
        t4 = response.xpath(paths.d4).get()
        v4 = response.xpath(paths.v4).get()
        t5 = response.xpath(paths.d5).get()
        v5 = response.xpath(paths.v5).get()
        t6 = response.xpath(paths.d6).get()
        v6 = response.xpath(paths.v6).get()
        t7 = response.xpath(paths.d7).get()
        v7 = response.xpath(paths.v7).get()
        t8 = response.xpath(paths.d8).get()
        v8 = response.xpath(paths.v8).get()
        t9 = response.xpath(paths.d9).get()
        v9 = response.xpath(paths.v9).get()
        price = response.xpath(paths.price).get() 

        items['heading'] = heading
        items['level1'] = level1
        items['level2'] = level2
        items['level3'] = level3
        items['level4'] = level4
        items['level5'] = level5
        items['unit'] = unit
        items['t1'] = t1 
        items['t2'] = t2
        items['t3'] = t3      
        items['t4'] = t4
        items['t5'] = t5 
        items['t6'] = t6
        items['t7'] = t7
        items['t8'] = t8
        items['t9'] = t9
        items['v1'] = v1
        items['v2'] = v2
        items['v3'] = v3
        items['v4'] = v4
        items['v5'] = v5
        items['v6'] = v6
        items['v7'] = v7
        items['v8'] = v8
        items['v9'] = v9
        items['price'] = price

        yield{
            'heading': heading,
            'location':{
                'level1': level1,
                'level2': level2,
                'level3':level3,
                'level4':level4,
                'level5':level5,
            },
            'ad data':{
                t1:v1,
                t2:v2,
                t3:v3,
                t4:v4,
                t5:v5, 
                t6:v6,
                t7:v7,
                t8:v8,
                t9:v9,
            },
            'unit':unit,
            'price':[{'price':price,'Date':'{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())}]
        }      
               
if __name__ == '__main__':

#    process = CrawlerProcess({
#        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
#    })

#    process.crawl(crawler)
#    process.start()
    print(type(crawler))