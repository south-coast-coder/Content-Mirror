from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
#from selenium.webdriver.remote.webelement import WebElement
import time
 #add open file read ..if channel name user entered not in add flag - then search for channel name if it exists then open file adn write it otherwise exit with error
user_search='Py con' #make this accept options from command line in future so users can tell which channels to search for
options=webdriver.ChromeOptions()
options.set_headless
options.binary_location=r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"  # to change in future update - let user choose their browser and maybe bundle the driver/s with installation?
driver = webdriver.Chrome(executable_path=r'C:\Users\charlie\chrome\chromedriver.exe', options=options)
driver.get("http://www.youtube.com")
time.sleep(10)
try: driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button').click()
#above the issue is that sometimes google uses diff screen find x path for the OTHER accept it uses as well
except:
    print(str(driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[5]/div[2]/ytd-button-renderer[2]').get_attribute("innerHTML"))) #This SHOULD work for alternative screen youtube provides
    driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[5]/div[2]/ytd-button-renderer[2]').click()
    
time.sleep(10)
search=driver.find_element_by_xpath('//*[@id="search"]')
search.send_keys(user_search)
search.send_keys(Keys.RETURN)
time.sleep(200) #needed to add this so it waits long enough for page to load - before it was loading OLD dom
driver.refresh()
print("current url="+str(driver.current_url))
#WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "text")))
#chilledCowElem = driver.find_element_by_css_selector("#text style-scope ytd-channel-name")

titles=driver.find_elements_by_xpath('//*[@id="text"]')
print(titles[2].get_attribute("innerHTML"))
titles[2].click()      #This used to always be the one with videos but has changed so added function above
print(titles[2].get_attribute("innerHTML"))
time.sleep(200)
driver.refresh()
driver.find_element_by_xpath('//*[@id="tabsContent"]/tp-yt-paper-tab[2]/div').click() #this clicks on video tab on channel
time.sleep(200) 
driver.refresh()
while True:      #this block ensures page has scrolled to bottom (and uses time sleep to make sure waits for content to load) - package into function
    scroll_height = 2000
    document_height_before = driver.execute_script("return document.documentElement.scrollHeight")
    driver.execute_script(f"window.scrollTo(0, {document_height_before + scroll_height});")
    time.sleep(1.5)
    document_height_after = driver.execute_script("return  document.documentElement.scrollHeight")
    if document_height_after == document_height_before:
        break
time.sleep(10)
videos=driver.find_elements_by_xpath('//*[@id="video-title"]')
print(videos[0].get_attribute("innerHTML"))
print(videos[1].get_attribute("innerHTML"))

print(videos[2].get_attribute("innerHTML"))
for video in videos:
    print(video.get_attribute("innerHTML"))





#print("this is title"+str(title.get_attribute('innerHTML')))
#TxtBoxContent=driver.find_element_by_id("text").get_attribute("innerHTML")
#print("This is Content:" + str(TxtBoxContent))
#driver.close()



#//*[@id="text"]
    

