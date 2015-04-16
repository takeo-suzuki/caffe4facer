# coding: utf-8

from datetime import datetime

from scrapy.contrib.spiders import SitemapSpider
from scrapy.selector import Selector

from caffescrapy.items import CaffescrapyItem


class ToyotaSpider(SitemapSpider):
    name = 'Toyota'
    allowed_domains = ['toyota.jp']
    sitemap_urls = [
        # ここにはrobots.txtのURLを指定してもよいが、
        # 無関係なサイトマップが多くあるので、今回はサイトマップのURLを直接指定する。
        'http://toyota.jp/sitemap.xml',
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)

        item = HunterItem()
        image_urls = hxs.select('//img/@src').extract()
        item['image_urls'] = ['http://toyota.jp/'+x for x in image_urls]
        return item
