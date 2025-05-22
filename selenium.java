ChromeOptions options = new ChromeOptions();
options.setBinary("/opt/chrome-for-testing/chrome-linux64/chrome");
options.addArguments("--headless");
options.addArguments("--no-sandbox");
options.addArguments("--disable-dev-shm-usage");

WebDriver driver = new ChromeDriver(options);
