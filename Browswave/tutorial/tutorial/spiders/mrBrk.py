# -*- encoding: utf-8 -*-
import scrapy
from collections import OrderedDict
# import json


class MrbrkSpider(scrapy.Spider):
    name = 'mrBrk'
    allowed_domains = ['mr-bricolage.bg']
    start_urls = [
        'https://mr-bricolage.bg/bg/Instrumenti/Avto-i-veloaksesoari/Veloaksesoari/c/006008012']
    # start_urls = ["https://mr-bricolage.bg/bg/Instrumenti/Avto-i-veloaksesoari/Veloaksesoari/c/006008012?q=%3Arelevance&page=1&priceValue="]

    # def Myparse(self, response):
    #     price_to_filter = response.css("p.price::text").get()
    #     price = []
    #     for i in price_to_filter:
    #         if ord(i) < 48 and ord(i) > 57 and ord(i) != 46:
    #             pass
    #         else:
    #             price.append(i)
    #     price = "".join(price).strip().split()[0]

    #     classification_to_filter = response.css(
    #         "div.product-classificationstd::text").getall()
    #     last = dict()
    #     for i in range(0, len(classification_to_filter), 2):
    #         last["".join(classification_to_filter[i]).strip()] = "".join(
    #             classification_to_filter[i+1]).strip()

    #     yield {
    #         'image': response.css(
    #             "section.product-single img::attr(src)").get(),
    #         'title': response.css("h1::text").get(),
    #         "price": price,
    #         'classifications': last
    #     }

    def parse(self, response):
        try:
            price_to_filter = response.css("p.price::text").get()
            price = []
            for i in price_to_filter:
                if ord(i) < 48 and ord(i) > 57 and ord(i) != 46:
                    pass
                else:
                    price.append(i)
            curr = "".join(price).strip().split()[1]
            price = "".join(price).strip().split()[0]

            classification_to_filter = response.css(
                "div.product-classifications td::text").getall()
            last = OrderedDict()
            for i in range(0, len(classification_to_filter), 2):
                last["".join(classification_to_filter[i]).strip()] = "".join(
                    classification_to_filter[i+1]).strip()
            # import pdb; pdb.set_trace()
            yield {
                'title': response.css("h1::text").get(),
                "price": {"total": price, "currency": curr},
                'image': response.css(
                    "section.product-single img::attr(src)").get(),
                'classifications': last
            }
        except:
            pass

        for next_page in response.css(
                "div.title a::attr(href)").extract():
            yield response.follow(next_page, callback=self.parse)

    # def parse_art(self, response):
        # price_to_filter = response.css("p.price::text").get()
        # price = []

        # for i in price_to_filter:
        #     if ord(i) < 48 and ord(i) > 57 and ord(i) != 46:
        #         pass
        #     else:
        #         price.append(i)
        # price = "".join(price).strip().split()[0]

        # yield {'cont': price}

# # gets next page
# next_page = response.css("li.pagination-next a::attr(href)").get()
# if next_page is not None:
#     next_page = response.urljoin(next_page)
#     yield scrapy.Request(next_page, callback=self.parse)

# # gets all from curr page products
# response.css("div.product div.title a::attr(href)").getall()

# # gets next page href
# response.css("li.pagination-next a::attr(href)").getall()

# # gets the image
# response.css("section.product-single img::attr(src)").get()
# # gets the title
# response.css("section.product-single img::attr(src)").get()
# # gets the price
# response.css("p.price::text").get()
# # gets all the classifications
# response.css("div.product-classifications td.attrib::text").getall()
