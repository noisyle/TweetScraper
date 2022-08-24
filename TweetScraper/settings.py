# !!! # Crawl responsibly by identifying yourself (and your website/e-mail) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
DEFAULT_REQUEST_HEADERS = {
  'Accept': '*/*',
  'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6',
}

# settings for spiders
BOT_NAME = 'TweetScraper'
LOG_LEVEL = 'INFO'

SPIDER_MODULES = ['TweetScraper.spiders']
NEWSPIDER_MODULE = 'TweetScraper.spiders'
ITEM_PIPELINES = {
    # 'TweetScraper.pipelines.SaveToFilePipeline':100,
    'TweetScraper.pipelines.SaveImagePipeline':101,
}

# settings for where to save data on disk
SAVE_TWEET_PATH = './Data/tweet/'
SAVE_USER_PATH = './Data/user/'

# settings for scrapy.pipelines.images.ImagesPipeline
IMAGES_STORE = './Data/image/'

DOWNLOAD_DELAY = 1.0

# settings for selenium
# from shutil import which
# SELENIUM_DRIVER_NAME = 'firefox'
# SELENIUM_BROWSER_EXECUTABLE_PATH = which('firefox')
# SELENIUM_DRIVER_EXECUTABLE_PATH = which('geckodriver')
# SELENIUM_DRIVER_ARGUMENTS=['-headless']  # '--headless' if using chrome instead of firefox
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy_selenium.SeleniumMiddleware': 800
# }

SELENIUM_DRIVER_NAME = 'chrome'
# SELENIUM_BROWSER_EXECUTABLE_PATH = 'chrome.exe'
SELENIUM_DRIVER_EXECUTABLE_PATH = './Driver/chromedriver.exe'
SELENIUM_DRIVER_ARGUMENTS=['--headless']  # '--headless' if using chrome instead of firefox
DOWNLOADER_MIDDLEWARES = {
    'scrapy_selenium.SeleniumMiddleware': 800
}

