import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('IshaOnlinePosting-f601765b7565.json', scope)

gc = gspread.authorize(credentials)

testsheet = gc.open("Online_posting_test_sheet").sheet1

#event_column = raw_input("Enter the ColumnID of the event in the spreadsheet (e.g. AH)")

event_column = 'A'

#hardcoding row numbers for various details
r_evname = 1
r_evday = 2
r_evdate = 3
r_evtime = 4
r_evloc = 5
r_evaddr = 6
r_evcity = 7
r_evzip = 8

evname = testsheet.acell(event_column + str(r_evname)).value
evday = testsheet.acell(event_column + str(r_evday)).value
evdate = testsheet.acell(event_column + str(r_evdate)).value
evtime = testsheet.acell(event_column + str(r_evtime)).value
evloc = testsheet.acell(event_column + str(r_evloc)).value
evaddr = testsheet.acell(event_column + str(r_evaddr)).value
evcity = testsheet.acell(event_column + str(r_evcity)).value
evzip = testsheet.acell(event_column + str(r_evzip)).value

print evname
print evday
print evtime
print evloc
print evaddr
print evcity
print evzip
