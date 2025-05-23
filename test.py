from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Replace with your EC2 public IP or domain
URL = "http://13.218.27.182"

# Initialize browser (make sure chromedriver is in PATH)
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Runs browser in headless mode.
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)

try:
    driver.get(URL)
    time.sleep(2)  # Wait for page to load

    # Check the text content
    phase_text = driver.find_element(By.CLASS_NAME, "phase").text
    assert "Phase 4" in phase_text, f"Expected 'Phase 4' in page but found: {phase_text}"

    print("Test Passed: Phase 4 found on front.html")

except Exception as e:
    print(f"Test Failed: {e}")

finally:
    driver.quit()
