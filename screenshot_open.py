from assets.pyhon.screenshot_common_utils import *

open_css_url = 'https://a-three.work/code/python/news/news_open.css'

# ChromeDriverの初期化  webdriver_setup.py
driver = initialize_webdriver()

# JavaScriptを使用して特定の要素にクラス "active" を追加
elements = driver.find_elements(By.CSS_SELECTOR, '.sentence')  # '.sentence' クラスに合致する要素をすべて取得

# すべての要素に 'active' クラスを追加
for element in elements:
    driver.execute_script("arguments[0].classList.add('active');", element)

configure_webpage(driver, open_css_url, 'screenshot_open')
