import scrapy
from ..items import SportscrawlerItem
from news.models import SHeadline
from sportscrawler.spiders import sports_spider
from sportscrawler import pipelines


class EconomicSportsSpider(scrapy.Spider):
    name = "ecosports"
    start_urls = [
        'https://economictimes.indiatimes.com/news/sports'
    ]

    def parse(self, response):
        for story in response.xpath('//div[@class="eachStory"]')[:10]:  # Limit to 10 stories
            item = SportscrawlerItem()

            # Extracting title
            title = story.xpath('.//span[@class="imgContainer"]/img/@alt').get()

            # Extracting link
            link = response.urljoin(story.xpath('.//@href').get())

            # Extracting image URL
            img = story.xpath('.//span[@class="imgContainer"]/img/@src').get()

            # Setting values to item
            item['title'] = title
            item['image'] = img
            item['url'] = link
            item['source'] = 'Economic Times'

            yield item

class SportsSpider(scrapy.Spider):
    name = "sports"
    start_urls = [
        'https://indianexpress.com/section/sports/'
    ]

    def parse(self, response):
        articles = response.xpath('//div[@id="section"]/div[@class="container"]/div[@class="row"]/div[@class="leftpanel"]/div[@class="nation"]/div[contains(@class, "articles")]')

        for article in articles:
            item = SportscrawlerItem()

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
            yield item
class HtimesSpider(scrapy.Spider):
	name = "Htimes"
	start_urls = [
		'https://www.hindustantimes.com/other-sports/'
	]

	def parse(self, response):

		div_all_news = response.xpath("//section[@class='container']/div[@class='news-area more-news-section']/div/div[@class='col-sm-7 col-md-8 col-lg-9']/div[@id='scroll-container']/ul[@class='latest-news-morenews more-latest-news more-separate newslist-sec']/li/div")
		i=0
		j=0
		for some in div_all_news:
			items = SportscrawlerItem()
			title = some.xpath("//div[@class='media-body']/div/a/text()")[i].extract()
			link = some.xpath("//div[@class='media-body']/div/a/@href")[i].extract()
			if i<3:
				img = some.xpath("//div[@class='media-left']/div/a/img/@src")[i].extract()
			else:
				img = some.xpath("//div[@class='media-left']/a/img/@src")[j].extract()
				j+=1
			i+=1 
			items["title"] = title
			items["image"] = img
			items["url"] = link
			items['source'] = 'Hindustan'
			yield items
