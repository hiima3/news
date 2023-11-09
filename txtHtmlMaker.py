from assets.pyhon.screenshot_common_utils import *

########## txt.html 作成
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
with open('assets/html/souce.html', 'w', encoding='utf-8') as file:
    file.write(page_source)

# 'txt.html' ファイルを読み込む
with open('assets/html/souce.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# BeautifulSoupを使用してHTMLを解析
soup = BeautifulSoup(html_content, 'html.parser')

# idが "detail-en" の要素を取得
element = driver.find_element(By.ID, 'detail-en')

# テキストを取得
detail_en_text = element.text

# HTMLをファイルに保存
with open('assets/html/txt.html', 'w', encoding='utf-8') as file:
    file.write(detail_en_text)

########## txt.html 編集
# 'txt.html' ファイルを読み込む
with open('assets/html/txt.html', 'r', encoding='utf-8') as file:
    lines = file.readlines()

####################

# 行がちょうど3文字で "解説" という文字列が含まれた行を検索
i = 0
while i < len(lines):
    if len(lines[i]) == 3 and "解説" in lines[i]:
        # "解説" を削除
        lines[i] = lines[i].replace("解説", "")

        # 次の2行が存在するか確認してから削除
        if i - 2 < len(lines):
            del lines[i - 2]
            # 改行を挿入
            lines.insert(i - 2, '\n')
            lines.insert(i - 3, '0:\n')

            # 次の2行が存在するか確認してから削除
            if i - 4 < len(lines):
                # lines.insert(i - 3, '\n')
                if len(lines[i - 4]) >= 2:
                    # 0: の上の行に文字が2文字以上入っている場合、改行を挿入
                    lines.insert(i - 3, '\n')
        else:
            break  # 2行下の行がない場合はループを終了

    else:
        i += 1

del lines[0]

####################
# 新しいファイルにデータを書き込み
with open('assets/html/txt.html', 'w', encoding='utf-8') as new_file:
    new_file.writelines(lines)

# ブラウザを閉じる
driver.quit()
