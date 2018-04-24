import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('IshaOnlinePosting-f601765b7565.json', scope)

gc = gspread.authorize(credentials)

testsheet = gc.open("Online_posting_test_sheet").sheet1

#get value
val = testsheet.acell('A1').value
val2 = testsheet.acell('A2').value

print 'A1 is ' + val
print 'A2 is ' + val2
