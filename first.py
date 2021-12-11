
import pyaarlo                                                                           
                                                                                                                                                                                    
from datetime import timedelta, date                                                
import datetime                                                                          
import getpass                                                                           
import sys
import requests 
import time        
import os   


# creates these directories...
basepath = os.getcwd()
if not os.path.isdir(f"{basepath}/videos"):
    os.mkdir(f"{basepath}/videos")                                               
                                                                                                                                                                                    
email = input("Enter your Arlo email address: ")                                         
pword = getpass.getpass(prompt="Enter password: ")                                       
                                                                                                                                                                                    
# login                                               
arlo = pyaarlo.PyArlo(username = email, password = pword, tfa_type = "SMS", tfa_source = "console", synchronous_mode = True) #, refresh_devices_every = 3)                                       
                                                                                                                                                                                    
print("\nSuccessfully connected to your Arlo account!\n")                                    
                                                                                                                                                                                    
#get our ArloCameras                                                                     
garage = arlo.cameras[0]                                                                   
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
dates_videos = {} # here, the keys will be unique dates, and then the videos_list will be appended to each date. If there are 30 keys, delete the first ever one

while garage.is_on:
        timestamp = datetime.datetime.now().strftime("%H:%M:%S") 
        latest_video = garage.last_video # callback to pyaarlo --> checking latest video every callback
        video_name = f"{basepath}/videos/garage_{date.today()}_{timestamp}.mp4"
        print(f"Record from the past 30 days: {dates_videos}\n")
        url = latest_video.url
        if date.today() not in dates_videos.keys(): # if we already have an entry for today...
                        dates_videos[date.today()] = [] # ...create a new list for this day
        print(f"Videos collected today: {dates_videos[date.today()]}\n")

        match = False
        for item in dates_videos[date.today()]:
                compare_url = item[0]
                if compare_url == url:
                        match = True

        if match == False: # save video, it is NOT anywhere in today's specific list values
                r = requests.get(url)
                open(f"{video_name}", "wb").write(r.content)
                dates_videos[date.today()].append((url, video_name)) # ...append tuple (url, saved_video_name) to the established list
                        
        # delete the videos after x amount of days
        if len(dates_videos) == 30:
                i = 0
                for key in dict.keys():
                        if i == 0:
                                # delete the videos from the file system, then delete entire k:v pair from dictionary
                                video_delete = dates_videos[key][1]
                                os.remove(video_delete)
                                del dates_videos[key]
                                break

        # check every {interval} seconds for an update
        time.sleep(60)
        continue