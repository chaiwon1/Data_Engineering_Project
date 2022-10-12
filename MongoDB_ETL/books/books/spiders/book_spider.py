from scrapy import Spider
from scrapy.selector import Selector
from books.items import BooksItem


class BookSpiderSpider(Spider):
    name = 'book_spider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        books = Selector(response).xpath('//article[@class="product_pod"]')
        for book in books:
            item = BooksItem()
            item['title'] = book.xpath(
                'div/a/img/@alt').extract()[0]
            print(item['title'])

            item['price'] = book.xpath(
                'div/p[@class="price_color"]/text()').extract()[0]
            print(item['price'])

            instock_status = "".join(book.xpath(
                'div/p[@class="instock availability"]/text()').extract())
            instock_status = instock_status.strip('\n')
            instock_status = instock_status.strip()
            item['in_stock'] = instock_status
            print(item['in_stock'])

            rating = book.xpath(
                'p[contains(@class, "star-rating")]/@class').extract()[0]
            rating = rating.replace("star-rating ", "")
            item['rating'] = rating
            print(item['rating'])

            item['url'] = book.xpath(
                'div[@class="image_container"]/a/@href').extract()[0]
            print(item['url'])
            print('----------------')
            yield item
            