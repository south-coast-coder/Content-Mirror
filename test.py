from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import os
import sys
import youtube_dl

#from selenium.webdriver.remote.webelement import WebElement
import time
 #add open file read ..if channel name user entered not in add flag - then search for channel name if it exists then open file adn write it otherwise exit with error
user_search='fightTIPS' #make this accept options from command line in future so users can tell which channels to search for
user_file=user_search +'.json'
#Here need to access downloaded vids doc 
downloaded_vids=["Po the Librarian is an Obnoxious, Midwit Bore",' Grigori Perelman is an Idiot, with Ivan the Heathen']
data_base = {}
def exists_json(file): #run this before interacting with any json file in order to check actually has content first - if not need to dump {} into it as this is bare minimum needed for json file to work
   if os.path.exists(file):
      with open(file,'a+') as f:
         try:
            data=json.open(f)
         except:
            print("no data")
            with open(file, 'w+') as f:
               initial={'videos':[]}
               json.dump(initial,f)
               print("dumped")         
   else:
      with open(file, 'w+') as f:
         initial={'videos':[]}
         json.dump(initial,f)
         print("dumped")         
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
print("returning.....")
time.sleep(200) #needed to add this so it waits long enough for page to load - before it was loading OLD dom
driver.refresh()
print("current url="+str(driver.current_url))
#WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "text")))
#chilledCowElem = driver.find_element_by_css_selector("#text style-scope ytd-channel-name")
try:
    titles=driver.find_elements_by_xpath('//*[@id="text"]')
    for title in titles [0:5]:
        print("title="+ title.get_attribute("innerHTML"))
        if title.get_attribute("innerHTML") == user_search:
         usetitle=title
         title.click()
         break
    
    if usetitle.get_attribute("innerHTML") != user_search:   #maybe add a regex here or force all characters to lower to ensure capture as much as poss
                                               print("No matching Channel Found please check you have typed the name correctly \n exiting -------")
                                               time.sleep(5)
                                               sys.exit(1)
    exists_json(user_file)
    jsonFile = open(user_file, "r")
    data = json.load(jsonFile)
    jsonFile.close()
except:
    print("No channel with name " + user_search +" found, exiting program.......")
    time.sleep(5)
    sys.exit(1)

time.sleep(200)
driver.refresh()
driver.find_element_by_xpath('//*[@id="tabsContent"]/tp-yt-paper-tab[2]/div').click() #this clicks on video tab on channel
time.sleep(200) 
driver.refresh()
while True:      #this block ensures page has scrolled to bottom (and uses time sleep to make sure waits for content to load) - package into function
    scroll_height = 2000
    document_height_before = driver.execute_script("return document.documentElement.scrollHeight")
    driver.execute_script(f"window.scrollTo(0, {document_height_before + scroll_height});")
    time.sleep(5)
    document_height_after = driver.execute_script("return  document.documentElement.scrollHeight")
    if document_height_after == document_height_before:
        break
time.sleep(10)
videos=driver.find_elements_by_xpath('//*[@id="video-title"]')
print(videos[0].get_attribute("innerHTML"))
print(videos[1].get_attribute("innerHTML"))

print(videos[2].get_attribute("innerHTML"))
def dict_search(dict, search):
    for item in dict:
        if item == search:
            return True
        return False

#should run below twice - first to check how many need downloading, then to prompt user if they want to donwload all (i.e if 100 vids want to download - could set a limit at beggining or add a CL option to silence all of these options and download as many as necessary)    
for video in videos[0:5]:   #Here we are going to test by downloading any videos that MATCH - need to change to opposite when working
    text=video.get_attribute("innerHTML")
    href=video.get_attribute("href")
    print(video.get_attribute("innerHTML"))
    print(href)
    result=dict_search(data['videos'],text) #this runs function that checks if this video has already been downloaded and title stored in json file
    print("result="+str(result))
    if result == False or result == None:
        print("NOT PRESENT DOWNLOAD ----")
        ydl_opts = {'format': 'best','external-downloader':'aria2c','outtmpl':'%s.mp4' % text}  #using aria2c as external downloader massively speeds up download
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
              ydl.download(["%s" % href]) 
              try:
                jsonFile = open(user_file, "r")  #write downloaded vid to json file so don't re-download in future
                data = json.load(jsonFile)
                jsonFile.close()
                data.update({'%s' %text})
                with open(user_file, 'r+') as f:
                            f.seek(0)        # <--- should reset file position to the beginning.
                            json.dump(data, f)
              except:
                print("failed to load json file")
    else:
            print("already matched")
        
#now that is has whole page loaded and list of vids its should check this against JSON list in for loop (i,e set a true or false then for item in 'list.json' for item in ....if item..i.e check if matches ..if no match add to another list ..when done for all then get the selenium link for each and download it then conver and upload to telegram..once uploaded add to uploaded list)





#print("this is title"+str(title.get_attribute('innerHTML')))
#TxtBoxContent=driver.find_element_by_id("text").get_attribute("innerHTML")
#print("This is Content:" + str(TxtBoxContent))
#driver.close()



#//*[@id="text"]
    

 