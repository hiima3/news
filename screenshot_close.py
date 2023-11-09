from assets.pyhon.screenshot_common_utils import *

close_css_url = 'https://a-three.work/code/python/news/news_close.css'

driver = initialize_webdriver()
# (driver, cssのurl, 画像データ名)
configure_webpage(driver, close_css_url, 'screenshot_close')

