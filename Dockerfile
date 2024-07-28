FROM ubuntu:20.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    gnupg2 \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Add Google Chrome repository
RUN curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list

# Install Google Chrome
RUN apt-get update && apt-get install -y \
    google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Get the version of Google Chrome
RUN CHROME_VERSION=$(google-chrome --version | grep -oP '\d+\.\d+\.\d+\.\d+') && \
    echo "Chrome version: $CHROME_VERSION" && \
    wget -q "https://chromedriver.storage.googleapis.com/$CHROME_VERSION/chromedriver_linux64.zip" && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/local/bin/ && \
    rm chromedriver_linux64.zip

# Set display port for XVFB
ENV DISPLAY=:99

# Install Xvfb
RUN apt-get update && apt-get install -y \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Copy the project files into the container
COPY . /app
WORKDIR /app

# Install Python dependencies
RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install -r requirements.txt

# Run the application
CMD ["xvfb-run", "-a", "python3", "main.py"]
