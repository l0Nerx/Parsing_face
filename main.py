from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

url = 'https://this-person-does-not-exist.com/en'

os.makedirs('parser/img', exist_ok=True)

num_images = 69

chromedriver_path = '/path/to/chromedriver' 

service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

for i in range(num_images):    
    driver.get(url)

    driver.implicitly_wait(2)
    img = driver.find_element(By.CSS_SELECTOR, '#avatar')

    image_url = img.get_attribute('src')

    file_path = f'parser/img/screenshot{i + 1}.png'

    driver.get(image_url)

    with open(file_path, 'wb') as file:
        file.write(driver.find_element(By.TAG_NAME, 'img').screenshot_as_png)
        
    print(f"Downloaded image /{num_images}: {file_path}")
    driver.refresh()

driver.quit()