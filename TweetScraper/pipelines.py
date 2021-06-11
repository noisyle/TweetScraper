import os, logging, json
from scrapy.utils.project import get_project_settings

from TweetScraper.items import Tweet, User, Image
from TweetScraper.utils import mkdirs

from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request

logger = logging.getLogger(__name__)
SETTINGS = get_project_settings()

class SaveToFilePipeline(object):
    ''' pipeline that save data to disk '''

    def __init__(self):
        self.saveTweetPath = SETTINGS['SAVE_TWEET_PATH']
        self.saveUserPath = SETTINGS['SAVE_USER_PATH']
        mkdirs(self.saveTweetPath) # ensure the path exists
        mkdirs(self.saveUserPath)


    def process_item(self, item, spider):
        if isinstance(item, Tweet):
            savePath = os.path.join(self.saveTweetPath, item['id_'])
            if os.path.isfile(savePath):
                pass # simply skip existing items
                # logger.debug("skip tweet:%s"%item['id_'])
                ### or you can rewrite the file, if you don't want to skip:
                # self.save_to_file(item,savePath)
                # logger.debug("Update tweet:%s"%item['id_'])
            else:
                self.save_to_file(item,savePath)
                logger.debug("Add tweet:%s" %item['id_'])

        elif isinstance(item, User):
            savePath = os.path.join(self.saveUserPath, item['id_'])
            if os.path.isfile(savePath):
                pass # simply skip existing items
                # logger.debug("skip user:%s"%item['id_'])
                ### or you can rewrite the file, if you don't want to skip:
                # self.save_to_file(item,savePath)
                # logger.debug("Update user:%s"%item['id_'])
            else:
                self.save_to_file(item, savePath)
                logger.debug("Add user:%s" %item['id_'])

        else:
            logger.info("Item type is not recognized! type = %s" %type(item))


    def save_to_file(self, item, fname):
        ''' input: 
                item - a dict like object
                fname - where to save
        '''
        with open(fname + '.json', 'w', encoding='utf-8') as f:
            json.dump(dict(item), f, ensure_ascii=False)


class ImgflipPipeline(ImagesPipeline):
    ''' pipeline that save image to disk '''

    def get_media_requests(self, item, info):
        if isinstance(item, Image):
            image_ids = item['image_ids']
            for i, url in enumerate(item['image_urls']):
                yield Request(url, meta={'image_id': image_ids[i]})


    def file_path(self, request, response=None, info=None, *, item=None):
        return f'%s.jpg' % request.meta['image_id']

