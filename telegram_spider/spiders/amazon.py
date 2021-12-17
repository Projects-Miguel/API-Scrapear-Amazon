import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    search = 'televisores'
    # allowed_domains = ['www.amazon.com.mx']
    start_urls = ['https://www.amazon.com.mx/s?k={}'.format(search)]

    def parse(self, response):
        return scrapy.Request(self.start_urls[0], self.after_init)

    def after_init(self, response):
        result = []
        data = response.xpath(
            '//*[@id = "search"]/div[1]/div[1]/div/span[3]/div[2]/div')[7:]

        for item in data:
            result.append("https://www.amazon.com.mx" +
                          str(item.xpath(".//div/span/div/div/div[2]/div[1]/h2/a/@href").get()))

        yield {'items_urls': result[0:5]}
