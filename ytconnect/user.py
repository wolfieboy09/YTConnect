import requests
from .exceptions import ResponceCodeNot200, APIKeyNotGiven

class Colors:
     BOLD = "\u001b[1m"
     BLACK = "\u001b[30m"
     RED = "\u001b[31m"
     GREEN = "\u001b[32m"
     YELLOW = "\u001b[33m"
     BLUE =  "\u001b[34m"
     MAGENTA = "\u001b[35m"
     CYAN = "\u001b[36m"
     CLEAR = "\u001b[0m"

class User:
     """Logic for retrieving information on a YouTube user
     
     NOTE: Commenting, posting and replying are not available because of bot/spam attacks"""
     def __init__(self, user: str, API_KEY: str = '') -> None:
          """`user` - The user you are connecting to"""
          self.user = user
          self.session = requests.Session()
          if API_KEY = '':
               raise APIKeyNotGiven("You need an API key")
          self.key = API_KEY

     def subscriber_count(self):
          """Get the subscriber count of a YouTuber"""
          url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername={self.user}&key={self.key}"
          r = self.session.get(url)
          subs = r.json()['items'][0]['statistics']['subscriberCount']
          return subs

     def view_count(self):
          """Get the total view count of a YouTuber
          
          NOTE: This is rounded and NOT 100% accurate due to GoogleAPIs not getting live counts."""
          url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername={self.user}&key={self.key}"
          r = self.session.get(url)
          views = r.json()['items'][0]['statistics']['viewCount']
          return views

     def about(self):
          """Get the about section of a YouTuber (incomplete)"""
          r = self.session.get(f"https://youtube.com/{self.user}/about").text
          # TODO: write logic for parsing about section
          if r.status_code == 200:
               print("Got")
          else:
               print("Error!")

     def location(self):
          """Get the geographical location of a YouTuber (INCLOMPLETE)"""
          raise NotImplementedError("The logic for this function is not complete")

     def video_count(self):
          """Get the number of videos a YouTuber has created"""
          url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername={self.user}&key={self.key}"
          r = self.session.get(url).json()
          return r['items'][0]['statistics']['videoCount']
