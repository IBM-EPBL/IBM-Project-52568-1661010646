import json
import wiotp.sdk.device
import time
myconfig={
    "identity":{
        "orgid":"hj5fmy",
        "typeid":"nodemcu",
        "deviceid":"12345"
    },
    "auth":{
        "token":"12345678"
    }
}
client=wiotp.sdk.device.deviceclient(config=myconfig,loghandlers=none)
client.connect()
while true:
    name="smartbridge"
    #in area location
    #latitude=17.4219272
    #longitude=78.5488783
    #out area location
    #latitude=17.4219272
    #longitude=78.5488783
    mydata={'name':name,'lat':latitude,'log':longitude}
    client.publishEvent(eventid="status",msgformat="json",data=mydata,qos=0,onpublish=none)
    print("Data published to IBM IOT platform:",myData)
    time.sleep(5)
    client.disconnect()
    
