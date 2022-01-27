#NOTE: share the google sheet with harini@ishaonlineposting.iam.gserviceaccount.com
#To read from a cell: testsheet.acell(CELL).value; to write: esheet.update_acell(C_EVENT_TYPE + str(ev_idx), new_name)

############################# SETTINGS ################################

#FLAGS
DEBUG = 0 #Debug event posting by turning off GSHEET reading

#Copy and paste the workbook URL here:
#WORKBOOKURL = 'https://docs.google.com/spreadsheets/d/1X7WS6spYZfV2o40Hy2e_D9jZcOD3mlQ6yjcN3UZykDQ/edit?ts=5ae13571#gid=0'
WORKBOOKURL = 'https://docs.google.com/spreadsheets/d/1oF0m7C4_XIC5WuSNWkj6Cpre63bopaBRxHbjDCe_hV0/edit#gid=1881966630'

C_JOURNALIST_NAME = 'A'
C_VERDICT = 'E'
START_ROW = 2506

#################################################################################
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains, keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
from fake_useragent import UserAgent

chrome_options = webdriver.ChromeOptions()
ua = UserAgent()
userAgent = ua.random
#chrome_options.add_argument(f'user-agent={userAgent}')

#chrome_options.add_argument("--headless")

#denugger stuff
import pdb

import random
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

ser = Service(chromedriver_path)

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

search_phrases = ["ecolog", "environment", "agricultur", "plants", "natur", "climate", "soil", "biology", "ecosystem", "pollution"]

#Eventbrite posting
def func(): 

       browser_eb.append(webdriver.Chrome(service=ser,
                              options=chrome_options))
       #browser_eb.append(webdriver.Chrome('/usr/local/bin/chromedriver'))
       browser = browser_eb[len(browser_eb)-1]
       wait = WebDriverWait(browser, 60)

       #read gsheet and get the journalist names. Do the search and count if any phrase in search_phrases are present
       ev_idx = START_ROW

       import gspread
       from oauth2client.service_account import ServiceAccountCredentials
      
       scope = ['https://spreadsheets.google.com/feeds',
                  'https://www.googleapis.com/auth/drive']
      
       credentials = ServiceAccountCredentials.from_json_keyfile_name('IshaOnlinePosting.json', scope)
      
       gc = gspread.authorize(credentials)
      
       #NOTE: operating on the first worksheet in a workbook. Fix here if otherwise..
       esheet = gc.open_by_url(WORKBOOKURL).get_worksheet(1)

       while 1:
         if esheet.acell(C_JOURNALIST_NAME + str(ev_idx)).value:
             jname = esheet.acell(C_JOURNALIST_NAME + str(ev_idx)).value
             print('Parsing ' + jname)
             jname = jname.replace(' ', '+')
             browser_eb.append(webdriver.Chrome(service=ser,
                              options=chrome_options))
             #browser_eb.append(webdriver.Chrome('/usr/local/bin/chromedriver'))
             browser = browser_eb[len(browser_eb)-1]
             wait = WebDriverWait(browser, 60)
             browser.get('https://www.google.com/search?q='+'news+articles+by+reporter+'+jname)
             count = 0
             for phrase in search_phrases:
                 if phrase in browser.page_source:
                     count += 1
             esheet.update_acell(C_VERDICT + str(ev_idx), str(count))
             ev_idx = ev_idx + 1
             random.seed(ev_idx)
             time.sleep(30+random.random()%20)
             browser.close()

         else:
             break
             #pdb.set_trace()
             #print(jname)
             #break

       #browser.get('https://www.google.com/search?q=python')

       #count = 0

       #for phrase in search_phrases:
       #    if phrase in browser.page_source:
       #        count += 1
       
       #print('Final count is ' + str(count))
       #browser.close()
     
func()
      
print('Job complete. Exiting ..')

