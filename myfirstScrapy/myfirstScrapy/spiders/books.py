# -*- coding: utf-8 -*-
import scrapy


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        books = response.css('.product_pod')
        for book in books:
            title = book.css('a::attr(title)').extract_first()
            price = book.css('.price_color::text').extract_first()
            yield {
                'title':title,
                'price':price
            }
        next_url = response.css('.pager .next a::attr(href)').extract_first()
        url = response.urljoin(next_url)
        yield scrapy.Request(url=url,callback=self.parse)

