#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import re
import time
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from datetime import datetime

browser = webdriver.Chrome('/usr/local/bin/chromedriver')
wait = WebDriverWait(browser, 60)

######### TO BE EDITED BY USER ################

bgg_login = 'isha.harini.umich@gmail.com'
bgg_password = 'Silver123'

tp_login = 'isha.harini.umich@gmail.com'
tp_password = 'Silver123'

tp_login = 'isha.harini.umich@gmail.com'
tp_password = 'Silver123'

###############################################

#browser.get('https://www.eventbrite.com/create')
#
#curpath =  "//*[@id='signin-email']"
#ele = wait.until(EC.presence_of_element_located((By.XPATH, curpath)))
#ele.send_keys(bgg_login)
#
#curpath =  "//*[@id='root']/div/div[2]/div/div/div/div[1]/div/main/div/div/div/form/div[2]/button"
#ele = wait.until(EC.presence_of_element_located((By.XPATH, curpath)))
#ele.click()
#
#curpath =  "//*[@id='password']"
#ele = wait.until(EC.presence_of_element_located((By.XPATH, curpath)))
#ele.send_keys(bgg_password)
#
#curpath = "//*[@id='root']/div/div[2]/div/div/div/div[1]/div/main/div/div/div/div[2]/form/div[3]/button" 
#ele = wait.until(EC.presence_of_element_located((By.XPATH, curpath)))
#ele.click()
#
#exit()

browser.get('http://myaccount.sulekha.com/signin?nexturl=http://myaccount.sulekha.com/post-an-event')

dummy = raw_input("Enter your credentials and press enter")

#curpath =  "//*[@id='txt_event_title']"
#ele = wait.until(EC.presence_of_element_located((By.XPATH, curpath)))
#ele.send_keys('Meditation for Beginners')
#
#curpath =  "//*[@id='alk_venue_autocomplete']"
#ele = wait.until(EC.presence_of_element_located((By.XPATH, curpath)))
#ele.click()
#
#curpath =  "//*[@id='txt_venue_name']"
#ele = wait.until(EC.presence_of_element_located((By.XPATH, curpath)))
#ele.send_keys('My home')
#
#curpath =  "//*[@id='txt_venue_address']"
#ele = wait.until(EC.presence_of_element_located((By.XPATH, curpath)))
#ele.send_keys('1929 Plymouth Road')
#
#curpath =  "//*[@id='txt_venue_city']"
#ele = wait.until(EC.presence_of_element_located((By.XPATH, curpath)))
#ele.send_keys('Ann Arbor')
#
#curpath =  "//*[@id='txt_venue_state']"
#ele = wait.until(EC.presence_of_element_located((By.XPATH, curpath)))
#ele.send_keys('Michigan')
#
#curpath =  "//*[@id='txt_venue_zip']"
#ele = wait.until(EC.presence_of_element_located((By.XPATH, curpath)))
#ele.send_keys('48105')
#
#curpath =  "//*[@id='lilanguage']/span[7]"
#ele = wait.until(EC.presence_of_element_located((By.XPATH, curpath)))
#ele.click()
#
#curpath =  "//*[(@id = 'iTinyEditorArea_ifr')]"
#ele = wait.until(EC.presence_of_element_located((By.XPATH, curpath)))
#ele.send_keys('Description goes here...')
#
##curpath =  "//*[@id='sel_org_list']"
##ele = wait.until(EC.presence_of_element_located((By.XPATH, curpath)))
##ele.send_keys('Description goes here')
#
##curpath =  "//*[@id='txt_org_description']"
##ele = wait.until(EC.presence_of_element_located((By.XPATH, curpath)))
##ele.send_keys('Description goes here')
#
#curpath =  "//*[@id='txt_hosted_by']"
#ele = wait.until(EC.presence_of_element_located((By.XPATH, curpath)))
#ele.send_keys('Description goes here')
#
#curpath =  "//*[@id='txt_org_contact']"
#ele = wait.until(EC.presence_of_element_located((By.XPATH, curpath)))
#ele.send_keys('Description goes here')

##event start date
#curpath =  "//*[@id='txt_event_startdate']"
#ele = wait.until(EC.presence_of_element_located((By.XPATH, curpath)))
#ele.clear()
#ele.send_keys('05/23/2018')

##event start time
##start hour
#starthourpath = "//*[@id='sel_event_starthour']"
#starthour = wait.until(EC.presence_of_element_located((By.XPATH, starthourpath)))
#start_time = '10'
#
#for option in starthour.find_elements_by_tag_name('option'):
#	if option.text == start_time:
#		option.click()
#		break
#
##startmin
#startminpath = "//*[@id='sel_event_startmin']"
#startmin = wait.until(EC.presence_of_element_located((By.XPATH, startminpath)))
#event_smin = '45'
#
#for option in startmin.find_elements_by_tag_name('option'):
#	if option.text == event_smin:
#		option.click()
#		break
#
#curpath = "//*[@id='sel_event_startmeridiem']"
#ele = wait.until(EC.presence_of_element_located((By.XPATH, curpath)))
#
#for option in ele.find_elements_by_tag_name('option'):
#	if option.text.lower() == 'am':
#		option.click()
#		break
#
##event end date
#curpath =  "//*[@id='txt_event_enddate']"
#ele = wait.until(EC.presence_of_element_located((By.XPATH, curpath)))
#ele.clear()
#ele.send_keys('05/23/2018')
#
##event end time
##end hour
#endhourpath = "//*[@id='sel_event_endhour']"
#endhour = wait.until(EC.presence_of_element_located((By.XPATH, endhourpath)))
#end_time = '11'
#
#for option in endhour.find_elements_by_tag_name('option'):
#	if option.text == end_time:
#		option.click()
#		break
#
##endmin
#endminpath = "//*[@id='sel_event_endmin']"
#endmin = wait.until(EC.presence_of_element_located((By.XPATH, endminpath)))
#event_emin = '45'
#
#for option in endmin.find_elements_by_tag_name('option'):
#	if option.text == event_emin:
#		option.click()
#		break
#
#curpath = "//*[@id='sel_event_endmeridiem']"
#ele = wait.until(EC.presence_of_element_located((By.XPATH, curpath)))
#
#for option in ele.find_elements_by_tag_name('option'):
#	if option.text.lower() == 'am':
#		option.click()
#		break
#

curpath = "//*[@id='div_imgcont_thumbnail']/label/span"
ele = wait.until(EC.presence_of_element_located((By.XPATH, curpath)))
ele.click()
curpath = "//*[@id='frm_event_post']/main/div[1]/div[2]/section/div[1]/div/div[1]/div/div[3]/label"
ele = wait.until(EC.presence_of_element_located((By.XPATH, curpath)))
ele.click()
#ele.send_keys('/Users/harini/Documents/GitHub/isha_online_posting/homepage-sliders-IshaFoundation.jpg')

exit()

#Keep clicking on Next till you reach the correct Month
locpath = "//*[@id='ui-datepicker-div']/div/div/span[1]"
idx = 0;
event_month = 'apr'
event_date = '23'
while idx < 12:
	idx = idx + 1
	month = wait.until(EC.presence_of_element_located((By.XPATH, locpath)))
	if event_month in month.text.lower():
		break;
	else:
		next_ = browser.find_element_by_xpath(curpath)
		next_.click()
if idx > 11:
	print 'Something went wrong'
	exit()



exit()

browser.get('https://www.townplanner.com/admin/events-ticket.php')

fid = 'login_email'
loginbox = wait.until(EC.presence_of_element_located((By.ID, fid)))
loginbox.send_keys(tp_login)

fid = 'login_password'
passbox = wait.until(EC.presence_of_element_located((By.ID, fid)))
passbox.send_keys(tp_password)
passbox.submit()

curpath =  "//*[contains(concat( ' ', @class, ' ' ), concat( ' ', 'icon-event', ' ' ))]"
events = wait.until(EC.presence_of_element_located((By.XPATH, curpath)))
events.click()

curpath =  "//*[contains(concat( ' ', @class, ' ' ), concat( ' ', 'btnNew', ' ' ))]"
all_new = wait.until(EC.presence_of_element_located((By.XPATH, curpath)))
all_new.click()

fid = 'singleDay'
box = wait.until(EC.presence_of_element_located((By.ID, fid)))
box.click()

fid = 'eventDate'
box = wait.until(EC.presence_of_element_located((By.ID, fid)))
box.click()


#Keep clicking on Next till you reach the correct Month
locpath = "//*[@id='ui-datepicker-div']/div/div/span[1]"
idx = 0;
event_month = 'apr'
event_date = '23'
while idx < 12:
	idx = idx + 1
	month = wait.until(EC.presence_of_element_located((By.XPATH, locpath)))
	if event_month in month.text.lower():
		break;
	else:
		next_ = browser.find_element_by_xpath(curpath)
		next_.click()
if idx > 11:
	print 'Something went wrong'
	exit()

#Now select the date
datepath = "//*[@id='ui-datepicker-div']/table/tbody/tr[1]/td[7]/a"
date = wait.until(EC.presence_of_element_located((By.XPATH, datepath)))
start_offset = 7 - int(date.text)
event_date = int(event_date) + start_offset
tr_id = event_date/7 + 1
td_id = event_date - int(event_date/7)*7
datepath = "//*[@id='ui-datepicker-div']/table/tbody/tr[" + str(tr_id) + "]/td[" + str(td_id) + "]/a"
date = wait.until(EC.presence_of_element_located((By.XPATH, datepath)))
date.click()

event_stime = '10'
event_etime = '11'
event_s_am_pm = 'am'
event_smin = '45'
event_emin = '45'
event_e_am_pm = 'am'
#start hour
starthourpath = "//*[@id='startTime']/select[1]"
starthour = wait.until(EC.presence_of_element_located((By.XPATH, starthourpath)))
start_time = str(event_stime) + event_s_am_pm

for option in starthour.find_elements_by_tag_name('option'):
	if option.text == start_time:
		option.click()
		break

#startmin
startminpath = "//*[@id='startTime']/select[2]"
startmin = wait.until(EC.presence_of_element_located((By.XPATH, startminpath)))

for option in startmin.find_elements_by_tag_name('option'):
	if option.text == event_smin:
		option.click()
		break

#end hour
endhourpath = "//*[@id='endTime']/select[1]"
endhour = wait.until(EC.presence_of_element_located((By.XPATH, endhourpath)))
end_time = str(event_etime) + event_e_am_pm

for option in endhour.find_elements_by_tag_name('option'):
	if option.text == end_time:
		option.click()
		break
#endmin
endminpath = "//*[@id='endTime']/select[2]"
endmin = wait.until(EC.presence_of_element_located((By.XPATH, endminpath)))
for option in endmin.find_elements_by_tag_name('option'):
	if option.text == event_emin:
		option.click()
		break

event_name = 'Meditation for Beginners'
event_descr = 'Event decription goes here .. '

eventnamepath = "//*[@id='eventTitle']"
eventname = wait.until(EC.presence_of_element_located((By.XPATH, eventnamepath)))
eventname.send_keys(event_name)

eventdescpath = "//*[@id='eventDescription']"
eventdesc = wait.until(EC.presence_of_element_located((By.XPATH, eventdescpath)))
eventdesc.send_keys(event_descr)

event_zip = '48105'
eventzippath = "//*[@id='zipcodeChoice']"
eventzip = wait.until(EC.presence_of_element_located((By.XPATH, eventzippath)))
eventzip.send_keys(event_zip)

#TODO event community .. 

eventcatpath = "//*[@id='eventCategory']"
eventcat = wait.until(EC.presence_of_element_located((By.XPATH, eventcatpath)))
for option in eventcat.find_elements_by_tag_name('option'):
	if option.text == 'Local Events':
		option.click()
		break

eventkeypath = "//*[@id='eventKeywords']"
eventkey = wait.until(EC.presence_of_element_located((By.XPATH, eventkeypath)))
eventkey.send_keys('Yoga, meditation')

eventurlpath = "//*[@id='eventUrl']"
eventurl = wait.until(EC.presence_of_element_located((By.XPATH, eventurlpath)))
eventurl.send_keys('http://isha.sadhguru.org/yoga/yoga-programs/upa-yoga/')

event_place = 'My Home'
eventfacilitypath = "//*[@id='eventFacility']"
eventfac = wait.until(EC.presence_of_element_located((By.XPATH, eventfacilitypath)))
eventfac.send_keys(event_place)

event_addr = '1929 Plymouth Road'
eventaddrpath = "//*[@id='eventAddress']"
eventaddr = wait.until(EC.presence_of_element_located((By.XPATH, eventaddrpath)))
eventaddr.send_keys(event_addr)


event_city = 'Ann Arbor'
eventcitypath = "//*[@id='eventCity']"
eventcity = wait.until(EC.presence_of_element_located((By.XPATH, eventcitypath)))
eventcity.send_keys(event_city)

event_state = 'MI'
eventstatepath = "//*[@id='eventState']"
eventstate = wait.until(EC.presence_of_element_located((By.XPATH, eventstatepath)))
for option in eventstate.find_elements_by_tag_name('option'):
	if option.text == event_state:
		option.click()
		break

event_zip = '48105'
eventzippath = "//*[@id='eventZip']"
eventzip = wait.until(EC.presence_of_element_located((By.XPATH, eventzippath)))
eventzip.send_keys(event_zip)


elepath = "//*[@id='eventContact']"
ele = wait.until(EC.presence_of_element_located((By.XPATH, elepath)))
ele.send_keys('Isha Detroit')

elepath = "//*[@id='eventPhone']"
ele = wait.until(EC.presence_of_element_located((By.XPATH, elepath)))
ele.send_keys('3134514742')

elepath = "//*[@id='eventEmail']"
ele = wait.until(EC.presence_of_element_located((By.XPATH, elepath)))
ele.send_keys('detroit@ishausa.org')

elepath = "//*[@id='photo']"
ele = wait.until(EC.presence_of_element_located((By.XPATH, elepath)))
ele.send_keys('/Users/harini/Documents/GitHub/isha_online_posting/Isha Kriya Canton May 21 2018-1.jpg')

elepath = "//*[@id='eventPlacement']"
ele = wait.until(EC.presence_of_element_located((By.XPATH, elepath)))
ele.click()


exit()

#Original code

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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
event_area = raw_input("Enter Event Area. This will appear in the ad title. (e.g. Ann Arbor): ")
event_date = raw_input("Enter when the event will happen(e.g. Sept 23): ")
event_stime = raw_input("Enter event start time (e.g. 5:00PM): ")
event_etime = raw_input("Enter event end time (e.g. 5:00PM): ")
event_addr = raw_input("Enter event address: ")
poster_path = raw_input("Enter complete path of the poster on your computer: ")

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
	wait = WebDriverWait(browser, 60)
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

