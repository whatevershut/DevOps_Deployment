import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def setup_browser():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    return webdriver.Firefox(options=options)

def test_generate_calligraphy():
    driver = setup_browser()
    try:
        driver.get("http://localhost:2000/")


        textarea = driver.find_element(By.NAME, "text")
        textarea.send_keys("Hello World")

        select = Select(driver.find_element(By.NAME, "font"))
        select.select_by_index(1)

        driver.find_element(By.TAG_NAME, "button").click()
        time.sleep(2)

        image = driver.find_element(By.TAG_NAME, "img")
        assert "data:image/png;base64" in image.get_attribute("src")

        print("✅ Image generated successfully")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_generate_calligraphy()
