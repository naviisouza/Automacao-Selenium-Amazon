from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(r'./chromedriver.exe')  # Caminho para o ChromeDriver
driver = webdriver.Chrome(service=service)
driver.get("https://www.youtube.com/")