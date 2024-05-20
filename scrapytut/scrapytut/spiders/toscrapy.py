import scrapy


class ToscrapySpider(scrapy.Spider):
    name = "toscrapy"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        pass
