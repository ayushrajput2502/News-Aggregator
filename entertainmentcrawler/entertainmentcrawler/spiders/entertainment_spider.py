import scrapy
from ..items import EntertainmentcrawlerItem
from news.models import ENHeadline
from entertainmentcrawler.spiders import entertainment_spider
from entertainmentcrawler import pipelines

class DnaEntertainmentSpider(scrapy.Spider):
    name = "dna_entertainment"
    start_urls = [
        'https://www.dnaindia.com/entertainment',
    ]

    def parse(self, response):
        for news_item in response.css('div.list-news > div.list-img'):
            item = EntertainmentcrawlerItem()

            # Extracting title
            title = news_item.css('a::attr(title)').get()
            # Extracting link
            link = news_item.css('a::attr(href)').get()
            # Extracting image URL
            img = news_item.css('img::attr(src)').get()
            # Setting values to item
            item['title'] = title
            item['image'] = img
            item['url'] = response.urljoin(link)  # Ensure to join relative URL with base URL
            item['source'] = 'DNA News'
            yield item

class NdtvEntertainmentSpider(scrapy.Spider):
    name = "ndtv_entertainment"
    start_urls = [
        'https://www.ndtv.com/entertainment/latest'
    ]

    def parse(self, response):
        for news_item in response.css('div.news_Itm'):
            item = EntertainmentcrawlerItem()

            # Extracting title
            title = news_item.css('div.news_Itm-cont > h2.newsHdng > a::text').get()

            # Extracting link
            link = news_item.css('div.news_Itm-cont > h2.newsHdng > a::attr(href)').get()

            # Extracting image URL
            img = news_item.css('div.news_Itm-img > a > img::attr(src)').get()

            # Setting values to item
            item['title'] = title
            item['image'] = img
            item['url'] = link
            item['source'] = 'NDTV'

            yield item


# class News18EntertainmentSpider(scrapy.Spider):
#     name = "news18_entertainment"
#     start_urls = [
#         'https://www.news18.com/entertainment/'
#     ]
#
#     def parse(self, response):
#         for blog_item in response.css('div.jsx-704b44ef308e1a3a.blog_list_row'):
#             item = EntertainmentcrawlerItem()
#
#             # Extracting title
#             title = blog_item.css('a::attr(title)').get()
#
#             # Extracting link
#             link = blog_item.css('a::attr(href)').get()
#
#             # Extracting image URL
#             img = blog_item.css('img::attr(data-src)').get()
#
#             # Setting values to item
#             item['title'] = title
#             item['image'] = img
#             item['url'] = link
#             item['source'] = 'News18'
#
#             yield item



# class EntertainmentSpider(scrapy.Spider):
#     name = "entertainment"
#     start_urls = [
#         'https://variety.com/'
#     ]
#
#     def parse(self, response):
#         for teaser in response.css('ul.o-tease-news-list > li.o-tease-list_item'):
#             item = EntertainmentcrawlerItem()
#
#             # Extracting title
#             title = teaser.css('div.o-tease_secondary > div.c-lazy-image > a::attr(title)').get()
#
#             # Extracting link
#             link = teaser.css('div.o-tease_secondary > div.c-lazy-image > a::attr(href)').get()
#
#             # Extracting image URL
#             img = teaser.css('div.o-tease_secondary > div.c-lazy-image > a > div > img::attr(src)').get()
#
#             # Setting values to item
#             item['title'] = title
#             item['image'] = img
#             item['url'] = link
#             item['source'] = 'Variety'
#
#             yield item
#
#
#
# class IndiaEntertainmentSpider(scrapy.Spider):
#     name = "entrtnment"
#     start_urls = [
#         'https://indianexpress.com/section/entertainment/'
#     ]
#
#     def parse(self, response):
#         articles = response.xpath('//div[@id="section"]/div[@class="container"]/div[@class="row"]/div[@class="leftpanel"]/div[@class="nation"]/div[contains(@class, "articles")]/div')
#
#         for article in articles:
#             items = EntertainmentcrawlerItem()
#
#             # Extracting title
#             title = article.xpath('.//div[@class="title"]/a/text()').get()
#
#             # Extracting link
#             link = article.xpath('.//div[@class="title"]/a/@href').get()
#
#             # Extracting image URL
#             img = article.xpath('.//div[@class="snaps"]/a/img/@src').get()
#
#             items['title'] = title.strip() if title else None
#             items['image'] = img.strip() if img else None
#             items['url'] = link.strip() if link else None
#             items['source'] = 'Indian Express'
#             yield items