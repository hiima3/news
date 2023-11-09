from assets.pyhon.screenshot_common_utils import *

point1_css_url = 'https://a-three.work/code/python/news/news_point1.css'

driver = initialize_webdriver()
# (driver, cssのurl, 画像データ名)
configure_webpage(driver, point1_css_url, 'screenshot_point1')