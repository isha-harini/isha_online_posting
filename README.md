# isha_online_posting
Script for posting to the websites.

1. Download and install python3 (script was tested for Python3.6)

2. Copy the permissions file (IshaOnlinePosting.json) to this directory.

3. Change line 10 of online_posting.py to reflect the URL of your events sheet. 

4. Share the events sheet with the client email mentioned in IshaOnlinePosting.json

5. Run the following commad to install required packages

            python installer.py
    
6. Test if the installations went well

            python hello_world.py
            python hello_world_gsheet.py
            
7. Finally, run the script

            python online_posting.py
            
You need not repeat (1) to (6) everytime you need to post an event. It is needed only once to setup your computer if you are using the same events sheet


Currently works for:
1. Eventbrite
2. Patch
3. Meetup
4. Isha Portal
