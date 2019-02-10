'''
author : pH, radsn23
date : 09.02.2019
'''

import xml.dom.minidom
import requests
import random
import time

# blaster songs
songs = ['pink.mp3', 'imagine_dragons.mp3', 'the_nights.mp3']

# speaker's IP
ipaddr = "192.168.1.174"

url = 'https://radsn23.github.io/' + random.choice(songs)
# "https://radsn23.github.io/pink.mp3"  # enter the URL of the file you want to play here
service = "testing"
reason = "this"
message = "method."
# API key
key = "ku1IYMERCz8iqwNsMFDMSJJZ1kfYyOhA"

# volume of speaker
volumeVal = "25"

sendXML = "<play_info><app_key>" + key + "</app_key><url>" + url + "</url><service>" + service + "</service><reason>" + reason + "</reason><message>" + message + "</message><volume>" + volumeVal + "</volume></play_info>"

# form and send the /speaker POST request to start song
send = requests.post('http://' + ipaddr + ':8090/speaker', data=sendXML)

print('1')
time.sleep(10)
print('2')

# form and send the /speaker GET request to stop song
pause = requests.get('http://' + ipaddr + ':8090/standby')

# print a pretty version of the response
responseXML = xml.dom.minidom.parseString(send.text)
responseXML_pretty = responseXML.toprettyxml()
print(responseXML_pretty)
