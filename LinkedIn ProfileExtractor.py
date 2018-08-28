
# coding: utf-8

# In[1]:


import os 
import time
import pandas as pd
from shutil import move

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# In[2]:


driverPath = r'C:/LinkedInData/chromedriver_win32/chromedriver.exe'
os.environ["webdriver.chrome.driver"] = driverPath
download_dirs = r'C:/LinkedInData/Profiles/'

options = webdriver.ChromeOptions()

profiles = {"download.default_directory": download_dirs}
options.add_experimental_option("prefs", profiles)

driver = webdriver.Chrome(executable_path= driverPath, chrome_options=options)

userid = 'aakashg80@gmail.com'
password = 'C0n7r0l&P0wer'


# In[3]:


driver.get("https://www.linkedin.com")

driver.implicitly_wait(6)
driver.find_element_by_xpath("""//*[@id="login-email"]""").send_keys(userid)
driver.find_element_by_xpath("""//*[@id="login-password"]""").send_keys(password)
driver.find_element_by_xpath("""//*[@id="login-submit"]""").click()


# In[4]:


Links = pd.read_excel('C:/LinkedInData/LinkedinLinks.xlsx')


# In[5]:


for idx, row in Links.iterrows():
    urlLink = row['Links']
    name = '_'.join(row['Name'].split())
    
    print(urlLink)
    driver.get(urlLink)
    driver.implicitly_wait(10)
    
    buttonList = driver.find_elements(By.XPATH, '//button')
    print(len(buttonList))
    for button in buttonList:
        if 'overflow-toggle' in button.get_attribute('class'):
            try:
                print("More Actions")
                button.click()
            except:
                print('Error on Click of More Actions')
                
    driver.implicitly_wait(10)
    buttonList2 = driver.find_elements(By.XPATH, '//button')
    print(len(buttonList2))
    for button in buttonList2:
        if 'save-to-pdf' in button.get_attribute('class'):
            try:
                print("Save to PDF")
                button.click()
            except:
                print("Error on Save to PDF")
                
    time.sleep(10)
    newFile = r'C:/LinkedInData/Profiles/' + name + r'.pdf'
    print("Move file to new name: "+ newFile)
    move(r'C:/LinkedInData/Profiles/Profile.pdf', newFile )


# In[6]:


driver.quit()

