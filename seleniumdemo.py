# Pythonでググる

import time

# seleniumライブラリが必要です "pip install selenium"とターミナルで打ちます
from selenium import webdriver

# Chrome自動操作に必要なchromedriver
# http://chromedriver.chromium.org/downloads
driver = webdriver.Chrome('/Users/okaken/chromedriver')

# getでサイトを開けます
# 今回はGoogleを開いてみる
driver.get('https://www.google.com/')

# 2秒待つ
time.sleep(2)

# 名前から要素を探す
search_box = driver.find_element_by_name("q")

# ShibaLabとキーを送信
search_box.send_keys('ShibaLab')

# 決定
search_box.submit()
