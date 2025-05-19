import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os

def setup_browser():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    return webdriver.Chrome(options=options)

def test_wordart_generation_and_download():
    driver = setup_browser()

    try:
        driver.get("http://127.0.0.1:5000/")
        time.sleep(1)

        # Fill in text area
        textarea = driver.find_element(By.NAME, "text")
        textarea.send_keys("Test Download")

        # Choose a font
        select = Select(driver.find_element(By.NAME, "font"))
        select.select_by_index(1)  # Skip disabled option

        # Click generate
        driver.find_element(By.TAG_NAME, "button").click()
        time.sleep(2)  # Wait for image to generate

        # Check if image is displayed
        image = driver.find_element(By.TAG_NAME, "img")
        assert "data:image/png;base64" in image.get_attribute("src")
        print("✅ Image rendered on page.")

        # Check if download link exists
        links = driver.find_elements(By.TAG_NAME, "a")
        download_link = None
        for link in links:
            href = link.get_attribute("href")
            if href and "static/output/" in href:
                download_link = href
                break

        assert download_link is not None, "❌ Download link not found."
        print(f"✅ Download link available: {download_link}")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_wordart_generation_and_download()
