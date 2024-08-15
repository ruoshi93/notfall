from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# 初始化浏览器驱动
driver = webdriver.Chrome()  

# 打开目标网页
driver.get('https://stadt.muenchen.de/terminvereinbarung_/terminvereinbarung_abh.html?cts=1000113')  # 将 'http://example.com' 替换为你想刷新的网页URL

try:
    while True:
        time.sleep(5)  # 每5秒刷新一次页面
        WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, "appointment"))
        )

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "F00e214c9f52bf4cddab8ebc9bbb11b2b"))
        )

        # 等待下拉菜单出现
        select_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "CASETYPES[Notfalltermin UA 35]"))
        )
        select = Select(select_element)
        select.select_by_value("1")

        weiter_button = driver.find_element(By.CLASS_NAME, "WEB_APPOINT_FORWARDBUTTON")
        weiter_button.click()

        WebDriverWait(driver, 10).until(
            EC.url_changes('https://terminvereinbarung.muenchen.de/abh/termin/?cts=1000113')
        )
        driver.refresh()
except KeyboardInterrupt:
    print("停止自动刷新")
finally:
    driver.quit()  # 关闭浏览器
