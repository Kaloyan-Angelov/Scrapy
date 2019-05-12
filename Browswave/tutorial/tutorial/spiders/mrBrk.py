# -*- encoding: utf-8 -*-
import scrapy


class MrbrkSpider(scrapy.Spider):
    name = 'mrBrk'
    allowed_domains = ['mr-bricolage.bg']
    start_urls = ['https://mr-bricolage.bg/bg/Instrumenti/Avto-i-veloaksesoari/Veloaksesoari/ZhILETKA-SVETLOOTRZhZELENA/p/857037']

    def parse(self, response):
        price_to_filter = response.css("p.price::text").get()
        price = []
        for i in price_to_filter:
            if ord(i) < 48 and ord(i) > 57 and ord(i) != 46:
                pass
            else:
                price.append(i)
        price = "".join(price)
        price = price.strip().split()[0]
        yield {
            'image': response.css("section.product-single img::attr(src)").get(),
            'title': response.css("h1::text").get(),
            "price": price,
            'classifications': response.css("div.product-classifications td.attrib::text").getall()
        }

        # next_page = response.css("li.pagination-next a::attr(href)").get()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)

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
