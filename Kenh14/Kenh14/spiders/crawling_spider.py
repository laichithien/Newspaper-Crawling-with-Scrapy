from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(CrawlSpider):
    name = 'Kenh14'
    allowed_domains = [
        'kenh14.vn'
    ]
    start_urls = [
        'https://kenh14.vn/'
    ]

    rules = (
        Rule(LinkExtractor(allow=r'^https:\/\/kenh14\.vn\/[a-z-]+\.chn$')),
        Rule(LinkExtractor(allow=r'^https:\/\/kenh14\.vn\/[a-z-]+-\d+\.chn$'), callback='parse_item')  
    )

    def parse_item(self, response):
        content = response.css('.knc-content p::text').getall()
        full_content = '\n'.join(content)
        # category = response.css('ul.breadcrumb a::text').getall()
        category = response.css('.kbws-list a::text').get()

        yield{
            # 'link': response.request.url,
            'category': category,
            'title': response.css('h1.kbwc-title::text').get(),
            'date time': response.css('span.kbwcm-time::text').get(),
            'description': response.css('.knc-sapo::text').get(),
            'content': full_content,
        }