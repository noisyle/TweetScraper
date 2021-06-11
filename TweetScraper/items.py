from scrapy import Item, Field


class Tweet(Item):
    id_ = Field()
    raw_data = Field()

class User(Item):
    id_ = Field()
    raw_data = Field()

class Image(Item):
    query = Field()
    image_ids = Field()
    image_urls = Field()
