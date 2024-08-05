import scrapy
from ..items import NewscrawlerItem
from news.models import Headline
from newscrawler.spiders import news_spider
from newscrawler import pipelines

class HindiTechnologySpider(scrapy.Spider):
    name = "hindi_technology"
    start_urls = [
        'https://www.thehindu.com/sci-tech/technology/',
    ]

    def parse(self, response):
        for news_item in response.css('.row-element'):
            item = NewscrawlerItem()

            # Extracting title
            title = news_item.css('h3.title.big a::text').get()

            # Extracting link
            link = news_item.css('h3.title.big a::attr(href)').get()

            # Extracting image URL
            img = news_item.css('.picture img::attr(data-original)').get()

            # Setting values to item
            item['title'] = title.strip() if title else ""
            item['image'] = img.strip() if img else None
            item['url'] = link.strip() if link else None
            item['source'] = 'Hindi Technology News'

            yield item

# class IndiaTechnologySpider(scrapy.Spider):
#     name = "india_technology"
#     start_urls = [
#         'https://indiatechnologynews.in/latest-it-news-and-technology-updates-in-india-india-technology-news/'
#     ]
#     max_news = 20
#     news_count = 0
#
#     def parse(self, response):
#         for news_item in response.css('.posts-list article.post--overlay'):
#             if self.news_count >= self.max_news:
#                 break
#
#             item = NewscrawlerItem()
#
#             # Extracting title
#             title = news_item.css('.post_text-wrap h3.post_title a::text').get()
#
#             # Extracting link
#             link = news_item.css('a.link-overlay::attr(href)').get()
#
#             # Extracting image URL
#             img = news_item.css('.background-img::attr(style)').re_first(r"url\('(.*?)'\)")
#
#             # Check if title exists, if not, set it to an empty string
#             item['title'] = title.strip() if title else ""
#
#             item['image'] = img.strip() if img else None
#             item['url'] = link.strip() if link else None
#             item['source'] = 'India Technology News'
#
#             yield item
#             self.news_count += 1

class NewsSpider(scrapy.Spider):
    name = 'news'
    start_urls=[
        'https://techcrunch.com/'
    ]

    def parse(self, response):
        div_all_news = response.xpath("//div[@class='river river--homepage']/div[@class='post-block post-block--image post-block--unread']")
        for index, article in enumerate(div_all_news[:10], start=1):  # Limit to 10 stories
            items = NewscrawlerItem()

            # Extracting title
            title = article.xpath(".//h2/a/text()").get().strip()

            # Extracting link
            link = response.urljoin(article.xpath(".//h2/a/@href").get())

            # Extracting image URL
            img = article.xpath(".//footer//img/@src").get()

            items['title'] = title
            items['image'] = img
            items['url'] = link
            items['source'] = 'Techcrunch'

            yield items
# class DnaTechnologySpider(scrapy.Spider):
#     name = "dna_technology"
#     start_urls = [
#         'https://www.dnaindia.com/technology',
#     ]
#
#     def parse(self, response):
#         for news_item in response.css('div.list-news div.list-img'):
#             item = NewscrawlerItem()
#
#             # Extracting title
#             title = news_item.css('a::attr(title)').get()
#
#             # Extracting link
#             link = news_item.css('a::attr(href)').get()
#
#             # Extracting image URL
#             img = news_item.css('img::attr(src)').get()
#
#             # Setting values to item
#             item['title'] = title
#             item['image'] = img
#             item['url'] = link
#             item['source'] = 'DNA India'
#
#             yield item
# class ReutersSpider(scrapy.Spider):
#     name = 'reuters'
#     start_urls=[
#         'https://www.reuters.com/technology/'
#     ]
#
#     def parse(self, response):
#         articles = response.xpath(
#             '//ul[contains(@class, "story-collection")]/li[contains(@class, "story-collection_list-item")]/div[contains(@data-testid, "MediaStoryCard")]')[
#                    :10]  # Limit to 10 stories
#
#         for article in articles:
#             item = NewscrawlerItem()
#
#             # Extracting title
#             title = article.xpath('.//a/@aria-hidden').get()
#
#             # Extracting link
#             link = response.urljoin(article.xpath('.//a/@href').get())
#
#             # Extracting image URL
#             img = article.xpath('.//img/@src').get()
#
#             item['title'] = title
#             item['image'] = img
#             item['url'] = link
#             item['source'] = 'Reuters'
#
#             yield item

#
# class TechSpider(scrapy.Spider):
# 	name = 'technews'
# 	start_urls=[
# 		'https://www.theverge.com/tech'
# 	]
#
# 	def parse(self, response):
# 		div_all_news =  response.xpath("//div[@class='c-compact-river']/div/div")
# 		i=0
# 		for some in div_all_news:
# 			items = NewscrawlerItem()
# 			title =  some.xpath("//div/h2/a/text()")[i].extract()
# 			link = some.xpath("//div/h2/a/@href")[i].extract()
# 			s = some.xpath("//a/div/noscript")[i].extract()
# 			l = s.split('"')
# 			img = l[3]
# 			i+=1
# 			l=[]
# 			items['title'] = title
# 			items['image'] = img
# 			items['url'] = link
# 			items['source'] = 'The Verge'
# 			yield items
# 			if i==12:
# 				break

# class GadgetTech(scrapy.Spider):
#     name = "gadgettech"
#     start_urls = [
#         'https://www.gadgets360.com/news#pfrom=topnav_desk',
#     ]
#
#     def parse(self, response):
#         articles = response.xpath('//div[@class="story_list row margin_b30"]//ul//li')
#
#         for article in articles:
#             item = NewscrawlerItem()
#
#             # Extracting title
#             title = article.xpath('.//span[@class="news_listing"]/text()').get()
#
#             # Extracting image URL
#             img = article.xpath('.//div[@class="thumb"]/a/picture/img/@src').get()
#
#             # Extracting link
#             link = article.xpath('.//div[@class="thumb"]/a/@href').get()
#
#             item['title'] = title.strip() if title else None
#             item['image'] = img.strip() if img else None
#             item['link'] = link.strip() if link else None
#             item['source'] = 'Gadgets 360'
#
#             yield item

# class EconomicTechSpider(scrapy.Spider):
#     name = "ecotech"
#     start_urls = [
#         'https://economictimes.indiatimes.com/tech/information-tech'
#     ]
#
#     def parse(self, response):
#         for story in response.css('.story-box.clearfix')[:10]:  # Limit to 10 stories
#             item = NewscrawlerItem()
#
#             # Extracting title
#             title = story.css('.desc h3 a::text').get()
#
#             # Extracting link
#             link = response.urljoin(story.css('h3 a::attr(href)').get())
#
#             # Extracting image URL
#             img = story.css('.image a img::attr(src)').get()
#
#             # Setting values to item
#             item['title'] = title.strip() if title else "2"
#             item['image'] = img.strip() if img else None
#             item['url'] = link.strip() if link else None
#             item['source'] = 'Economic Times'
#
#             yield item
#
#
#
#
# class IndianTech(scrapy.Spider):
#     name = "indian_tech"
#     start_urls = [
#         'https://indianexpress.com/section/technology/'
#     ]
#
#     def parse(self, response):
#         articles = response.xpath('//div[@class="top-article"]//ul[@class="article-list"]/li')
#
#         for article in articles:
#             item = TechCrawlerItem()
#
#             # Extracting title
#             title = article.xpath('.//h3/a/text()').get()
#
#             # Extracting image URL
#             img = article.xpath('.//figure/a/img/@src').get()
#
#             # Extracting link
#             link = article.xpath('.//figure/a/@href').get()
#
#             item['title'] = title.strip() if title else None
#             item['image'] = img.strip() if img else None
#             item['url'] = response.urljoin(link.strip()) if link else None
#             item['source'] = 'Indian Express - Technology'
#
#             yield item
