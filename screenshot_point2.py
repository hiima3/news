from assets.pyhon.screenshot_common_utils import *

point2_css_url = 'https://a-three.work/code/python/news/news_point2.css'

driver = initialize_webdriver()

# (driver, cssのurl, 画像データ名)
configure_webpage(driver, point2_css_url, 'screenshot_point2')