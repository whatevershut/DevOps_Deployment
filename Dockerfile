FROM debian:bookworm-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    unzip \
    wget \
    fonts-liberation \
    libxss1 \
    libappindicator3-1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libnspr4 \
    libnss3 \
    libxcomposite1 \
    libxrandr2 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libx11-xcb1 \
    libxcb1 \
    xdg-utils \
    ca-certificates \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Add Google Chrome signing key and repository
RUN mkdir -p /etc/apt/keyrings && \
    curl -fsSL https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /etc/apt/keyrings/google.gpg && \
    echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/google.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

# Install ChromeDriver matching the installed Chrome version
RUN CHROME_VERSION=$(google-chrome-stable --version | grep -oP "\d+\.\d+\.\d+") && \
    DRIVER_VERSION=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_${CHROME_VERSION}") && \
    wget -O /tmp/chromedriver.zip "https://chromedriver.storage.googleapis.com/${DRIVER_VERSION}/chromedriver_linux64.zip" && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver && \
    rm -rf /tmp/chromedriver.zip

# Optional: Set display environment variable for headless usage
ENV DISPLAY=:99

# Set default command
CMD ["google-chrome-stable", "--version"]
