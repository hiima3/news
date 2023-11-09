from assets.pyhon.screenshot_common_utils import *

# ニュースサイトのURLを入れる

open_css_url = 'https://a-three.work/code/python/news/news_open.css'

# ChromeDriverの初期化  webdriver_setup.py
driver = initialize_webdriver()

# JavaScriptを使用して特定の要素にクラス "active" を追加
elements = driver.find_elements(By.CSS_SELECTOR, '.sentence')  # '.sentence' クラスに合致する要素をすべて取得

# すべての要素に 'active' クラスを追加
for element in elements:
    driver.execute_script("arguments[0].classList.add('active');", element)

# 外部CSSファイルのリンクを作成して追加
open_css_injection_script = f"var link = document.createElement('link'); link.rel = 'stylesheet'; link.href = '{open_css_url}'; document.head.appendChild(link);"

# CSSを追加
driver.execute_script(open_css_injection_script)

# ページのHTMLを取得
page_source = driver.page_source

# HTMLをファイルに保存
with open('assets/html/dynamic.html', 'w', encoding='utf-8') as file:
    file.write(page_source)

# 'dynamic.html' ファイルを読み込む
with open('assets/html/dynamic.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# BeautifulSoupを使用してHTMLを解析
soup = BeautifulSoup(html_content, 'html.parser')

# idが "detail-en" の要素を取得
element = driver.find_element(By.ID, 'detail-en')

# テキストを取得
detail_en_text = element.text

# HTMLをファイルに保存
with open('txt.html', 'w', encoding='utf-8') as file:
    file.write(detail_en_text)

# ブラウザを閉じる
driver.quit()
