import scrapy
import string
import lxml
from lxml import etree

from tutorial import items


class LianjiaSpider(scrapy.Spider):
    name = 'Lianjia'
    allowed_domains = ['sz.lianjia.com']
    start_urls = ['https://sz.lianjia.com/ershoufang/dapengxinqu/pg1/']

    baseURL = "https://sz.lianjia.com/ershoufang/dapengxinqu/"
    offset = 1

    def parse(self, response, **kwargs):

        filename = "SpiderResult"
        with open(filename, 'ab') as f:
            f.write(response.body)

        item = items.TutorialItem()
        segment = response.xpath("(//a[@data-el='region'])/text()").extract()
        length = len(segment) + 1
        for i in range(1, length):
            house_first_name_str = "(//a[@data-el='region'])[" + str(i) + "]/text()"
            house_last_name_str = "(//a[@data-el='region']/following-sibling::a)[" + str(i) + "]/text()"
            house_info_str = "(//div[@class='houseInfo'])[" + str(i) + "]/text()"
            #house_unit_price_str = "(//div[@data-price='0']//span)[" + str(i) + "]/text()"
            house_unit_price_str = "(//div[@class='unitPrice']//span)[" + str(i) + "]/text()"
            item["HouseFirstName"] = response.xpath(house_first_name_str).extract()
            item["HouseLastName"] = response.xpath(house_last_name_str).extract()
            item["HouseInfo"] = response.xpath(house_info_str).extract()
            item["HouseUnitPrice"] = response.xpath(house_unit_price_str).extract()
            print("抓取完毕一条")
            yield item

        if self.offset < 101:
            self.offset += 1
            url = self.baseURL + "pg" + str(self.offset) + "/"
            yield scrapy.Request(url, callback=self.parse)
            print("抓取完毕一页")

        pass
