# -*- encoding: utf-8 -*-
import scrapy


class MrbrkSpider(scrapy.Spider):
    name = 'mrBrk'
    allowed_domains = ['mr-bricolage.bg']
    start_urls = ['https://mr-bricolage.bg/bg/Instrumenti/Avto-i-veloaksesoari/Veloaksesoari/c/006008012']

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
            last = dict()
            for i in range(0, len(classification_to_filter), 2):
                if "".join(classification_to_filter[i]).strip() == 'Гаранция':
                    last["".join(classification_to_filter[i]).strip()] =\
                        " ".join("".join(classification_to_filter[i+1])
                                 .strip().split())
                else:
                    last["".join(classification_to_filter[i]).strip()] =\
                        "".join(classification_to_filter[i+1]).strip()

            yield {
                'image': response.css(
                    "section.product-single img::attr(src)").get(),
                "price": {"total": price, "currency": curr},
                'title': response.css("h1::text").get(),
                'classifications': last
            }
        except:
            pass

        for next_page in response.css(
                "div.title a::attr(href)").extract():
            yield response.follow(next_page, callback=self.parse)
