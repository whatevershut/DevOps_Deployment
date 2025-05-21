import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Set up Selenium WebDriver
def setup_browser():
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")
    return webdriver.Chrome(options=options)

def test_generate_calligraphy():
    driver = setup_browser()

    try:
        driver.get("http://localhost:2000/")

        # Fill in the textarea with text
        textarea = driver.find_element(By.NAME, "text")
        textarea.send_keys("Hello World")

        # Select the first available font
        select_element = Select(driver.find_element(By.NAME, "font"))
        select_element.select_by_index(1)  # Skip the first (disabled) option

        # Click the Generate button
        driver.find_element(By.TAG_NAME, "button").click()

        time.sleep(2)  # Wait for image generation

        # Check if image was generated
        image = driver.find_element(By.TAG_NAME, "img")
        assert "data:image/png;base64" in image.get_attribute("src")

        print("✅ Image generated successfully")

    finally:
        driver.quit()
    
if __name__ == "__main__":
    test_generate_calligraphy()

