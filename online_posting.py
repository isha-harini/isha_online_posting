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

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

month_list = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

browser = webdriver.Chrome('/usr/local/bin/chromedriver')
wait = WebDriverWait(browser, 60)

######### TO BE EDITED BY USER ################

eb_login = 'isha.harini.umich@gmail.com'
eb_password = 'Silver123'

################## FLAGS ######################
DEBUG = 1 # 1 - Enable DEBUG; 0 - Disable DEBUG
GSHEET = 0 # 1 - Enable input read from Google Sheet; 0 - Disable input read from Google Sheet

################# EVENTBRITE ###########################

#testing here so that we can exit before all the fancy input stuff!
browser.get('https://www.eventbrite.com/create')



#login and password

curpath =  "//*[@id='signin-email']"
ele = wait.until(EC.presence_of_element_located((By.XPATH, curpath)))
ele.send_keys(eb_login)

curpath =  "//*[@id='root']/div/div[2]/div/div/div/div[1]/div/main/div/div/div/form/div[2]/button"
ele = wait.until(EC.presence_of_element_located((By.XPATH, curpath)))
ele.click()

curpath =  "//*[@id='password']"
ele = wait.until(EC.presence_of_element_located((By.XPATH, curpath)))
ele.send_keys(eb_password)

curpath = "//*[@id='root']/div/div[2]/div/div/div/div[1]/div/main/div/div/div/div[2]/form/div[3]/button" 
ele = wait.until(EC.presence_of_element_located((By.XPATH, curpath)))
ele.click()

##org name
#path = "//*[@id='event_details_organizer']/div[2]/div[1]/span/a[2]"
#ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
#ele.click()
#path = "//*[@id='id_group-organizer-organizers-1-organization_name']"
#ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
#ele.send_keys('Isha Foundation')

#assert 'NBA' in browser.page_source
#action = action_chains.ActionChains(browser)
#
## open up the developer console, mine on MAC, yours may be diff key combo
#action.send_keys(keys.Keys.COMMAND+keys.Keys.ALT+'i')
#action.perform()
#time.sleep(3)
## this below ENTER is to rid of the above "i"
#action.send_keys(keys.Keys.ENTER)
## inject the JavaScript...
#action.send_keys("document.querySelectorAll('label.boxed')[1].click()"+keys.Keys.ENTER)
#action.perform()

#exit()

#Event details - defaults for testing
event_id = '1'
event_name = 'TODO'
event_venue = 'TODO'
event_date = 'Sept 23'
event_stime = '5:00PM'
event_etime = '6:00PM'
event_addr = 'Isha Yoga Center'
event_city = 'Ann Arbor'
event_zip = '48105'
event_year = 2018
event_desc = 'Whatever you can do or cannot do, learn how to be'
poster_path = '/Users/harini/Documents/GitHub/isha_online_posting/posters/ishakriya.jpg'
org_desc_file = open('event_desc/isha_general.txt', 'r')
org_desc = ''
if org_desc_file.mode == 'r':
	org_desc = org_desc_file.read()
else:
	print('Something went wrong')
	exit()

#Event details - get it from user
if DEBUG == 0 and GSHEET == 0:
	#event type
	event_id = raw_input("Enter Event ID (1: Isha Kriya; 2: Yoga for Beginners; 3: Yoga for Success): ") 

	if(not int(event_id) or int(event_id) > 3):
		print bcolors.FAIL + "Invalid EventID. Exiting" + bcolors.ENDC
		exit()
	else:
		print bcolors.OKBLUE + "Please enter the following details for your event" + bcolors.ENDC

	#other event details
	event_date = raw_input("Enter when the event will happen(e.g. Sept 23): ")
	event_stime = raw_input("Enter event start time (e.g. 5:00PM): ")
	event_etime = raw_input("Enter event end time (e.g. 5:00PM): ")
	event_venue = raw_input("Enter event venue name: ")
	event_addr = raw_input("Enter event address: ")
	event_city = raw_input("Enter Event City. (e.g. Ann Arbor): ")
	event_zip = raw_input("Enter Event Zip code (e.g. 48105): ")
	
	#ask for verification	
	is_correct = raw_input("Take a moment to verify.. Are all entered details correct(yes/no)? ")
	if(not is_correct.lower().startswith('y')):
		print bcolors.FAIL + "Exiting the program. Restart the program and enter details again" + bcolors.ENDC
		exit()

	#assign poster/description file paths based on event ID
	if(int(event_id) == 1):
		#Isha Kriya
		event_name = 'Meditation for Beginners'
		desc_file = open("event_desc/isha_kriya.txt", "r")
		poster_path = '/Users/harini/Documents/GitHub/isha_online_posting/posters/ishakriya.jpg'
	elif(int(event_id) == 2):
		#Yoga for Beginners
		event_name = 'Yoga for Beginners'
		desc_file = open("event_desc/yoga_for_beginners.txt", "r")
		poster_path = '/Users/harini/Documents/GitHub/isha_online_posting/posters/yfb.jpg'
	elif(int(event_id) == 3):
		#Yoga for Success
		event_name = 'Yoga for Success'
		desc_file = open("event_desc/yoga_for_success.txt", "r")
		poster_path = '/Users/harini/Documents/GitHub/isha_online_posting/posters/yfs.jpg'

	if desc_file.mode == 'r':
		event_desc = desc_file.read()
	else:
		print('Something went wrong')
		exit()

#TODO: GSheet integration


#actual event

path = "//*[@id='id_group-details-name']"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.send_keys(event_name)

#location

#enter address click
path = "//*[@id='create_location_content']/div/div/ul/li[3]/a"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.click()
ele.click()

#venue name
path = "//*[@id='location_edit_form']/div[1]/input[1]"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.send_keys(event_venue)

#address line 1
path = "//*[@id='location_edit_form']/div[1]/input[2]"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.send_keys(event_addr)

#skipping line 2 of the address for now...
##address line 2
#path = "//*[@id='location_edit_form']/div[1]/input[3]"
#ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
#ele.send_keys('Address Line 2')

#city
path = "//*[@id='location_edit_form']/div[1]/input[4]"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.send_keys(event_city)

#state -- hardcoding for now ..
path = "//*[@id='location_edit_form']/div[2]/div[1]/input"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.send_keys('Michigan')

#zip
path = "//*[@id='location_edit_form']/div[2]/div[2]/input"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.send_keys(event_zip)

#country -- hardcoding for now ..
path = "//*[@id='location_edit_form']/div[2]/div[3]/div/select"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
for option in ele.find_elements_by_tag_name('option'):
	if option.text == 'United States':
			option.click()
			break


#start date -- clear and type in the date
event_date = ''.join(event_date.split()) #remove all whitespace characters
split_date = re.split('(\d+)', event_date)
event_month = split_date[0].lower()
event_date = split_date[1]

path = "//*[contains(concat( ' ', @class, ' ' ), concat( ' ', 'hasDatepicker', ' ' ))]" 
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele = browser.find_elements_by_xpath(path)
ele[0].click()
ele[0].clear()
mon_idx = 0
for mon in month_list:
	mon_idx = mon_idx + 1
	if mon in event_month:
		break
in_date = str(mon_idx) + '/' + str(event_date) + '/' + str(event_year)
ele[0].send_keys(in_date)

#end date
ele[1].click()
ele[1].clear()
ele[1].send_keys(in_date)

#Fix the start time
event_stime = ''.join(event_stime.split()) #remove all whitespace characters
event_stime = event_stime.lower()
event_stime = event_stime.replace('.', '') #remove dot from a.m, p.m.
split_stime = ''
event_am_pm = ''
if "am" in event_stime:
	event_am_pm = "am"
	split_stime = re.split("[:a]", event_stime)
elif "pm" in event_stime:
	event_am_pm = "pm"
	split_stime = re.split("[:p]", event_stime)
else:
	print bcolors.FAIL + "Event start time does not have AM or PM. Exiting" + bcolors.ENDC
	exit()
new_stime = split_stime[0] + ':' + split_stime[1] + event_am_pm

#start time --clear and type in the time
path = "//*[@id='event_details_date']/div/div[1]/div[1]/div[1]/div/div[2]/input"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.clear()
ele.send_keys(new_stime)

#Fix the end time
event_etime = ''.join(event_etime.split()) #remove all whitespace characters
event_etime = event_etime.lower()
event_etime = event_etime.replace('.', '') #remove dot from a.m, p.m.
split_etime = ''
event_am_pm = ''
if "am" in event_stime:
	event_am_pm = "am"
	split_etime = re.split("[:a]", event_etime)
elif "pm" in event_stime:
	event_am_pm = "pm"
	split_etime = re.split("[:p]", event_etime)
else:
	print bcolors.FAIL + "Event end time does not have AM or PM. Exiting" + bcolors.ENDC
	exit()
new_etime = split_etime[0] + ':' + split_etime[1] + event_am_pm

#end time
path = "//*[@id='event_details_date']/div/div[1]/div[1]/div[2]/div/div[2]/input"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.clear()
ele.send_keys(new_etime)
time.sleep(2)

for i in range(1, 6):
	actions = ActionChains(browser)
	actions.send_keys(Keys.TAB)
	actions.perform()
	time.sleep(1)

actions.send_keys(Keys.TAB)
actions.perform()
time.sleep(1)
actions = ActionChains(browser)
actions.send_keys(event_desc)
actions.perform()
time.sleep(3)

#event image
path = "//*[@id='uploader-file-input-id']"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.send_keys(poster_path)
text = 'DONE'
ele = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, text)))
ele.click()
time.sleep(6)


path = "//*[@id='id_group-organizer-organizer']"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
for option in ele.find_elements_by_tag_name('option'):
	if 'Isha Foundation' in option.text:
			option.click()
			break

time.sleep(3)

#event type
path = "//*[@id='id_group-privacy_and_promotion-event_format']"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
for option in ele.find_elements_by_tag_name('option'):
	if 'Class' in option.text:
			option.click()
			break

#event topic
path = "//*[@id='id_group-privacy_and_promotion-event_category']"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
for option in ele.find_elements_by_tag_name('option'):
	if 'Health' in option.text:
			option.click()
			break

#ticketing
path = "//*[@id='create-ticket-free-button']"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.click()

time.sleep(3)

path = "//*[@id='id_group-tickets-0-ticket_type']"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.send_keys('RSVP')

path = "//*[@id='id_group-tickets-0-quantity_total']"
ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
ele.send_keys('100')

exit()

################################################################### JUNK .. ###############################
###################################################################



if bgg_password == 'xxxx':
	print bcolors.FAIL + 'Please enter your login/password info for Big Green Gym in the script and retry' + bcolors.ENDC
	exit()

event_id = raw_input("Enter Event ID (1: Isha Kriya; 2: Yoga for Beginners; 3: Yoga for Success): ") 

if(not int(event_id) or int(event_id) > 3):
	print bcolors.FAIL + "Invalid EventID. Exiting" + bcolors.ENDC
	exit()
else:
	print bcolors.OKBLUE + "Please enter the following details for your event" + bcolors.ENDC


#Input event details
event_date = raw_input("Enter when the event will happen(e.g. Sept 23): ")
event_stime = raw_input("Enter event start time (e.g. 5:00PM): ")
event_etime = raw_input("Enter event end time (e.g. 5:00PM): ")
event_addr = raw_input("Enter event address: ")
event_area = raw_input("Enter Event City. (e.g. Ann Arbor): ")
#poster_path = raw_input("Enter complete path of the poster on your computer: ")

is_correct = raw_input("Take a moment to verify.. Are all entered details correct(yes/no)? ")

if(not is_correct.lower().startswith('y')):
	print bcolors.FAIL + "Exiting the program. Restart the program and enter details again" + bcolors.ENDC
	exit()

event_name = ''
desc_file = ''

if(int(event_id) == 1):
	#Isha Kriya
	event_name = 'Meditation for Beginners'
	desc_file = open("event_desc/isha_kriya.txt", "r")
	poster_path = open("/Users/harini/Documents/GitHub/isha_online_posting/posters/isha_kriya.jpg")
elif(int(event_id) == 2):
	#Yoga for Beginners
	event_name = 'Yoga for Beginners'
	desc_file = open("event_desc/yoga_for_beginners.txt", "r")
elif(int(event_id) == 3):
	#Yoga for Success
	event_name = 'Yoga for Success'
	desc_file = open("event_desc/yoga_for_success.txt", "r")
	


#Generate Event title

event_name = event_name + '-' + event_area + '-' + event_date + ' ' + event_stime

print bcolors.OKGREEN + "Posting " + event_name + bcolors.ENDC

#Read event description

event_description = ''

if desc_file.mode == 'r':
	event_description = desc_file.read()
else:
	print('Something went wrong')
	exit()

#Fix the start time
event_stime = ''.join(event_stime.split()) #remove all whitespace characters
event_stime = event_stime.lower()
event_stime = event_stime.replace('.', '') #remove dot from a.m, p.m.
split_stime = ''

event_am_pm = ''
if "am" in event_stime:
	event_am_pm = "am"
	split_stime = re.split("[:a]", event_stime)
elif "pm" in event_stime:
	event_am_pm = "pm"
	split_stime = re.split("[:p]", event_stime)
else:
	print bcolors.FAIL + "Event start time does not have AM or PM. Exiting" + bcolors.ENDC
	exit()

if(not (int(split_stime[1]) == 0 or int(split_stime[1]) == 30)):
	if(int(split_stime[1]) < 30):
		split_stime[1] = "0"
	else:
		split_stime[1] = "30"

new_stime = split_stime[0] + ':' + split_stime[1]

#fix event date
event_date = ''.join(event_date.split()) #remove all whitespace characters
split_date = re.split('(\d+)', event_date)
event_month = split_date[0].lower()
event_date = split_date[1]


print bcolors.HEADER + "All set. Starting to post" + bcolors.ENDC

############################################## EVENTBRITE ######################################################






############################################## BIG GREEN GYM ######################################################

browser.get('https://www.thebiggreengym.com/en/listings/new')

loginbox = browser.find_element_by_id('main_person_login')
loginbox.send_keys(bgg_login)

passbox = browser.find_element_by_id('main_person_password')
passbox.send_keys(bgg_password)
passbox.submit()

if(int(event_id) == 1):
	session_type = browser.find_element_by_partial_link_text('Meditation')
else:
	session_type = browser.find_element_by_partial_link_text('Yoga Basics')
session_type.click()

listing_type = browser.find_element_by_partial_link_text('Free session')
listing_type.click()

#start filling in the details ...

try:
	curpath =  "//*[(@id = 'listing_title')]"
	element = wait.until(EC.presence_of_element_located((By.XPATH, curpath)))
finally:
	try:
		list_title = browser.find_element_by_xpath(curpath)
		list_title.send_keys(event_name)
	except:
		print('Title not found')
	
try:
	curpath = "//*[(@id = 'listing_description')]"
	wait = WebDriverWait(browser, 60)
	element = wait.until(EC.presence_of_element_located((By.XPATH, curpath)))
finally:
	try:
		list_title = browser.find_element_by_xpath(curpath)
		list_title.send_keys(event_description)
	except:
		print('Description not found')

try:
	curpath = "//*[contains(concat( ' ', @class, ' ' ), concat( ' ', 'required', ' ' ))]"
	wait = WebDriverWait(browser, 60)
	element = wait.until(EC.presence_of_element_located((By.XPATH, curpath)))
finally:
	try:
		start_time = browser.find_element_by_xpath(curpath)
		for option in start_time.find_elements_by_tag_name('option'):
			if option.text == new_stime:
				option.click()
				break
	except:
		print('Time not found')

try:
	fid = 'custom_fields_28618'
	wait = WebDriverWait(browser, 60)
	element = wait.until(EC.presence_of_element_located((By.ID, fid)))
finally:
	try:
		am_pm = browser.find_element_by_id(fid)
		for option in am_pm.find_elements_by_tag_name('option'):
			if option.text.lower() == event_am_pm:
				option.click()
				break
	except:
		print('AM/PM not found')

try:
	fid = 'custom_fields_28437__1i'
	wait = WebDriverWait(browser, 60)
	element = wait.until(EC.presence_of_element_located((By.ID, fid)))
finally:
	try:
		event_year = browser.find_element_by_id(fid)
		for option in event_year.find_elements_by_tag_name('option'):
			if option.text == '2018':
				option.click()
				break
	except:
		print('Event year not found')

try:
	fid = 'custom_fields_28437__2i'
	wait = WebDriverWait(browser, 60)
	element = wait.until(EC.presence_of_element_located((By.ID, fid)))
finally:
	try:
		web_event_month = browser.find_element_by_id(fid)
		for option in web_event_month.find_elements_by_tag_name('option'):
			if (event_month in option.text.lower()) or (option.text.lower() in event_month):
				option.click()
				break
	except:
		print 'Event month' + event_month +  'not found'

try:
	fid = 'custom_fields_28437__3i'
	wait = WebDriverWait(browser, 60)
	element = wait.until(EC.presence_of_element_located((By.ID, fid)))
finally:
	try:
		web_event_date = browser.find_element_by_id(fid)
		for option in web_event_date.find_elements_by_tag_name('option'):
			if option.text == event_date:
				option.click()
				break
	except:
		print('Event date not found')

try:
	fid = 'custom_fields_28441'
	wait = WebDriverWait(browser, 60)
	element = wait.until(EC.presence_of_element_located((By.ID, fid)))
finally:
	try:
		instructor = browser.find_element_by_id(fid)
		instructor.send_keys('Isha Foundation')
	except:
		print('Time not found')

try:
	fid = 'listing_valid_until_1i'
	wait = WebDriverWait(browser, 60)
	element = wait.until(EC.presence_of_element_located((By.ID, fid)))
finally:
	try:
		event_year = browser.find_element_by_id(fid)
		for option in event_year.find_elements_by_tag_name('option'):
			if option.text == '2018':
				option.click()
				break
	except:
		print('Event year not found')

try:
	fid = 'listing_valid_until_2i'
	wait = WebDriverWait(browser, 60)
	element = wait.until(EC.presence_of_element_located((By.ID, fid)))
finally:
	try:
		web_event_month = browser.find_element_by_id(fid)
		for option in web_event_month.find_elements_by_tag_name('option'):
			if event_month in option.text.lower() or option.text.lower() in event_month:
				option.click()
				break
	except:
		print 'Event month' + event_month +  'not found'

try:
	fid = 'listing_valid_until_3i'
	wait = WebDriverWait(browser, 60)
	element = wait.until(EC.presence_of_element_located((By.ID, fid)))
finally:
	try:
		web_event_date = browser.find_element_by_id(fid)
		for option in web_event_date.find_elements_by_tag_name('option'):
			if option.text == event_date:
				option.click()
				break
	except:
		print('Event date not found')

try:
	fid = 'listing_origin'
	wait = WebDriverWait(browser, 60)
	element = wait.until(EC.presence_of_element_located((By.ID, fid)))
finally:
	try:
		place = browser.find_element_by_id(fid)
		place.send_keys(event_addr)
	except:
		print('Time not found')

#fileupload
try:
	curpath = "//*[contains(concat( ' ', @class, ' ' ), concat( ' ', 'fileupload', ' ' ))]"
	wait = WebDriverWait(browser, 60)
	element = wait.until(EC.presence_of_element_located((By.XPATH, curpath)))
finally:
	try:
		upload = browser.find_element_by_xpath(curpath)
		#upload.send_keys('/Users/harini/Documents/OneDrive - umich.edu/ISHA/PROMO/scripting/Isha Kriya Canton May 21 2018-1.jpg')
		upload.send_keys(poster_path)

	except:
		print('Upload not found')


print bcolors.HEADER + 'Completed posting to Big Green Gym' + bcolors.ENDC

