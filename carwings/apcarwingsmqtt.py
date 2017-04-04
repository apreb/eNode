#!/usr/bin/python

import pycarwings2
import time
from ConfigParser import SafeConfigParser
import logging
import sys
import pprint
import paho.mqtt.client as mqtt
import os
import json

logging.basicConfig()


if (len(sys.argv) != 4):
	print "\nInvalid operand, please check below\n"
	print "\nusage:"
	print "       carwings.py [user] [password] [action]\n"
	print "[user]     - carwings username"
	print "[password] - carwings password"
	print "[action]"
	print "   - battlaststaus - Request Last Status"
	print "   - battupdate    - Request Update"
	print "   - climateupdate - Request Climate Update"
	print "   - climatestart  - Request Climate Start"
	print "   - climatestop   - Request Climate Stop"
	print "   - chargestart   - Request Charge Start" 
	sys.exit()

username = str(sys.argv[1])
password = str(sys.argv[2])
action = str(sys.argv[3]

# USER DEFINED CONFIG
mqtt_host = "192.168.20.240"
mqtt_status_topic = "leaf/from"


client = mqtt.Client()

# Publish messages to the broker
def send_mqtt(mqtt_status_topic, mqtt_status_message):
  #client.username_pw_set(mqtt_username, mqtt_password);
  client.connect(mqtt_host, "1883", 60)
  client.publish(mqtt_status_topic, mqtt_status_message);


s = pycarwings2.Session(username, password , "NE")

try:
	l = s.get_leaf()
	send_mqtt(mqtt_status_topic,"Login OK")
except:
	send_mqtt(mqtt_status_topic,"Login NOK")
	sys.exit()


if action == 'battlaststaus':
  leaf_info = l.get_latest_battery_status()
	
  client.publish(mqtt_status_topic + "/OperationDateAndTime", leaf_info.answer["BatteryStatusRecords"]["OperationDateAndTime"],qos=0, retain=True)
  time.sleep(0.2)
  client.publish(mqtt_status_topic + "/NotificationDateAndTime", leaf_info.answer["BatteryStatusRecords"]["NotificationDateAndTime"],qos=0, retain=True)
  time.sleep(0.2)
  client.publish(mqtt_status_topic + "/CruisingRangeAcOff", leaf_info.answer["BatteryStatusRecords"]["CruisingRangeAcOff"],qos=0, retain=True)
  time.sleep(0.2)
  client.publish(mqtt_status_topic + "/CruisingRangeAcOn", leaf_info.answer["BatteryStatusRecords"]["CruisingRangeAcOn"],qos=0, retain=True)
  time.sleep(0.2)
  client.publish(mqtt_status_topic + "/PluginState", leaf_info.answer["BatteryStatusRecords"]["PluginState"],qos=0, retain=True)
  time.sleep(0.2)
  client.publish(mqtt_status_topic + "/TargetDate", leaf_info.answer["BatteryStatusRecords"]["TargetDate"],qos=0, retain=True)
  time.sleep(0.2)
  client.publish(mqtt_status_topic + "/BatteryRemainingAmountWH", leaf_info.answer["BatteryStatusRecords"]["BatteryStatus"]["BatteryRemainingAmountWH"],qos=0, retain=True)
  time.sleep(0.2)
  client.publish(mqtt_status_topic + "/BatteryChargingStatus", leaf_info.answer["BatteryStatusRecords"]["BatteryStatus"]["BatteryChargingStatus"],qos=0, retain=True)
  time.sleep(0.2)
  client.publish(mqtt_status_topic + "/BatteryRemainingAmount", leaf_info.answer["BatteryStatusRecords"]["BatteryStatus"]["BatteryRemainingAmount"],qos=0, retain=True)
  time.sleep(0.2)
  client.publish(mqtt_status_topic + "/BatteryCapacity", leaf_info.answer["BatteryStatusRecords"]["BatteryStatus"]["BatteryCapacity"],qos=0, retain=True)
  time.sleep(0.2)
  client.publish(mqtt_status_topic + "/BatteryRemainingAmountkWH", leaf_info.answer["BatteryStatusRecords"]["BatteryStatus"]["BatteryRemainingAmountkWH"],qos=0, retain=True)
  time.sleep(0.2)
  client.publish(mqtt_status_topic + "/TimeRequiredToFull200_6kW", leaf_info.answer["BatteryStatusRecords"]["TimeRequiredToFull200_6kW"]["HourRequiredToFull"] + ":" + leaf_info.answer["BatteryStatusRecords"]["TimeRequiredToFull200_6kW"]["MinutesRequiredToFull"],qos=0, retain=True)
  time.sleep(0.2)
  client.publish(mqtt_status_topic + "/TimeRequiredToFull200", leaf_info.answer["BatteryStatusRecords"]["TimeRequiredToFull200"]["HourRequiredToFull"] + ":" + leaf_info.answer["BatteryStatusRecords"]["TimeRequiredToFull200"]["MinutesRequiredToFull"],qos=0, retain=True)
  time.sleep(0.2)
  client.publish(mqtt_status_topic + "/TimeRequiredToFull", leaf_info.answer["BatteryStatusRecords"]["TimeRequiredToFull"]["HourRequiredToFull"] + ":" + leaf_info.answer["BatteryStatusRecords"]["TimeRequiredToFull"]["MinutesRequiredToFull"],qos=0, retain=True)
  time.sleep(0.2)

  #if leaf_info.is_connected == True:
  #  client.publish(mqtt_status_topic + "/connected", "Yes")
  #elif leaf_info.is_connected == False:
  #  client.publish(mqtt_status_topic + "/connected", "No")
  #else:
  #  client.publish(mqtt_status_topic + "/connected", leaf_info.is_connected)
  
  #pprint.pprint(json.dumps(leaf_info.answer))

elif action == 'battupdate':
        # REQUEST UPDATE
        result_key = l.request_update()
        i=0
        while True:
                i = i+1
                time.sleep(20)
                leaf_info = l.get_status_from_update(result_key)
                if leaf_info is not None:
			pprint.pprint(json.dumps(leaf_info.answer))
	
			_a = 0.1
			client.publish(mqtt_status_topic + "/currentChargeLevel", leaf_info.answer["currentChargeLevel"],qos=0, retain=True)
			time.sleep(_a)
			client.publish(mqtt_status_topic + "/timeRequiredToFull", leaf_info.answer["timeRequiredToFull"]["hours"] + ":" + leaf_info.answer["timeRequiredToFull"]["minutes"],qos=0, retain=True)
			time.sleep(_a)
			client.publish(mqtt_status_topic + "/timeRequiredToFull200_6kW", leaf_info.answer["timeRequiredToFull200_6kW"]["hours"] + ":" + leaf_info.answer["timeRequiredToFull200_6kW"]["minutes"],qos=0, retain=True)
			time.sleep(_a)
			client.publish(mqtt_status_topic + "/timeStamp", leaf_info.answer["timeStamp"],qos=0, retain=True)
			time.sleep(_a)
			client.publish(mqtt_status_topic + "/pluginState", leaf_info.answer["pluginState"],qos=0, retain=True)
			time.sleep(_a)
			client.publish(mqtt_status_topic + "/cruisingRangeAcOff", leaf_info.answer["cruisingRangeAcOff"],qos=0, retain=True)
			time.sleep(_a)
			client.publish(mqtt_status_topic + "/timeRequiredToFull200", leaf_info.answer["timeRequiredToFull200"]["hours"] + ":" + leaf_info.answer["timeRequiredToFull200"]["minutes"],qos=0, retain=True)
			time.sleep(_a)
			client.publish(mqtt_status_topic + "/batteryCapacity", leaf_info.answer["batteryCapacity"],qos=0, retain=True)
			time.sleep(_a)
			client.publish(mqtt_status_topic + "/cruisingRangeAcOn", leaf_info.answer["cruisingRangeAcOn"],qos=0, retain=True)
			time.sleep(_a)
			client.publish(mqtt_status_topic + "/batteryDegradation", leaf_info.answer["batteryDegradation"],qos=0, retain=True)
			time.sleep(_a)
			client.publish(mqtt_status_topic + "/charging", leaf_info.answer["charging"],qos=0, retain=True)
			time.sleep(_a)
			client.publish(mqtt_status_topic + "/chargeStatus", leaf_info.answer["chargeStatus"],qos=0, retain=True)
			time.sleep(_a)
			client.publish(mqtt_status_topic + "/chargeMode", leaf_info.answer["chargeMode"],qos=0, retain=True)
			time.sleep(_a)
                       	break
                if i > 3:
                        client.publish(mqtt_status_topic + "/battupdate", "Timeout",qos=0, retain=True)
                        break

elif action == 'climateupdate':
  leaf_info = l.get_latest_hvac_status()
  client.publish(mqtt_status_topic + "/climate", leaf_info.is_hvac_running)

elif action == 'climatestart':
  result_key = l.start_climate_control()
  client.publish(mqtt_status_topic + "/climate", "Start Sent")

elif action == 'climatestop':
  result_key = l.stop_climate_control()
  client.publish(mqtt_status_topic + "/climate", "Stop Sent")
  
elif action == 'chargestart':
  result_key = l.start_charging()
  client.publish(mqtt_status_topic + "/charge", "Start Sent")
	 
else:
	#print "--------- Get Lat Lon ---------"
	#result_key = l.get_lat_lon()
	#pprint.pprint(json.dumps(result_key.answer))

        print "--------- Driving Analysis ---------"
        result_key = l.get_driving_analysis()
        pprint.pprint(json.dumps(result_key.answer))


