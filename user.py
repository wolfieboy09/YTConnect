#ooooKkkJKDJK
#zinusiqy@finews.biz

#Get a User

import requests
import json

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
class user():
     def subscriber_count(self):
          print("requesting")
          url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername={self}&key={key}"
          r = requests.get(url)
          subs = r.json()['items'][0]['statistics']['subscriberCount']
          return subs
     def view_count(user):
          r = requests.get(f"https://youtube.com/{user}/about").text
          try:
               r.json()['Total Views']
          except:
               print("Failed to Parse ", r)               
     def about(user):
          r = requests.get(f"https://youtube.com/{user}/about").text
          if r.status_code == 200:
               print("Got")
          else:
               print("Error!")
     def location(user):
          pass
'''
To prevent spam and bot attacks, Comment and Video posting and replying is not a thing with YouTubeConnect and Never will be.
'''
