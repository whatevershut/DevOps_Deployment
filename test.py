from selenium import webdriver
driver = webdriver.Remote("http://localhost:4444/wd/hub", options=webdriver.ChromeOptions())
driver.get("http://localhost:8080")  # Replace with your app URL
assert "My App" in driver.title
driver.quit()
