#NOTE: share the google sheet with harini@ishaonlineposting.iam.gserviceaccount.com
#To read from a cell: testsheet.acell(CELL).value; esheet.update_acell(C_EVENT_TYPE + str(ev_idx), new_name)

############################# SETTINGS ################################

#Copy and paste the workbook URL here:
WORKBOOKURL = 'https://docs.google.com/spreadsheets/d/1X7WS6spYZfV2o40Hy2e_D9jZcOD3mlQ6yjcN3UZykDQ/edit?ts=5ae13571#gid=0'

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




#################################################################################

import gspread
import re
from oauth2client.service_account import ServiceAccountCredentials

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

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('IshaOnlinePosting-f601765b7565.json', scope)

gc = gspread.authorize(credentials)

#NOTE: operating on the first worksheet in a workbook. Fix here if otherwise..
esheet = gc.open_by_url(WORKBOOKURL).get_worksheet(0)

ev_idx = START_ROW

while 1:
	if esheet.acell(C_EVENT_TYPE + str(ev_idx)).value:
		if not esheet.acell(C_POSTING_STATUS + str(ev_idx)).value: #not yet posted
			#EVENT TYPE
			ev_type = esheet.acell(C_EVENT_TYPE + str(ev_idx)).value
			ev_name = ''
			if 'meditation for beginners' in ev_type.lower():
				print bcolors.HEADER + 'Meditation for Beginners identified' + bcolors.ENDC
				ev_name = 'Meditation for Beginners'
			elif 'yoga for beginners' in ev_type.lower():
				print bcolors.HEADER + 'Yoga for Beginners identified' + bcolors.ENDC
				ev_name = 'Yoga for Beginners'
			elif 'yoga for success' in ev_type.lower():
				print bcolors.HEADER + 'Yoga for Success identified' + bcolors.ENDC
				ev_name = 'Yoga for Success'
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

			esheet.update_acell(C_POSTING_STATUS + str(ev_idx), 'POSTED')

		ev_idx = ev_idx + 1
	else:
		break




