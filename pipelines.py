# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import traceback

import pymysql

from twisted.internet import defer
from twisted.enterprise import adbapi

class HousePipeline(object):
    def process_item(self, item, spider):
        return item
class MysqlWriterPipeline(object):

    def __init__(self):
        conn_kwargs = {
            'host': '127.0.0.1',
            'user': 'root',
            'password': 'q1w2e3r4t5',
            'database': 'test',
            'cursorclass': pymysql.cursors.DictCursor
        }
        self.dbpool = adbapi.ConnectionPool('pymysql',
                                            charset='utf8',
                                            use_unicode=True,
                                            connect_timeout=5,
                                            **conn_kwargs)

    def close_spider(self, spider):

        self.dbpool.close()

    @defer.inlineCallbacks
    def process_item(self, item, spider):
        """Processes the item. Does insert into MySQL"""

        logger = spider.logger

        try:
            yield self.dbpool.runInteraction(self.do_replace, item)
        except pymysql.OperationalError:
            if self.report_connection_error:
                logger.error("Can't connect to MySQL" )
                self.report_connection_error = False
        except:
            print(traceback.format_exc())

        # Return the item for the next stage
        defer.returnValue(item)



    @staticmethod
    def do_replace(tx, item):
        """Does the actual REPLACE INTO"""

        sql = "REPLACE INTO fangtianxia (name, adress, storey, area, level, price, wuye_price)VALUES (%s, %s, %s, %s, %s, %s, %s)"

        args = (
            item["name"],
            item["adress"],
            item["storey"],
            item["area"],
            item["level"],
            item["price"],
            item["wuye_price"]
        )
        tx.execute(sql, args)

