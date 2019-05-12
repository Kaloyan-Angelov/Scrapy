# -*- encoding: utf-8 -*-
import scrapy


class MrbrkSpider(scrapy.Spider):
    name = 'mrBrk'
    allowed_domains = ['mr-bricolage.bg']
    start_urls = ['https://mr-bricolage.bg/bg/Instrumenti/Avto-i-veloaksesoari/Veloaksesoari/ZhILETKA-SVETLOOTRZhZELENA/p/857037']
    # start_urls = []
    # start_urls = response.css("div.product div.title a::attr(href)").getall()
    # def start_requests(self):
    #     urls = response.css("div.product div.title a::attr(href)").getall()
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # urls = response.css("div.product div.title a::attr(href)").getall()
        # for url in urls:
        #     yield scrapy.Request(url=url, callback=self.parse)

        yield {
            'image': response.css("section.product-single img::attr(src)").get(),
            'title': response.css("h1::text").get(),
            'price': response.css("p.price::text").get(),
            'classifications': response.css("div.product-classifications td.attrib::text").getall()
        }

        next_page = response.css("li.pagination-next a::attr(href)").get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

# gets all from curr page products
# response.css("div.product div.title a::attr(href)").getall()
# gets next page href
# response.css("li.pagination-next a::attr(href)").getall()

# gets the image
# response.css("section.product-single img::attr(src)").get()
# gets the title
# response.css("section.product-single img::attr(src)").get()
# gets the price
# response.css("p.price::text").get()
# gets some classifications #TODO: get all of them
# response.css("div.product-classifications td.attrib::text").getall()
