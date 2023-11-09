from assets.pyhon.screenshot_common_utils import *

#################### url取得
# ChromeDriverの初期化  webdriver_setup.py
driver = initialize_webdriver()

# 要素が読み込まれるのを待つ
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'gendai-hd2-info--title')))

# ページのHTMLを取得
page_source = driver.page_source

# HTMLをファイルに保存
with open('assets/html/geturl.html', 'w', encoding='utf-8') as file:
    file.write(page_source)

# 'geturl.html' ファイルを読み込む
with open('assets/html/geturl.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# BeautifulSoupを使用してHTMLを解析
soup = BeautifulSoup(html_content, 'html.parser')

# .gendai-hd2-info--title クラスを持つ要素を取得
title_element = soup.find(class_='gendai-hd2-info--title')

# タイトルテキストを取得
if title_element:
    title_text = title_element.text[:3]  # 最初の5文字を取得
else:
    title_text = "title_text not found"

print("HTMLファイルから取得したタイトルテキスト:", title_text)

# スクショがとれるかテスト
# スクリーンショットを取得
screenshot_directory = 'assets/'
screenshot_filename__point2 = 'screenshot_point2.png'
screenshot_path__point2 = os.path.join(screenshot_directory, screenshot_filename__point2)
driver.save_screenshot(screenshot_path__point2)


# ブラウザを閉じる
driver.quit()