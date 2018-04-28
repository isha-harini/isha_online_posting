#NOTE: share the google sheet with harini@ishaonlineposting.iam.gserviceaccount.com
#To read from a cell: testsheet.acell(CELL).value; to write: esheet.update_acell(C_EVENT_TYPE + str(ev_idx), new_name)

############################# SETTINGS ################################

#FLAGS
DEBUG = 0 #Debug event posting by turning off GSHEET reading

#Copy and paste the workbook URL here:
WORKBOOKURL = 'https://docs.google.com/spreadsheets/d/1X7WS6spYZfV2o40Hy2e_D9jZcOD3mlQ6yjcN3UZykDQ/edit?ts=5ae13571#gid=0'

#Column names of different event details
C_EVENT_TYPE = 'A'
C_POSTING_STATUS = 'B'
C_DATE = 'F'
C_START_TIME = 'G'
C_END_TIME = 'H'
C_VENUE = 'I'
C_ADDR_LINE1 = 'J'
C_ADDR_LINE2 = 'K'
C_CITY = 'L'
C_STATE = 'M'
C_ZIP = 'N'
START_ROW = 2

#login details
#Eventbrite
eb_login = 'detroit@ishausa.org'
eb_password = 'j0y247LetUsMakeitHappen!'

#Patch
patch_login = 'isha.harini.umich@gmail.com'
patch_password = 'Dhyanalinga247'

#State name - code dictionary
state_name = {
	'MI' : 'Michigan'

	}

#################################################################################
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

#prettifies the cmd line
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

browser_eb = []
browser_pat = []


#Eventbrite posting
def eventbrite(ev_name, ev_month, ev_date, ev_year, ev_shour, ev_smin, 
				ev_sampm, ev_ehour, ev_emin, ev_eampm, ev_venue, 
					ev_addr_l1, ev_addr_l2, ev_city, ev_state, ev_zip, ev_desc, ev_poster, ev_url): 

	browser_eb.append(webdriver.Chrome('/usr/local/bin/chromedriver'))
	browser = browser_eb[len(browser_eb)-1]
	wait = WebDriverWait(browser, 60)
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
	
	#actual event
	
	path = "//*[@id='id_group-details-name']"
	ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
	ele.send_keys(ev_name)
	
	#location
	
	#enter address click
	path = "//*[@id='create_location_content']/div/div/ul/li[3]/a"
	ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
	ele.click()
	ele.click()
	
	#venue name
	path = "//*[@id='location_edit_form']/div[1]/input[1]"
	ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
	ele.send_keys(ev_venue)
	
	#address line 1
	path = "//*[@id='location_edit_form']/div[1]/input[2]"
	ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
	ele.send_keys(ev_addr_l1)
	
	#address line 2
	path = "//*[@id='location_edit_form']/div[1]/input[3]"
	ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
	ele.send_keys(ev_addr_l2)
	
	#city
	path = "//*[@id='location_edit_form']/div[1]/input[4]"
	ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
	ele.send_keys(ev_city)
	
	#state -- hardcoding for now ..
	path = "//*[@id='location_edit_form']/div[2]/div[1]/input"
	ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
	ele.send_keys(ev_state)
	
	#zip
	path = "//*[@id='location_edit_form']/div[2]/div[2]/input"
	ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
	ele.send_keys(ev_zip)
	
	#country -- hardcoding for now ..
	path = "//*[@id='location_edit_form']/div[2]/div[3]/div/select"
	ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
	for option in ele.find_elements_by_tag_name('option'):
		if option.text == 'United States':
				option.click()
				break
	
	
	#start date -- clear and type in the date
	path = "//*[contains(concat( ' ', @class, ' ' ), concat( ' ', 'hasDatepicker', ' ' ))]" 
	ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
	ele = browser.find_elements_by_xpath(path)
	ele[0].click()
	ele[0].clear()
	in_date = str(ev_month) + '/' + str(ev_date) + '/' + str(ev_year)
	ele[0].send_keys(in_date)
	
	#end date
	ele[1].click()
	ele[1].clear()
	ele[1].send_keys(in_date)
	
	#Fix the start time
	new_stime = ev_shour + ':' + ev_smin + ev_sampm
	
	#start time --clear and type in the time
	path = "//*[@id='event_details_date']/div/div[1]/div[1]/div[1]/div/div[2]/input"
	ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
	ele.clear()
	ele.send_keys(new_stime)
	
	#Fix the end time
	new_etime = ev_ehour + ':' + ev_emin + ev_eampm
	
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
	actions.send_keys(ev_desc)
	actions.perform()
	time.sleep(3)
	
	#event image
	path = "//*[@id='uploader-file-input-id']"
	ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
	ele.send_keys(ev_poster)
	time.sleep(3)
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
	
	print bcolors.HEADER + 'Completed posting to Eventbrite' + bcolors.ENDC

#Patch posting
def patch(ev_name, ev_month, ev_date, ev_year, ev_shour, ev_smin, 
				ev_sampm, ev_ehour, ev_emin, ev_eampm, ev_venue, 
					ev_addr_l1, ev_addr_l2, ev_city, ev_state, ev_zip, ev_desc, ev_poster, ev_url): 

	browser_pat.append(webdriver.Chrome('/usr/local/bin/chromedriver'))
	browser = browser_pat[len(browser_pat)-1]
	month_list_patch = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

	wait = WebDriverWait(browser, 60)
	browser.get('https://my.patch.com/user-login')

	##credentials
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
	ele.send_keys(ev_poster)

	#patch sel
	path = "//*[@id='select-patch']"
	ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
	ele.clear()
	ele.send_keys(ev_zip)

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
	ele.send_keys(ev_name)
	
	#date
	path = "//*[@id='edit-field-calendar-date-und-0-value-datepicker-popup-0']"
	ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
	ele.clear()
	patch_date = month_list_patch[int(ev_month)-1] + ' ' + ev_date + ' ' + ev_year
	ele.send_keys(patch_date)
	
	#time
	path = "//*[@id='edit-field-calendar-date-und-0-value-timepicker-popup-1']"
	ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
	ele.clear()
	event_stime = ev_shour + ':' + ev_smin + ev_sampm
	ele.send_keys(event_stime)
	
	
	#venue
	path = "//*[@id='edit-field-calendar-address-und-0-name-line']"
	ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
	ele.send_keys(ev_venue)
	
	#addr line 1
	path = "//*[@id='edit-field-calendar-address-und-0-thoroughfare']"
	ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
	ele.send_keys(ev_addr_l1)
	
	#addr line 2
	path = "//*[@id='edit-field-calendar-address-und-0-premise']"
	ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
	ele.send_keys(ev_addr_l2)
	
	#city
	path = "//*[@id='edit-field-calendar-address-und-0-locality']"
	ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
	ele.send_keys(ev_city)
	
	#state
	path = "//*[@id='edit-field-calendar-address-und-0-administrative-area']"
	ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
	for option in ele.find_elements_by_tag_name('option'):
		if option.text.lower() == state_name[ev_state].lower():
				option.click()
				break
	
	#zip
	path = "//*[@id='edit-field-calendar-address-und-0-postal-code']"
	ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
	ele.send_keys(ev_zip)
	
	
	#event desc
	path = "//*[(@id = 'redactor-uuid-0')]"
	ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
	ele.send_keys(ev_desc)
	
	#event url
	path = "//*[(@id = 'edit-field-calendar-link-und-0-url')]"
	ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
	ele.send_keys(ev_url)

	print bcolors.HEADER + 'Completed posting to Patch' + bcolors.ENDC

if DEBUG == 1:
	ev_name = 'Meditation for Beginners'
	ev_month = '09'
	ev_date = '23'
	ev_year = '2018'
	ev_shour = '5'
	ev_smin = '45'
	ev_sampm = 'PM'
	ev_ehour = '6'
	ev_emin = '45'
	ev_eampm = 'PM'
	ev_venue = 'Ann Arbor District Library'
	ev_addr_l1 = '123 Ann Arbor Road'
	ev_addr_l2 = 'Room 3003'
	ev_city = 'Ann Arbor'
	ev_state = 'MI'
	ev_zip = '48105'
	ev_desc = 'You may either Hide or you may Seek; The domain of the Divine is open to all who Seek'
	ev_poster = '/Users/harini/Documents/GitHub/isha_online_posting/posters/ishakriya.jpg'
	ev_url = 'http://www.ishafoundation.org/Ishakriya'

	eventbrite(ev_name, ev_month, ev_date, ev_year, ev_shour, ev_smin, 
				ev_sampm, ev_ehour, ev_emin, ev_eampm, ev_venue, 
					ev_addr_l1, ev_addr_l2, ev_city, ev_state, ev_zip, ev_desc, ev_poster, ev_url)

	patch(ev_name, ev_month, ev_date, ev_year, ev_shour, ev_smin, 
				ev_sampm, ev_ehour, ev_emin, ev_eampm, ev_venue, 
					ev_addr_l1, ev_addr_l2, ev_city, ev_state, ev_zip, ev_desc, ev_poster, ev_url)

elif DEBUG == 0:
	import gspread
	from oauth2client.service_account import ServiceAccountCredentials

	scope = ['https://spreadsheets.google.com/feeds',
         	'https://www.googleapis.com/auth/drive']

	credentials = ServiceAccountCredentials.from_json_keyfile_name('gsheet/IshaOnlinePosting-f601765b7565.json', scope)

	gc = gspread.authorize(credentials)

	#NOTE: operating on the first worksheet in a workbook. Fix here if otherwise..
	esheet = gc.open_by_url(WORKBOOKURL).get_worksheet(0)

	ev_idx = START_ROW
	ev_desc = ''
	ev_poster = ''
	desc_file = ''
	ev_url = ''

	while 1:
		if esheet.acell(C_EVENT_TYPE + str(ev_idx)).value: #there is an event in this row
			if not esheet.acell(C_POSTING_STATUS + str(ev_idx)).value: #not yet posted
				#EVENT TYPE
				ev_type = esheet.acell(C_EVENT_TYPE + str(ev_idx)).value
				ev_name = ''
				if 'meditation for beginners' in ev_type.lower():
					print bcolors.HEADER + 'Meditation for Beginners identified' + bcolors.ENDC
					ev_name = 'Meditation for Beginners'
					desc_file = open("event_desc/isha_kriya.txt", "r")
					ev_poster = '/Users/harini/Documents/GitHub/isha_online_posting/posters/ishakriya.jpg'
					ev_url = 'http://www.ishafoundation.org/Ishakriya'

				elif 'yoga for beginners' in ev_type.lower():
					print bcolors.HEADER + 'Yoga for Beginners identified' + bcolors.ENDC
					ev_name = 'Yoga for Beginners'
					desc_file = open("event_desc/yoga_for_beginners.txt", "r")
					ev_poster = '/Users/harini/Documents/GitHub/isha_online_posting/posters/yfb.jpg'
					ev_url = 'http://isha.sadhguru.org/yoga/yoga-programs/upa-yoga/'

				elif 'yoga for success' in ev_type.lower():
					print bcolors.HEADER + 'Yoga for Success identified' + bcolors.ENDC
					ev_name = 'Yoga for Success'
					desc_file = open("event_desc/yoga_for_success.txt", "r")
					ev_poster = '/Users/harini/Documents/GitHub/isha_online_posting/posters/yfs.jpg'
					ev_url = 'http://isha.sadhguru.org/yoga/yoga-programs/upa-yoga/'

				else:
					print bcolors.FAIL + 'Unsupported event name found in row ' + str(ev_idx) + bcolors.ENDC
					ans = raw_input('What do you want to do? Answer with: \'rename\' to give a new name to the event; \'ignore\' to ignore this event and continue with the next; \'exit\' to end the script. (r/i/e): ')
	
					if ans.lower().startswith('r'):
						new_name = raw_input('Input new name for event in row ' + str(ev_idx) + ': ')
						esheet.update_acell(C_EVENT_TYPE + str(ev_idx), new_name)
						continue
					elif ans.lower().startswith('i'):
						print bcolors.HEADER + 'Okay. Proceeding to the next event' + bcolors.ENDC
						ev_idx = ev_idx + 1
						continue
					elif ans.lower().startswith('e'):
						print bcolors.HEADER + 'Okay. Exiting the script. Pranams' + bcolors.ENDC
				 		exit()
					else:
						print bcolors.FAIL + 'Sorry. Unrecognized answer. Exiting the script' + bcolors.ENDC
						exit()
		
				#Event description
				if desc_file.mode == 'r':
					ev_desc = desc_file.read()
				else:
					print('Something went wrong')
					exit()

				#DATE
				ev_date = esheet.acell(C_DATE + str(ev_idx)).value	
				date_split = re.split(r"[\/]", ev_date)
				ev_month = date_split[0]
				ev_date = date_split[1]
				ev_year = date_split[2]
				if(len(date_split[2]) == 2):
					ev_year = '20' + date_split[2]
	
				#START TIME
				ev_stime = esheet.acell(C_START_TIME + str(ev_idx)).value
				ev_stime = ''.join(ev_stime.split()) #remove all whitespace characters
				ev_stime = ev_stime.lower()
				ev_stime = ev_stime.replace('a.m', 'am')
				ev_stime = ev_stime.replace('p.m', 'pm')
				ev_sampm = ''
				if 'am' in ev_stime:
					ev_sampm = 'AM'
					ev_stime = ev_stime.replace('am', '')
				elif 'pm' in ev_stime:
					ev_sampm = 'PM'
					ev_stime = ev_stime.replace('pm', '')
				else:
					print 'Error. No AM/PM in start time'
					exit()
	
				stime_split = re.split(r"[;.:]", ev_stime)
				ev_shour = stime_split[0]
				ev_smin = stime_split[1]
					
	
				#END TIME
				ev_etime = esheet.acell(C_END_TIME + str(ev_idx)).value
				ev_etime = ''.join(ev_etime.split()) #remove all whitespace characters
				ev_etime = ev_etime.lower()
				ev_etime = ev_etime.replace('a.m', 'am')
				ev_etime = ev_etime.replace('p.m', 'pm')
				ev_eampm = ''
				if 'am' in ev_etime:
					ev_eampm = 'AM'
					ev_etime = ev_etime.replace('am', '')
				elif 'pm' in ev_etime:
					ev_eampm = 'PM'
					ev_etime = ev_etime.replace('pm', '')
				else:
					print 'Error. No AM/PM in end time'
					exit()
	
				etime_split = re.split(r"[;.:]", ev_etime)
				ev_ehour = etime_split[0]
				ev_emin = etime_split[1]
	
				#VENUE
				ev_venue = esheet.acell(C_VENUE + str(ev_idx)).value
	
				#ADDRESS LINE1
				ev_addr_l1 = esheet.acell(C_ADDR_LINE1 + str(ev_idx)).value
	
				#ADDRESS LINE2
				ev_addr_l2 = esheet.acell(C_ADDR_LINE2 + str(ev_idx)).value
	
				#CITY
				ev_city = esheet.acell(C_CITY + str(ev_idx)).value
	
				#STATE
				ev_state = esheet.acell(C_STATE + str(ev_idx)).value
	
				#ZIP
				ev_zip = esheet.acell(C_ZIP + str(ev_idx)).value
	
				print 'Event name: ' + ev_name
				print 'Event month: ' + ev_month
				print 'Event date: ' + ev_date
				print 'Event year: ' + ev_year
				print 'Event start hour: ' + ev_shour
				print 'Event start min: ' + ev_smin
				print 'Event start AM/PM: ' + ev_sampm
				print 'Event end hour: ' + ev_ehour
				print 'Event end min: ' + ev_emin
				print 'Event end AM/PM: ' + ev_eampm
				print 'Event venue: ' + ev_venue
				print 'Event Addr Line1: ' + ev_addr_l1
				print 'Event Addr Line2: ' + ev_addr_l2
				print 'Event city: ' + ev_city
				print 'Event state: ' + ev_state
				print 'Event zip: ' + ev_zip
	
				eventbrite(ev_name, ev_month, ev_date, ev_year, ev_shour, ev_smin, 
						ev_sampm, ev_ehour, ev_emin, ev_eampm, ev_venue, 
						ev_addr_l1, ev_addr_l2, ev_city, ev_state, ev_zip, ev_desc, ev_poster, ev_url)

				patch(ev_name, ev_month, ev_date, ev_year, ev_shour, ev_smin, 
						ev_sampm, ev_ehour, ev_emin, ev_eampm, ev_venue, 
						ev_addr_l1, ev_addr_l2, ev_city, ev_state, ev_zip, ev_desc, ev_poster, ev_url)

				esheet.update_acell(C_POSTING_STATUS + str(ev_idx), 'POSTED')
	
			ev_idx = ev_idx + 1
		else:
			break

print 'Job complete. Exiting ..'

