#NOTE: share the google sheet with harini@ishaonlineposting.iam.gserviceaccount.com
#To read from a cell: testsheet.acell(CELL).value; to write: esheet.update_acell(C_EVENT_TYPE + str(ev_idx), new_name)

############################# SETTINGS ################################

#FLAGS
DEBUG = 0 #Debug event posting by turning off GSHEET reading

#Copy and paste the workbook URL here:
#WORKBOOKURL = 'https://docs.google.com/spreadsheets/d/1X7WS6spYZfV2o40Hy2e_D9jZcOD3mlQ6yjcN3UZykDQ/edit?ts=5ae13571#gid=0'
WORKBOOKURL = 'https://docs.google.com/spreadsheets/d/1fLOhwdIiVOQaNHdrKYt6JeY924jW66Ag6I-r2av-LhQ/edit?usp=sharing'

#Column names of different event details
C_EVENT_TYPE = 'A'
C_POSTING_STATUS = 'B'
C_DATE = 'G'
C_START_TIME = 'H'
C_END_TIME = 'I'
C_VENUE = 'J'
C_ADDR_LINE1 = 'K'
C_ADDR_LINE2 = 'L'
C_CITY = 'M'
C_STATE = 'O'
C_ZIP = 'N'
C_CENTERID = 'O'
C_HOST = 'T'
C_PRESENTER = 'U'
START_ROW = 116

#login details
#Eventbrite
eb_login = 'detroit@ishausa.org'
eb_password = 'j0y247LetUsMakeitHappen!'

#Patch
patch_login = 'isha.harini.umich@gmail.com'
patch_password = 'Dhyanalinga247'

#Meetup
meetup_login = 'isha.harini.umich@gmail.com'
meetup_password = 'Dhyanalinga247'

#Isha site
isha_login = 'hmuthukrishnan'
isha_password = 'Dhyanalinga247'

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
from geopy.geocoders import Nominatim
from datetime import datetime

#denugger stuff
import pdb

import re
import time
import smtplib
#from email.MIMEMultipart import MIMEMultipart
#from email.MIMEText import MIMEText
from datetime import datetime

#sort out chromedriver
chromedriver_path = ''
import os
import sys
if os.name == 'nt':
      chromedriver_path = 'win/chromedriver.exe'
elif os.name == 'posix':
      if not ('linux' in sys.platform.lower()):
            chromedriver_path = 'mac/chromedriver'
      else:
            print('Unrecognized platform')
            exit()
else:
      print('Unrecognized platform')
      exit()

cwd = os.getcwd()

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
browser_meetup = []
browser_isha = []


#Eventbrite posting
def eventbrite(ev_name, ev_month, ev_date, ev_year, ev_shour, ev_smin, 
                   ev_sampm, ev_ehour, ev_emin, ev_eampm, ev_venue, 
                         ev_addr_l1, ev_addr_l2, ev_city, ev_state, ev_zip, ev_desc, ev_poster, ev_url): 

       browser_eb.append(webdriver.Chrome(chromedriver_path))
       #browser_eb.append(webdriver.Chrome('/usr/local/bin/chromedriver'))
       browser = browser_eb[len(browser_eb)-1]
       wait = WebDriverWait(browser, 60)
       browser.get('https://www.eventbrite.com/create')
       
       #login and password
       
       curpath = "//*[@id='signin-email']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, curpath)))
       ele.send_keys(eb_login)
                  
       curpath = "//*[@id='root']/div/div[2]/div/div/div/div[1]/div/main/div/div/div/div[2]/form/div[2]/button"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, curpath)))
       ele.click()
       
       curpath = "//*[@id='password']"
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
       #path = "//*[@id='location_edit_form']/div[2]/div[3]/div/select"
       #ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       #for option in ele.find_elements_by_tag_name('option'):
       #    if option.text == 'United States':
       #        option.click()
       #        break
       
       
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
       
       print(bcolors.HEADER + 'Completed posting to Eventbrite' + bcolors.ENDC)

#Patch posting
def patch(ev_name, ev_month, ev_date, ev_year, ev_shour, ev_smin, 
              ev_sampm, ev_ehour, ev_emin, ev_eampm, ev_venue, 
                  ev_addr_l1, ev_addr_l2, ev_city, ev_state, ev_zip, ev_desc, ev_poster, ev_url): 

       browser_pat.append(webdriver.Chrome(chromedriver_path))
       #browser_pat.append(webdriver.Chrome('/usr/local/bin/chromedriver'))
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
       
       browser.get('https://my.patch.com/node/add/calendar-item')
       #path = "//*[@id='block-system-main']/div[3]/div[1]/a"
       #path = "//*[@id='block-system-main']/section[2]/section[1]/a/span[2]"
       #ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       #ele.click()
       
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
       #path = "//*[@id='edit-share-nearby']"
       #ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       #ele.click()
       
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
       
       actions = ActionChains(browser); actions.send_keys(Keys.TAB); actions.perform()
       actions = ActionChains(browser); actions.send_keys(Keys.TAB); actions.perform()
       actions = ActionChains(browser); actions.send_keys(ev_venue + ', ' + ev_addr_l1 + ', ' + ev_addr_l2 + ', ' + ev_city + ', ' + state_name[ev_state] + ' ' + ev_zip); actions.perform()
       
       #venue
       #path = "//*[@id='edit-field-calendar-address-und-0-name-line']"
       #ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       #ele.send_keys(ev_venue)
       
       #addr line 1
       #path = "//*[@id='edit-field-calendar-address-und-0-thoroughfare']"
       #ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       #ele.send_keys(ev_addr_l1)
       #
       ##addr line 2
       #path = "//*[@id='edit-field-calendar-address-und-0-premise']"
       #ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       #ele.send_keys(ev_addr_l2)
       #
       ##city
       #path = "//*[@id='edit-field-calendar-address-und-0-locality']"
       #ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       #ele.send_keys(ev_city)
       #
       ##state
       #path = "//*[@id='edit-field-calendar-address-und-0-administrative-area']"
       #ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       #for option in ele.find_elements_by_tag_name('option'):
       #     if option.text.lower() == state_name[ev_state].lower():
       #         option.click()
       #         break
       #
       ##zip
       #path = "//*[@id='edit-field-calendar-address-und-0-postal-code']"
       #ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       #ele.send_keys(ev_zip)
       
       
       #event desc
       path = "//*[(@id = 'redactor-uuid-0')]"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       ele.send_keys(ev_desc)
       
       #event url
       path = "//*[(@id = 'edit-field-calendar-link-und-0-url')]"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       ele.send_keys(ev_url)
       
       print(bcolors.HEADER + 'Completed posting to Patch' + bcolors.ENDC)

#Meetup posting
def meetup(ev_name, ev_month, ev_date, ev_year, ev_shour, ev_smin, 
              ev_sampm, ev_ehour, ev_emin, ev_eampm, ev_venue, 
                  ev_addr_l1, ev_addr_l2, ev_city, ev_state, ev_zip, ev_desc, ev_poster, ev_url): 

       browser_meetup.append(webdriver.Chrome(chromedriver_path))
       #browser_meetup.append(webdriver.Chrome('/usr/local/bin/chromedriver'))
       browser = browser_meetup[len(browser_meetup)-1]
       month_list_meetup = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
       
       wait = WebDriverWait(browser, 60)
       browser.get('https://secure.meetup.com/login/')
       
       ##credentials
       path = "//*[@id='email']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       ele.send_keys(meetup_login)
       
       path = "//*[@id='password']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       ele.send_keys(patch_password)
       
       path = "//*[@id='loginForm']/div/div[3]/input"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       ele.click()
       
       time.sleep(3)
       
       browser.get('https://www.meetup.com/Isha-Yoga-Detroit-Free-Meditation-Classes/schedule/#changeVenue')

       time.sleep(3)
       
       #event name
       path = "//*[@id='name']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       ele.send_keys(ev_name)

       ##date
       actions = ActionChains(browser)
       actions.send_keys(Keys.TAB)
       actions.perform()

       #identify current month
       name = "cur-month"
       ele = wait.until(EC.presence_of_element_located((By.CLASS_NAME, name)))
       #cur_month = ele.text

       #find the month number
       #idx = 0
       #while idx < 12:
       #     idx = idx + 1
       #     print('Cur Month: ' + cur_month.lower() + 'List month: ' + month_list_meetup[idx - 1])
       #     if month_list_meetup[idx - 1].lower() in cur_month.lower():
       #           break
       idx = datetime.now().month - 1
       if idx > 11:
            print('Something went wrong')
            exit()
       

       #number of clicks to reach correct month
       #if idx > int(ev_month): #month is in the next year
       #   num_clicks = int(ev_month) + 12 - idx
       #else:
       #   num_clicks = int(ev_month) - idx

       #time.sleep(3)

       #while num_clicks > 0:
       #   path = "/html/body/div[3]/div[1]/span[2]"
       #   ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       #   ele.click()
       #   num_clicks = num_clicks - 1
       #   time.sleep(3)

       ##date
       #idx = 1
       #while 1:
       #     path = '/html/body/div[2]/div[2]/div/div[2]/div/span[' + str(idx) + ']'                        
       #     ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       #     if ele.text == '1':
       #         break
       #     idx = idx + 1

       #date_idx = idx + int(ev_date) - 1
       #path = '/html/body/div[2]/div[2]/div/div[2]/div/span[' + str(date_idx) + ']'                        
       #ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       #ele.click()

       #start time
       path = "//*[@id='start_time']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       input_data = ev_shour + ':' + ev_smin
       ele.send_keys(input_data)
       ele.send_keys(ev_sampm)

       #end time
       path = "//*[@id='end_time']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       input_data = ev_ehour + ':' + ev_emin
       ele.send_keys(input_data)
       ele.send_keys(ev_eampm)

       #add location
       path = "//*[@id='searchVenues-searchResultInput']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       ele.send_keys(ev_venue)

       actions = ActionChains(browser)
       actions.send_keys(Keys.ESCAPE)
       actions.perform()

       path = "//*[@id='mupMain']/form/div[1]/div/div/section[4]/div/div/section/div/fieldset/div[1]/button"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       ele.click()

       #venue name
       actions = ActionChains(browser); actions.send_keys(Keys.TAB); actions.perform()
       actions = ActionChains(browser); actions.send_keys(Keys.TAB); actions.perform()
       actions = ActionChains(browser); actions.send_keys(ev_venue); actions.perform()

       #addr line1
       path = "//*[@id='address_1']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       ele.send_keys(ev_addr_l1)

       #addr line2
       path = "//*[@id='address_2']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       ele.send_keys(ev_addr_l2)

       #city
       path = "//*[@id='city']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       ele.send_keys(ev_city)

       #zip
       path = "//*[@id='zip']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       ele.send_keys(ev_zip)

       #state
       path = "//*[@id='state']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       for option in ele.find_elements_by_tag_name('option'):
            if option.text.lower() == state_name[ev_state].lower():
                option.click()
                break

       #submit
       path = "//*[@id='mupMain']/form/div[1]/div/div/section[4]/div/div/section/div/fieldset/fieldset/div[8]/div/div[2]/button"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       ele.click()

       #image upload
       path = "//*[@id='eventScheduleForm']/section[4]/div/div/section/div/div[2]/div/input"
       path = "//*[@id='uploadButton-submit']/input"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       ele.send_keys(ev_poster)

       time.sleep(3) 
       #finish
       path = "//*[@id='uploadButton-submit']/div[1]/div/div[2]/div[2]/div[3]/button/span"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       ele.click()
       time.sleep(3) 

       #desc
       path = "//*[@id='description']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       ele.send_keys(ev_desc)

       #attendee limit
       path = "//*[@id='rsvp_limit']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       ele.send_keys('108')

       #path = "//*[@id='eventScheduleForm']/section[5]/div/div/section/div/div[6]/label/div/div[1]/span"
       #ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       #ele.click()
       
       print(bcolors.HEADER + 'Completed posting to Meetup' + bcolors.ENDC)

#Isha site posting
def ishasite(ev_name, ev_month, ev_date, ev_year, ev_shour, ev_smin, 
              ev_sampm, ev_ehour, ev_emin, ev_eampm, ev_venue, 
                  ev_addr_l1, ev_addr_l2, ev_city, ev_state, ev_zip, ev_desc, ev_poster, ev_url, centerId, ev_host, ev_presenter):
       
       browser_isha.append(webdriver.Chrome(chromedriver_path))
       #browser_isha.append(webdriver.Chrome('/usr/local/bin/chromedriver'))
       browser = browser_isha[len(browser_isha)-1]
       
       wait = WebDriverWait(browser, 60)
       browser.get('https://innerengineering.com/ieo/newadmin/login.php')

       #credentials
       path = "//*[@id='login']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       ele.send_keys(isha_login)
 
       path = "//*[@id='password']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       ele.send_keys(isha_password)
      
       path = "/html/body/div/form/div/div[3]/button"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       ele.click()

       time.sleep(3) 
       browser.get('https://innerengineering.com/ieo/newadmin/freeEvents.php?act=Add')

       time.sleep(3) 
       #event type
       path = "//*[@id='event_type_id']"                 
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       for option in ele.find_elements_by_tag_name('option'):
             if option.text.lower() in ev_name.lower():
                option.click()
                break

       #event desc
       path = "//*[@id='event_desc']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       ele.send_keys(ev_desc)

       #address line 1
       path = "//*[@id='address_line1']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       ele.send_keys(ev_addr_l1)

       #address line 2
       path = "//*[@id='address_line2']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       ele.send_keys(ev_addr_l2)

       #city
       path = "//*[@id='city']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       ele.send_keys(ev_city)

       #state
       path = "//*[@id='usState']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       for option in ele.find_elements_by_tag_name('option'):
            if option.text.lower() == state_name[ev_state].lower():
                option.click()
                break

       #zip code
       path = "//*[@id='zipcode']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       ele.send_keys(ev_zip)

       geolocator = Nominatim()
       addr = ev_addr_l1 + ', ' + ev_city + ', ' + ev_state
       location = geolocator.geocode(addr)

       #latitude
       path = "//*[@id='lat']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       ele.send_keys(str(location.latitude))

       #longitude
       path = "//*[@id='lng']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       ele.send_keys(str(location.longitude))

       actions = ActionChains(browser) 
       actions.send_keys(Keys.TAB)
       actions.perform()

       #event date
       path = "//*[@id='event_st_dt']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       date = ev_year + '-' + ev_month + '-' + ev_date
       ele.clear()
       ele.send_keys(date)

       #start time
       path = "//*[@id='event_start_time']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       stime = ev_shour + ':' + ev_smin + ' ' + ev_sampm.upper()
       ele.send_keys(stime)

       #end time
       path = "//*[@id='event_end_time']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       etime = ev_ehour + ':' + ev_emin + ' ' + ev_eampm.upper()
       ele.send_keys(etime)

       #event category
       path = "//*[@id='event_cat_id']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       for option in ele.find_elements_by_tag_name('option'):
            if option.text == 'Other':
                option.click()
                break

       #center ID
       path = "//*[@id='centerId']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       for option in ele.find_elements_by_tag_name('option'):
            if option.text.lower() == centerId.lower():
                option.click()
                break

       #public event
       path = "//*[@id='event_type']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       ele.click()

       #host
       path = "//*[@id='host']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       ele.send_keys(ev_host)

       actions = ActionChains(browser) 
       actions.send_keys(Keys.TAB)
       actions.perform()

       #presenter
       path = "//*[@id='presenter']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       ele.send_keys(ev_presenter)

       #status
       path = "//*[@id='evtStatus']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       for option in ele.find_elements_by_tag_name('option'):
            if option.text.lower() == 'active':
                option.click()
                break

       #Program details
       #type
       path = "//*[@id='evt_pgmId1']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       for option in ele.find_elements_by_tag_name('option'):
            if option.text.lower() in ev_name.lower():
                option.click()
                break

       #start time
       path = "//*[@id='evt_start_time1']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       ele.send_keys(stime)

       #end time
       path = "//*[@id='evt_end_time1']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       ele.send_keys(etime)

       #RSVP
       path = "//*[@id='main-content']/div[1]/div[2]/div/div/div[4]/div[4]/div/input"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       ele.click()

       print(bcolors.HEADER + 'Completed posting to Isha portal' + bcolors.ENDC)
       

#Isha site posting
def ishasite_tab(ev_name, ev_month, ev_date, ev_year, ev_shour, ev_smin, 
              ev_sampm, ev_ehour, ev_emin, ev_eampm, ev_venue, 
                  ev_addr_l1, ev_addr_l2, ev_city, ev_state, ev_zip, ev_desc, ev_poster, ev_url, centerId, ev_host, ev_presenter):
       
       browser_isha.append(webdriver.Chrome(chromedriver_path))
       #browser_isha.append(webdriver.Chrome('/usr/local/bin/chromedriver'))
       browser = browser_isha[len(browser_isha)-1]
       
       wait = WebDriverWait(browser, 60)
       browser.get('https://innerengineering.com/ieo/newadmin/login.php')

       #credentials
       path = "//*[@id='login']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       ele.send_keys(isha_login)
 
       path = "//*[@id='password']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       ele.send_keys(isha_password)
      
       path = "/html/body/div/form/div/div[3]/button"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       ele.click()

       time.sleep(3) 
       browser.get('https://innerengineering.com/ieo/newadmin/freeEvents.php?act=Add')

       time.sleep(3) 
       #event type
       path = "//*[@id='event_type_id']"                 
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       for option in ele.find_elements_by_tag_name('option'):
             if option.text.lower() in ev_name.lower():
                option.click()
                break

       #country
       actions = ActionChains(browser); actions.send_keys(Keys.TAB); actions.perform()

       #state       
       actions = ActionChains(browser); actions.send_keys(Keys.TAB); actions.perform()
       actions = ActionChains(browser); actions.send_keys("Michigan"); actions.perform()

       #Category
       actions = ActionChains(browser); actions.send_keys(Keys.TAB); actions.perform()
       actions = ActionChains(browser); actions.send_keys("Other"); actions.perform()

       #Center Id
       actions = ActionChains(browser); actions.send_keys(Keys.TAB); actions.perform()
       actions = ActionChains(browser); actions.send_keys("Detroit MI"); actions.perform()

       #Event Status
       actions = ActionChains(browser); actions.send_keys(Keys.TAB); actions.perform()
       actions = ActionChains(browser); actions.send_keys("Active"); actions.perform()

       #Program Type
       actions = ActionChains(browser); actions.send_keys(Keys.TAB); actions.perform()
       actions = ActionChains(browser); actions.send_keys(ev_name); actions.perform()

       #Event Description
       for i in range(1, 13):
            actions = ActionChains(browser); actions.send_keys(Keys.TAB); actions.perform()
            time.sleep(3)

       #Should have reached event descr
       actions = ActionChains(browser); actions.send_keys(ev_desc); actions.perform()

       #Address line 1
       #actions = ActionChains(browser); actions.send_keys(Keys.TAB); actions.perform()
       actions = ActionChains(browser); actions.send_keys(ev_addr_l1); actions.perform()

       #Address line 2
       actions = ActionChains(browser); actions.send_keys(Keys.TAB); actions.perform()
       actions = ActionChains(browser); actions.send_keys(ev_addr_l2); actions.perform()

       #City
       actions = ActionChains(browser); actions.send_keys(Keys.TAB); actions.perform()
       actions = ActionChains(browser); actions.send_keys(ev_city); actions.perform()

       #Zip code
       actions = ActionChains(browser); actions.send_keys(Keys.TAB); actions.perform()
       actions = ActionChains(browser); actions.send_keys(ev_zip); actions.perform()

       geolocator = Nominatim()
       addr = ev_addr_l1 + ', ' + ev_city + ', ' + ev_state
       location = geolocator.geocode(addr)
       #Latitude
       actions = ActionChains(browser); actions.send_keys(Keys.TAB); actions.perform()
       actions = ActionChains(browser); actions.send_keys(str(location.latitude)); actions.perform()

       #Longitude
       actions = ActionChains(browser); actions.send_keys(Keys.TAB); actions.perform()
       actions = ActionChains(browser); actions.send_keys(str(location.longitude)); actions.perform()

       #pdb.set_trace()

       #event date
       actions = ActionChains(browser); actions.send_keys(Keys.TAB); actions.perform()
       actions = ActionChains(browser); actions.send_keys(Keys.DELETE); actions.perform()
       date = ev_year + '-' + ev_month + '-' + ev_date
       actions = ActionChains(browser); actions.send_keys(date); actions.perform()
       
       #pdb.set_trace()

       #start time
       actions = ActionChains(browser); actions.send_keys(Keys.TAB); actions.perform()
       stime = ev_shour + ':' + ev_smin + ' ' + ev_sampm.upper()
       actions = ActionChains(browser); actions.send_keys(stime); actions.perform()

       #end time
       actions = ActionChains(browser); actions.send_keys(Keys.TAB); actions.perform()
       etime = ev_ehour + ':' + ev_emin + ' ' + ev_eampm.upper()
       actions = ActionChains(browser); actions.send_keys(etime); actions.perform()

       #host
       actions = ActionChains(browser); actions.send_keys(Keys.TAB); actions.perform()
       time.sleep(1)
       actions = ActionChains(browser); actions.send_keys(Keys.TAB); actions.perform()
       actions = ActionChains(browser); actions.send_keys(ev_host); actions.perform()

       #presenter
       actions = ActionChains(browser); actions.send_keys(Keys.TAB); actions.perform()
       actions = ActionChains(browser); actions.send_keys(ev_presenter); actions.perform()

       #Program details

       #start time
       actions = ActionChains(browser); actions.send_keys(Keys.TAB); actions.perform()
       actions = ActionChains(browser); actions.send_keys(stime); actions.perform()

       #end time
       actions = ActionChains(browser); actions.send_keys(Keys.TAB); actions.perform()
       actions = ActionChains(browser); actions.send_keys(etime); actions.perform()

       #RSVP
       #actions = ActionChains(browser); actions.send_keys(Keys.TAB); actions.perform()
       #actions = ActionChains(browser); actions.click(); actions.perform()

       #public event
       path = "//*[@id='event_type']"
       ele = wait.until(EC.presence_of_element_located((By.XPATH, path)))
       ele.click()

       print(bcolors.HEADER + 'Completed posting to Isha portal' + bcolors.ENDC)
       


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
       ev_addr_l1 = '1929 Plymouth Road'
       ev_addr_l2 = 'Room 3003'
       ev_city = 'Ann Arbor'
       ev_state = 'MI'
       ev_zip = '48105'
       ev_desc = 'You may either Hide or you may Seek; The domain of the Divine is open to all who Seek'
       ev_poster = '/Users/harini/Documents/GitHub/isha_online_posting/posters/ishakriya.jpg'
       ev_url = 'http://www.ishafoundation.org/Ishakriya'
       ev_centerId = 'Detroit MI'
       ev_host = 'Creation'
       ev_presenter = 'Creator'
       
       #eventbrite(ev_name, ev_month, ev_date, ev_year, ev_shour, ev_smin, 
        #   ev_sampm, ev_ehour, ev_emin, ev_eampm, ev_venue, 
         #      ev_addr_l1, ev_addr_l2, ev_city, ev_state, ev_zip, ev_desc, ev_poster, ev_url)
       
       #patch(ev_name, ev_month, ev_date, ev_year, ev_shour, ev_smin, 
        #   ev_sampm, ev_ehour, ev_emin, ev_eampm, ev_venue, 
         #      ev_addr_l1, ev_addr_l2, ev_city, ev_state, ev_zip, ev_desc, ev_poster, ev_url)

       #meetup(ev_name, ev_month, ev_date, ev_year, ev_shour, ev_smin, 
        #   ev_sampm, ev_ehour, ev_emin, ev_eampm, ev_venue, 
         #      ev_addr_l1, ev_addr_l2, ev_city, ev_state, ev_zip, ev_desc, ev_poster, ev_url)

       ishasite(ev_name, ev_month, ev_date, ev_year, ev_shour, ev_smin, 
           ev_sampm, ev_ehour, ev_emin, ev_eampm, ev_venue, 
               ev_addr_l1, ev_addr_l2, ev_city, ev_state, ev_zip, ev_desc, ev_poster, ev_url, ev_centerId, ev_host, ev_presenter)


elif DEBUG == 0:
      import gspread
      from oauth2client.service_account import ServiceAccountCredentials
      
      scope = ['https://spreadsheets.google.com/feeds',
      'https://www.googleapis.com/auth/drive']
      
      credentials = ServiceAccountCredentials.from_json_keyfile_name('IshaOnlinePosting.json', scope)
      
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
                 if 'mfb' in ev_type.lower():
                       print(bcolors.HEADER + 'Meditation for Beginners identified' + bcolors.ENDC)
                       ev_name = 'Meditation for Beginners'
                       ev_name = 'Meditation for Beginners (Isha Kriya) - Free Class'
                       desc_file = open("event_desc/isha_kriya.txt", "r")
                       ev_poster = cwd + '/posters/ishakriya.jpg'
                       ev_url = 'http://www.ishafoundation.org/Ishakriya'
                 
                 elif 'yfb' in ev_type.lower():
                       print(bcolors.HEADER + 'Yoga for Beginners identified' + bcolors.ENDC)
                       #ev_name = 'Yoga for Beginners'
                       ev_name = 'Yoga for Beginners - Free Class (Upa Yoga)'
                       desc_file = open("event_desc/yoga_for_beginners.txt", "r")
                       ev_poster = cwd + '/posters/yfb.jpg'
                       ev_url = 'http://isha.sadhguru.org/yoga/yoga-programs/upa-yoga/'
                 
                 elif 'yfs' in ev_type.lower():
                       print(bcolors.HEADER + 'Yoga for Success identified' + bcolors.ENDC)
                       #ev_name = 'Yoga for Success'
                       ev_name = 'Yoga For Success - Free and Open to All'
                       desc_file = open("event_desc/yoga_for_success.txt", "r")
                       ev_poster = cwd + '/posters/yfs.jpg'
                       ev_url = 'http://isha.sadhguru.org/yoga/yoga-programs/upa-yoga/'
                 
                 else:
                       print(bcolors.FAIL + 'Unsupported event name found in row ' + str(ev_idx) + bcolors.ENDC)
                       ans = input('What do you want to do? Answer with:\n rename: to give a new name to the event\n ignore: to ignore this event and continue with the next\n exit: to end the script. (r/i/e): ')
                       
                       if ans.lower().startswith('r'):
                           new_name = input('Input new name for event in row ' + str(ev_idx) + ': ')
                           esheet.update_acell(C_EVENT_TYPE + str(ev_idx), new_name)
                           continue
                       elif ans.lower().startswith('i'):
                           print(bcolors.HEADER + 'Okay. Proceeding to the next event' + bcolors.ENDC)
                           ev_idx = ev_idx + 1
                           continue
                       elif ans.lower().startswith('e'):
                           print(bcolors.HEADER + 'Okay. Exiting the script. Pranams' + bcolors.ENDC)
                           exit()
                       else:
                           print(bcolors.FAIL + 'Sorry. Unrecognized answer. Exiting the script' + bcolors.ENDC)
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
                      print('Error. No AM/PM in start time')
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
                      print('Error. No AM/PM in end time')
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
                 
                 #CenterID
                 ev_centerid = esheet.acell(C_CENTERID + str(ev_idx)).value

                 #Host
                 ev_host = esheet.acell(C_HOST + str(ev_idx)).value

                 #Presenter
                 ev_presenter = esheet.acell(C_PRESENTER + str(ev_idx)).value

                 print('Event name: ' + ev_name)
                 print('Event month: ' + ev_month)
                 print('Event date: ' + ev_date)
                 print('Event year: ' + ev_year)
                 print('Event start hour: ' + ev_shour)
                 print('Event start min: ' + ev_smin)
                 print('Event start AM/PM: ' + ev_sampm)
                 print('Event end hour: ' + ev_ehour)
                 print('Event end min: ' + ev_emin)
                 print('Event end AM/PM: ' + ev_eampm)
                 print('Event venue: ' + ev_venue)
                 print('Event Addr Line1: ' + ev_addr_l1)
                 print('Event Addr Line2: ' + ev_addr_l2)
                 print('Event city: ' + ev_city)
                 print('Event state: ' + ev_state)
                 print('Event zip: ' + ev_zip)
                 print('Event centerid: ' + ev_centerid)
                 print('Event host: ' + ev_host)
                 print('Event presenter: ' + ev_presenter)
                 
                 eventbrite(ev_name, ev_month, ev_date, ev_year, ev_shour, ev_smin, 
                               ev_sampm, ev_ehour, ev_emin, ev_eampm, ev_venue, 
                                  ev_addr_l1, ev_addr_l2, ev_city, ev_state, ev_zip, ev_desc, ev_poster, ev_url)
                 
                 patch(ev_name, ev_month, ev_date, ev_year, ev_shour, ev_smin, 
                              ev_sampm, ev_ehour, ev_emin, ev_eampm, ev_venue, 
                                  ev_addr_l1, ev_addr_l2, ev_city, ev_state, ev_zip, ev_desc, ev_poster, ev_url)
                 
                 meetup(ev_name, ev_month, ev_date, ev_year, ev_shour, ev_smin, 
                              ev_sampm, ev_ehour, ev_emin, ev_eampm, ev_venue, 
                                  ev_addr_l1, ev_addr_l2, ev_city, ev_state, ev_zip, ev_desc, ev_poster, ev_url)

                 ishasite_tab(ev_name, ev_month, ev_date, ev_year, ev_shour, ev_smin, 
                              ev_sampm, ev_ehour, ev_emin, ev_eampm, ev_venue, 
                                  ev_addr_l1, ev_addr_l2, ev_city, ev_state, ev_zip, ev_desc, ev_poster, ev_url, ev_centerid, ev_host, ev_presenter)

                 print('Please verify and complete the event posting')

                 compl = input('Answer with:\nComplete: to mark posting complete and move on to the next event\n ignore: to ignore this event and move on to the next event\n repost: to repost the current event;\n exit: to quit (c/i/r/e): ')
                 if compl.lower().startswith('c'):
                       print("Okay. Moving to the next event if any")
                       esheet.update_acell(C_POSTING_STATUS + str(ev_idx), 'POSTED')
                 elif compl.lower().startswith('i'):
                       print("Okay. Ignoring current event and moving to the next event if any")
                 elif compl.lower().startswith('r'):
                       print("Okay. Reposting the event")
                       ev_idx = ev_idx - 1
                 elif compl.lower().startswith('e'):
                       print("Okay. Exiting the script")
                       exit()
                 else:
                       print("Unrecognized input. Exiting")
                       exit()
             
             ev_idx = ev_idx + 1
         else:
              break

print('Job complete. Exiting ..')

