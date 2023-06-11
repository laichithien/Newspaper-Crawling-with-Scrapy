from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(CrawlSpider):
    name = 'VNE'
    allowed_domains = [
        'vnexpress.net'
    ]
    start_urls = [
        'https://vnexpress.net/'
    ]

    rules = (
        Rule(LinkExtractor(allow=r'https://vnexpress.net/[^/.]+$')),
        Rule(LinkExtractor(allow=r'https://vnexpress.net/[^/]+\.html$'), callback='parse_item')  
    )

    def parse_item(self, response):
        content = response.css('p.Normal::text').getall()
        full_content = '\n'.join(content)
        category = response.css('ul.breadcrumb a::text').getall()

        yield{
            # 'link': response.request.url,
            'category': category,
            'title': response.css('h1.title-detail::text').get(),
            'date time': response.css('span.date::text').get(),
            'description': response.css('p.description::text').get(),
            'content': full_content,
        }