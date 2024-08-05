import scrapy
import random  # Import random module
from ..items import EconomycrawlerItem
from news.models import EHeadline
from economycrawler.spiders import economy_spider
from economycrawler import pipelines

class EconomySpider(scrapy.Spider):
    name = "economy"
    start_urls = [
        'https://economictimes.indiatimes.com/markets/stocks/news'
    ]

    def parse(self, response):
        div_all_news = response.xpath("//div[@class='eachStory']")
        items = []  # List to store items
        for some in div_all_news:
            item = EconomycrawlerItem()

            # Extracting title
            title = some.xpath(".//h3/a/text()").get()

            # Extracting link
            link = response.urljoin(some.xpath(".//h3/a/@href").get())

            # Extracting image URL
            img = some.xpath(".//span[contains(@class, 'imgContainer')]/img/@src").get()

            item["title"] = title.strip() if title else None
            item["image"] = img.strip() if img else None
            item["url"] = link.strip() if link else None
            item['source'] = 'Economic Times'
            items.append(item)  # Append item to the list

        random.shuffle(items)  # Shuffle the list of items
        for item in items:
            yield item

class ExpressSpider(scrapy.Spider):
    name = "express"
    start_urls = [
        'https://indianexpress.com/section/business/economy/'
    ]

    def parse(self, response):
        articles = response.xpath('//div[@id="section"]//div[contains(@class, "articles")]')
        items = []  # List to store items
        for article in articles:
            item = EconomycrawlerItem()

            # Extracting title
            title = article.xpath('.//h2[@class="title"]/a/@title').get()

            # Extracting link
            link = article.xpath('.//h2[@class="title"]/a/@href').get()

            # Extracting image URL
            img = article.xpath('.//div[@class="snaps"]/a/img/@src').get()

            item['title'] = title
            item['image'] = img
            item['url'] = link
            item['source'] = 'Indian Express'
            items.append(item)  # Append item to the list

        random.shuffle(items)  # Shuffle the list of items
        for item in items:
            yield item
