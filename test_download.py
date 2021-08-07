from __future__ import unicode_literals
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time

import youtube_dl

downloaded_vids=["Adrien Abauzit | Analyse de la décision du Conseil Constitutionnel | Bilan de saison"]
#Set up the Driver
options=webdriver.ChromeOptions()
options.set_headless
options.binary_location=r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"  # to change in future update - let user choose their browser and maybe bundle the driver/s with installation?
driver = webdriver.Chrome(executable_path=r'C:\Users\charlie\chrome\chromedriver.exe', options=options)
driver.get("https://www.youtube.com/c/RadioAth%C3%A9na/videos")
#Run a function to ensure page is fully scrolled
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
""" for video in videos:   #Here we are going to test by downloading any videos that MATCH - need to change to opposite when working
    text=video.get_attribute("innerHTML")
    for item in downloaded_vids:
        print("")
        print(item)
        print(text)
        print("")
        if item==text:
            print("MAAAAAAAAATTTTTCCCCCCCHHHHH")
        else:
            print("not")  """
print("testing....")
#def remove_non_ascii_1(text):

  #  return ''.join(i for i in text if ord(i)<128)
#vid_stripped=remove_non_ascii_1(videos[0].get_attribute('innerHTML'))
#vid_stripped2=vid_stripped.strip(" ")
vid_stripped2=videos[0].get_attribute('innerHTML')
vid_stripped3=vid_stripped2[2:]
href=videos[0].get_attribute('href')
print(href)
if vid_stripped3 == downloaded_vids[0]:
    print("success!")
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                      ydl.download([href])
else:
    print("failure")
print(vid_stripped3)
print(downloaded_vids[0])
href=videos[0].get_attribute('href')


