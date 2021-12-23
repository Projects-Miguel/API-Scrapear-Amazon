import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['www.amazon.com.mx']
    start_urls = ['https://www.amazon.com.mx/']

    def parse(self, response):
        search = getattr(self, 'search_criteria', None)

        if search is None or search == "":
            raise Exception("The search criteria cant't be empty")
        else:
            splited_words = search.split(' ')
            separator = '+'
            parsed_word = separator.join(splited_words)

            return scrapy.Request(self.start_urls[0] + 's?k=' + parsed_word, self.after_init)

    def after_init(self, response):
        result = []
        data = response.xpath(
            '//*[@id = "search"]/div[1]/div[1]/div/span[3]/div[2]/div')

        for item in data:
            if item.xpath(".//div/div/div/div/div[2]/div[1]/h2/a/@href").get() is not None:
                result.append("https://www.amazon.com.mx" +
                              str(item.xpath(".//div/div/div/div/div[2]/div[1]/h2/a/@href").get()))

        yield {'items_urls': result[0:5]}
