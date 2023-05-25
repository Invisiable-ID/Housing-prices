# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class TutorialPipeline:

    columns = ['HouseFirstName', 'HouseLastName', 'HouseInfo', 'HouseUnitPrice']
    file_name = 'Lianjia.csv'
    file = open(file_name, 'w', newline='', encoding='utf-8-sig')
    writer = csv.DictWriter(file, columns)

    def __int__(self):
        self.writer.writeheader()

    def process_item(self, item, spider):
        self.writer.writerow(item)
        print(len(item))
        return item

    #def close_spider(self, spider):
        #self.file.close()
