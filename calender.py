#import datetime
#import os.path
#from googleapiclient.discovery import build
#from google_auth_oauthlib.flow import InstalledAppFlow
#from google.auth.transport.requests import Request
#from google.oauth2.credentials import Credentials


#SCOPES = ['https://www.googleapis.com/auth/calendar']

#def check_signin():
#  creds = None

  #if os.path.exists('token.json'):
  #  creds = Credentials.from_authorized_user_file('token.json', #SCOPES)
  #if(creds):
  #  return True
  #else:
  #  return False
  
#def signin():
  #creds = None
  #if not creds or not creds.valid:
   # 
    #if not creds:
     # creds.refresh(Request())
    #if creds.expired: 
     # creds.refresh(Request())
    #if creds.refresh_token:
     # creds.refresh(Request())
    
     # flow = InstalledAppFlow.from_client_secrets_file(
    ###########    'credentials/json',
     ####   SCOPES
    #  )#
#
     # creds = flow.run_local_server(port=0)
#########
    #  with open('token.json', 'w') as t:
    #    t.write(creds.to_json())

#d#ef build_cal():
  #creds = Credentials.from_authorized_user_file('token.json', SCOPES)
 # service = build('calender', 'v3', credentials=creds)
 # return service


#def create_event(summary, service):
 # event = service.events().quickAdd(
 #   calender='primary',
 #   text='Remember to do a workout and take your medications Today!'
 # ).execute()

#signed_in = check_signin()
#i#f(signed_in == False):
  #signin()

#calender = build_cal()

#create_event('Remember to do a workout and take your medications #Today!', calender)

