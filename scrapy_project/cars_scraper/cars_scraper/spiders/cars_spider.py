import scrapy

class CarsSpider(scrapy.Spider):
    name = 'cars'
    
    def start_requests(self):
        urls = [
            'https://999.md/ru/61630522',
            'https://999.md/ru/63698666',
            'https://999.md/ru/63588835'
        ]
    
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        yield {
            'title': response.xpath('//*[@id="container"]/div/section/header/h1/text()').get(),
            'price': response.xpath('//*[@id="container"]/div/section/div/div/div[4]/div/div/div/ul/li/span[1]/text()').get(),
            'region': ''.join(response.xpath('//*[@id="container"]/div/section/div/div/div[4]/div/div/dl[1]/dd/text()').getall()),
            'phones': response.xpath('//*[@id="container"]/div/section/div/div/div[4]/div/div/dl[2]/dd/ul/li[1]/a/@href').get()[4:]
        }

class CarsListSpider(scrapy.Spider):
    name='cars_list'
    start_urls = [
        'https://999.md/ru/list/transport/cars?view_type=detail'
    ]

    def parse(self, response):
        cars = response.css('.ads-list-detail-item')
        for car in cars:
            yield {
                'title': car.css('.ads-list-detail-item-title a::text').get(),
                'description': car.css('.ads-list-detail-item-intro::text').get(),
                'price': car.css('.ads-list-detail-item-price::text').get()
            }
            # yield response.follow()
        
        next_page = response.xpath("//*[contains(@class, 'current')]/following-sibling::li/a/@href").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

        

