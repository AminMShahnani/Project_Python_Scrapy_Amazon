import scrapy
from ..items import AmazonItem

class AmazonSpiderSpider(scrapy.Spider):
    name = "amazon"
    start_urls = ["https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&qid=1693227334&rnid=1250225011&ref=lp_1000_nr_p_n_publication_date_0"]

    def parse(self, response):
        items= AmazonItem()

        product_name = response.css('.a-color-base.a-text-normal::text').extract()
        product_author = response.css('.widgetId\=search-results_6 .a-color-secondary .a-size-base:nth-child(4) , .widgetId\=search-results_2 span.a-size-base+ .a-size-base , .a-color-secondary .a-size-base.s-link-style , .a-color-secondary .a-row .a-size-base:nth-child(2)').css('::text').extract()
        product_price  = response.css('.puis-price-instructions-style .a-price-fraction , .puis-price-instructions-style .a-price-whole').css('::text').extract()
        product_imagelink = response.css('.s-image::attr(src)').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink

        yield items
