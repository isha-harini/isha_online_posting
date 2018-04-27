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
ele.send_keys("/Users/harini/Documents/GitHub/isha_online_posting/posters/ishakriya.jpg")

#patch sel
path = "//*[@id='select-patch']"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.clear()
ele.send_keys('48105')

path = "//*[@id='autocomplete-results']/div[1]"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.click()
ele.click()


#share nearby
path = "//*[@id='edit-share-nearby']"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.click()

#event name
path = "//*[@id='edit-title']"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.send_keys(patch_login)

#date
path = "//*[@id='edit-field-calendar-date-und-0-value-datepicker-popup-0']"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.clear()

#time
path = "//*[@id='edit-field-calendar-date-und-0-value-timepicker-popup-1']"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.clear()


#venue
path = "//*[@id='edit-field-calendar-address-und-0-name-line']"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.send_keys('Hi there')

#addr line 1
path = "//*[@id='edit-field-calendar-address-und-0-thoroughfare']"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.send_keys('Hi there')

#addr line 2
path = "//*[@id='edit-field-calendar-address-und-0-premise']"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.send_keys('Hi there')

#city
path = "//*[@id='edit-field-calendar-address-und-0-locality']"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.send_keys('Hi there')

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
ele.send_keys('48105')


#event desc
path = "//*[(@id = 'redactor-uuid-0')]"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.send_keys('Hi there')
