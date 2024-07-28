from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions

def main():
    # EdgeDriver beállítása
    edge_driver_path = '/usr/local/bin/msedgedriver'
    edge_binary_path = '/usr/bin/microsoft-edge'
    service = EdgeService(executable_path=edge_driver_path)
    options = EdgeOptions()
    options.binary_location = edge_binary_path
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--remote-debugging-port=9222')
    options.add_argument('--disable-gpu')

    # Az Edge böngésző indítása
    driver = webdriver.Edge(service=service, options=options)

    # Itt folytathatjuk a Selenium kódunkat
    driver.get('http://www.google.com')
    print(driver.title)
    driver.quit()

if __name__ == "__main__":
    main()
