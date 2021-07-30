from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options=webdriver.ChromeOptions()
options.binary_location=r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
driver = webdriver.Chrome(chrome_options=options)
driver.get("http://www.python.org")