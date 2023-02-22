import requests
import json

# Important
key = "AIzaSyApx8brEEcP1qq_b4hAd74yZNO9sx12xgg"

bold = "\u001b[1m"
Black = "\u001b[30m"
Red = "\u001b[31m"
Green = "\u001b[32m"
Yellow = "\u001b[33m"
Blue =  "\u001b[34m"
Magenta = "\u001b[35m"
Cyan = "\u001b[36m"
clear = "\u001b[0m"
'''
Please note, this is rounded and NOT 100% Accurate due to GoogleAPIs not getting live counts.
'''
# <--- Getting a YT User --->
class user():
     def subscriber_count(self):
          #Subscriber Count
          url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername={self}&key={key}"
          print(url)
          r = requests.get(url)
          subs = r.json()['items'][0]['statistics']['subscriberCount']
          return subs
     def view_count(user):
          #View Count of YouTuber
          url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername={user}&key={key}"
          r = requests.get(url)
          views = r.json()['items'][0]['statistics']['viewCount']
          return views       
     def about(user):
          #About of YouTuber (COMING SOON)
          r = requests.get(f"https://youtube.com/{user}/about").text
          if r.status_code == 200:
               print("Got")
          else:
               print("Error!")
     def location(user):
          #Location of YouTuber
          pass
     def video_count(user):
          url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername={user}&key={key}"
          r = requests.get(url)
          vcount = r.json()['items'][0]['statistics']['videoCount']
          return vcount   
'''
To prevent spam and bot attacks, Commenting, posting, replying etc. is not a thing with YouTubeConnect and never will be.
'''
