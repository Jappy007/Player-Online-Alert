import time
import requests
import json
import winsound
def song():
    winsound.Beep(294, 250) #D
    winsound.Beep(294, 258) #D
    winsound.Beep(587, 500) #High D
    winsound.Beep(448, 580) #A
    winsound.Beep(415, 580) #G
    winsound.Beep(392, 580) #G
    winsound.Beep(349, 500) #F
    winsound.Beep(294, 250) #D
    winsound.Beep(349, 258) # F
    winsound.Beep(392, 250) # G
while True:
    response = requests.get("https://api.mcsrvstat.us/2/45.131.108.206")
    online = response.json()["online"]
    if online == True:
        players = response.json()["players"]
        playernum = players["online"]
        if playernum > 0:
           song()
        else:
            print(playernum,"spillere online")
    time.sleep(5)