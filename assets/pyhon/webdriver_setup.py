from selenium import webdriver

def initialize_webdriver():
    # ChromeDriverの初期化
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--headless")

    # ブラウザを初期化
    driver = webdriver.Chrome(options=options)

    with open("url.txt", 'r') as file:
        url = file.read().strip()

    # ウェブサイトにアクセス
    driver.get(url)

    return driver
