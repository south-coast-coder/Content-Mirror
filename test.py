from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.remote.webelement import WebElement
import time

user_search='Thomas Baden Riess' #make this accept options from command line in future so users can tell which channels to search for
options=webdriver.ChromeOptions()
options.set_headless
options.binary_location=r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"  # to change in future update - let user choose their browser and maybe bundle the driver/s with installation?
driver = webdriver.Chrome(executable_path=r'C:\Users\charlie\chrome\chromedriver.exe', options=options)
driver.get("http://www.youtube.com")
try: driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button').click()
#above the issue is that sometimes google uses diff screen find x path for the OTHER accept it uses as well
except:
    pass
time.sleep(10)
search=driver.find_element_by_css_selector('input#search')
search.send_keys(user_search)
search.send_keys(Keys.RETURN)
time.sleep(200) #needed to add this so it waits long enough for page to load - before it was loading OLD dom
driver.refresh()
print("current url="+str(driver.current_url))
#WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "text")))
#chilledCowElem = driver.find_element_by_css_selector("#text style-scope ytd-channel-name")

titles=driver.find_elements_by_xpath('//*[@id="text"]')
print(titles[2].get_attribute("innerHTML"))



#print("this is title"+str(title.get_attribute('innerHTML')))
#TxtBoxContent=driver.find_element_by_id("text").get_attribute("innerHTML")
#print("This is Content:" + str(TxtBoxContent))
#driver.close()



#//*[@id="text"]
    

