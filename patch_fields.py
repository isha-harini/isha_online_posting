#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains, keys
from selenium.webdriver.common.action_chains import ActionChains

import re
import time
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from datetime import datetime

month_list_patch = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
event_url_ishakriya = 'http://www.ishafoundation.org/Ishakriya'
event_url_upayoga = 'http://isha.sadhguru.org/yoga/yoga-programs/upa-yoga/'

#Event details - defaults for testing
event_id = '1'
event_name = 'Meditation for Beginners'
event_venue = 'Ann Arbor Library'
event_date = '09/23/2018'
event_stime = '5:00PM'
event_etime = '6:00PM'
event_addr_l1 = '123 Ann Arbor'
event_addr_l2 = 'Room 23'
event_city = 'Ann Arbor'
event_state = 'Michigan'
event_zip = '48105'
event_year = 2018
event_desc = 'Whatever you can do or cannot do, learn how to be'
poster_path = '/Users/harini/Documents/GitHub/isha_online_posting/posters/ishakriya_full.jpg'
org_desc_file = open('event_desc/isha_general.txt', 'r')
org_desc = ''
if org_desc_file.mode == 'r':
	org_desc = org_desc_file.read()
else:
	print('Something went wrong')
	exit()

###
split_date = re.split("[\/]", event_date)
month = split_date[0]
date = split_date[1]
year = split_date[2]
#accessing fields in patch

##credentials
patch_login = 'isha.harini.umich@gmail.com'
patch_password = 'Dhyanalinga247'

browser = webdriver.Chrome('/usr/local/bin/chromedriver')
wait = WebDriverWait(browser, 60)

browser.get('https://my.patch.com/user-login')


path = "//*[(@id = 'edit-user-name')]"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.send_keys(patch_login)

path = "//*[(@id = 'edit-password')]"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.send_keys(patch_password)

path = "//*[(@id = 'edit-submit')]"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.click()

time.sleep(3)

path = "//*[@id='block-system-main']/div[3]/div[1]/a"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.click()

time.sleep(3)

#import pdb; pdb.set_trace()

#image upload
ele = wait.until(EC.presence_of_element_located((By.ID, 'edit-field-image-asset-und-0-upload')))
ele.send_keys(poster_path)

#patch sel
path = "//*[@id='select-patch']"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.clear()
ele.send_keys(event_zip)

path = "//*[@id='autocomplete-results']/div[1]"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.click()
ele.click()

time.sleep(3)

#share nearby
path = "//*[@id='edit-share-nearby']"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.click()

#event name
path = "//*[@id='edit-title']"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.send_keys(event_name)

#date
path = "//*[@id='edit-field-calendar-date-und-0-value-datepicker-popup-0']"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.clear()
patch_date = month_list_patch[int(month)-1] + ' ' + date + ' ' + year
ele.send_keys(patch_date)

#time
path = "//*[@id='edit-field-calendar-date-und-0-value-timepicker-popup-1']"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.clear()
ele.send_keys(event_stime)


#venue
path = "//*[@id='edit-field-calendar-address-und-0-name-line']"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.send_keys(event_venue)

#addr line 1
path = "//*[@id='edit-field-calendar-address-und-0-thoroughfare']"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.send_keys(event_addr_l1)

#addr line 2
path = "//*[@id='edit-field-calendar-address-und-0-premise']"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.send_keys(event_addr_l2)

#city
path = "//*[@id='edit-field-calendar-address-und-0-locality']"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.send_keys(event_city)

#state
path = "//*[@id='edit-field-calendar-address-und-0-administrative-area']"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
for option in ele.find_elements_by_tag_name('option'):
	if option.text == 'Michigan':
			option.click()
			break

#zip
path = "//*[@id='edit-field-calendar-address-und-0-postal-code']"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.send_keys(event_zip)


#event desc
path = "//*[(@id = 'redactor-uuid-0')]"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.send_keys(event_desc)

#event url
path = "//*[(@id = 'edit-field-calendar-link-und-0-url')]"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.send_keys(event_url_ishakriya)
