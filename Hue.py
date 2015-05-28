#*******************************************#
# Philips Hue Script                        #
# Written by Horacio Santoyo - 02/01/2015   #
# 02/20/15 - Added light bulb array         #
#*******************************************#

import json
import requests
import sys
import random

#Philips Bridge IP Address
IP = "192.168.1.30"

#List of light bulbs
lightList=[3,6,8]

#Color parameters:
#0 = Random color from colorList array, 1 = White, 2 = Color loop
colorList=[0,132,255,362,469,506,561,655]

#Check for user parameters (State, Brightness, Color)
if len(sys.argv) <4 :
   print ("Usage: <State (0=Off,1=On)> <Brightness (1-254)> <Color (0-65500>")
   sys.exit(0)
try:
   state = int(sys.argv[1])
   sat = int(sys.argv[2])
   bri = int(sys.argv[2])
   color = int(sys.argv[3])
except:
   print ("Arguments must be numeric.")
   sys.exit(0)

for i in lightList:
   if int(sys.argv[3])==0:
      color = random.choice(colorList)*100
      sat = 254

   if color==1:
      color = 35000

   if color==2:
      sat = 254
      On = {"on":True,"sat":sat,"bri":bri,"effect":"colorloop"}
   else:
      On = {"on":True,"sat":sat,"bri":bri,"hue":color,"effect":"none"}

   Off = {"on":False,"sat":sat,"bri":bri,"effect":"none"}
   url = "http://%s/api/newdeveloper/lights/%s/state" % (IP, i)

   if state==0:
      r = requests.put(url, data=json.dumps(Off))
   elif state==1:
      r = requests.put(url, data=json.dumps(On))
      

#Debugging:
#print (r.text)
#print (color)
