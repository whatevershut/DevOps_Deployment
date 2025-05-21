import time
import tempfile
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def setup_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")
    return webdriver.Chrome(options=options)

def test_generate_calligraphy():
    driver = setup_browser()
    try:
        driver.get("http://localhost:2000/")
        textarea = driver.find_element(By.NAME, "text")
        textarea.send_keys("Hello World")
        select_element = Select(driver.find_element(By.NAME, "font"))
        select_element.select_by_index(1)
        driver.find_element(By.TAG_NAME, "button").click()
        time.sleep(2)
        image = driver.find_element(By.TAG_NAME, "img")
        assert "data:image/png;base64" in image.get_attribute("src")
        print("✅ Image generated successfully")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_generate_calligraphy()
