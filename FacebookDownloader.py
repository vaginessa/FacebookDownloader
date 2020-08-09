#Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

import getpass




#Parameters
facebookUsername = input("Username:")
facebookPassword = getpass.getpass("Password:")
facebookURLextension = input("URL extension:")

#Variables
fullFacebookURL = "https://www.facebook.com/" + facebookURLextension



#Set Browser options 
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})



#Instantiate Browser using options
browser = webdriver.Chrome(chrome_options=option)



#Go to Facebook and login.
browser.get("http://www.facebook.com")

username = browser.find_element_by_name("email")
username.send_keys(facebookUsername)

password = browser.find_element_by_name("pass")
password.send_keys(facebookPassword + Keys.RETURN)



#Go to your profile page, then photos page, then open the first photo.
browser.implicitly_wait(5)

profilePage = browser.find_element_by_xpath('//a[@href="'+fullFacebookURL+'"]')
profilePage.click()

photosPage = browser.find_element_by_xpath('//a[@href="'+fullFacebookURL+'/photos"]')
photosPage.click()

firstPhoto = browser.find_element_by_xpath('//a[contains(@href, "/photo.php?fbid")]')
firstPhoto.click()



#Open "Actions for this post" menu and click Download.
previousURL = browser.current_url

actionsMenu = browser.find_element_by_xpath("//div[@class='btwxx1t3 j83agx80 hybvsw6c ll8tlv6m']//div[@class='nqmvxvec j83agx80 jnigpg78 cxgpxx05 dflh9lhu sj5x9vvc scb9dxdr odw8uiq3']//div[@aria-label='Actions for this post']")
browser.execute_script("arguments[0].click()", actionsMenu)

download = browser.find_element_by_xpath('//a[contains(@href, "https://scontent-lht6-1.xx.fbcdn.net")]')
download.click()
