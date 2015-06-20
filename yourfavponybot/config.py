import json
from log import log

class Config:
    def __init__(self, filename):
            with open(filename, "r") as file:
                jsonData = json.loads(file.read())
                self.consumerKey = jsonData["consumerKey"]
                self.consumerSecret = jsonData["consumerSecret"]
                self.accessKey = jsonData["accessKey"]
                self.accessSecret = jsonData["accessSecret"]
                self.tweetInterval = int(jsonData["tweetInterval"])
                self.tweetGrabInterval = int(jsonData["tweetGrabInterval"])
                self.rateLimitWaitInterval = int(jsonData["rateLimitWaitInterval"])
                self.mentionedDbPath = jsonData["mentionedDbPath"]
                self.startTime = jsonData["startTime"]
