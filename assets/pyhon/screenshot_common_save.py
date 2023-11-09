import os
from assets.pyhon.config import screenshot_directory

def configure_webpage(driver, css_url, screenshot_name):
    # スクショが切れている場合
    screen_height = 10000

    # 外部CSSファイルのリンクを作成して追加
    css_injection_script = f"var link = document.createElement('link'); link.rel = 'stylesheet'; link.href = '{css_url}'; document.head.appendChild(link);"

    # CSSを追加
    driver.execute_script(css_injection_script)

    # ズームレベルを設定（175%）
    driver.execute_script(f"document.body.style.zoom = '1.75';")

    # ウィンドウサイズ指定
    driver.set_window_size(1920, screen_height)

    # スクリーンショットを取得
    screenshot_path = os.path.join(screenshot_directory, screenshot_name + '.png')
    driver.save_screenshot(screenshot_path)

    # ブラウザを閉じる
    driver.quit()
