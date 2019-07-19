import scrapy, datetime
from scrapy.crawler import CrawlerProcess

class update(scrapy.Spider):
    name = 'update'
    allowed_domains = ["egypt.aqarmap.com"]
    start_urls = ['https://egypt.aqarmap.com/ar/for-sale/property-type/cairo/el-sheikh-zayed-city/'] # for sale only

    def parse(self, response):
        div = response.xpath("/html/body/div[9]/div[2]/section/div[1]/ul")
        for d in div:
            yield {
                'url': 'https://egypt.aqarmap.com' + d.xpath("./div[@class='card-container-wrapper']/a/@href").get()
            }                                                

        next_page = response.xpath("/html/body/div[9]/div[2]/section/div[2]/span[6]/a/@href").get()  # pagination object 
        if next_page is not None:
            yield response.follow(next_page, self.parse)  
        
        
if __name__ == '__main__':

    # process = CrawlerProcess({
    #    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    # })
    print(type(scrapy))
    # process.crawl(update)
    # process.start()
    # /html/body/div[9]/div[2]/section/div[2]/span[6]/a/@href
    # //div[@class = 'pagination']/span[@class = 'next']/a/@href
    # /html/body/div[9]/div[2]/section/div[1]/ul/div[3]/div/div/div[1]/div[2]/h2/a
    # /html/body/div[9]/div[2]/section/div[1]/ul/div/div/div/div[1]/a[@class = 'img-container-wrapper']/@href
    # /html/body/div[9]/div[2]/section/div[1]/ul
    # /html/body/div[9]/div[2]/section/div[1]/ul//div[@class='small-card search-Result-Card col-lg-6 col-md-6 col-sm-12 col-xs-12']
    
    # /html/body/div[9]/div[2]/section/div[2]/span[6]/a