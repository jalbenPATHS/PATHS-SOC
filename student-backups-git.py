#program to automatically generate daily files for students to backup
#file hashes will be uploaded to google sheets to verify during file recovery labs
#Nate Jalbert 2019-10-13 nrjalbert@gmail.com
#install pip3 gspread and oauth2client
import time
import random
import hashlib
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
#this will be added to column 2 of the spreadsheet
student_no = 12345
#this will be the sheet to add the data to based on the VM
OS = "sheet1"
# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
#Insert your Google Sheets API JSON File
creds = ServiceAccountCredentials.from_json_keyfile_name('*.json', scope)
client = gspread.authorize(creds)
#alphabet for the loop
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#grab today's date for the file name and entropy
today = datetime.today()
rightnow = datetime.now()
#create a new file yyyy-mm-dd.txt
fname = str(today.year)+"-"+str(today.month)+"-"+str(today.day)
file = open(fname+".txt","w+")
#create a new file based on current seconds and random number
rand = random.randint(1,10)
rand = rand*rightnow.second
#loop to create a random string of letters and add to the new file
for i in range (0,rand):
    randletter = random.randint(0,25)
    temp_letter = alpha[randletter]
    file.write(temp_letter)
file.close()


#calculate the hash of the new file
file = open(fname+".txt","rb")
bytes = file.read() 
readable_hash = hashlib.sha256(bytes).hexdigest();
#print(readable_hash)
file.close()


#open this google sheet
sheet = client.open("Spreadsheet")
#which worksheet to select
worksheet = sheet.worksheet(OS)
#add the data to the end of the sheet
worksheet.append_row([fname,student_no,fname+".txt",readable_hash])


