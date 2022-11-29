import wiotp.sdk.device
import time
import random
myData = { 
    "identity": {
        "orgId": "zv613n",
        "typeId": "NODEMCU",
        "deviceId": "47300"
    },
    "auth": {
        "token": "(LFnPudA0&q1&AGZN3"
    }
}

client = wiotp.sdk.device.DeviceClient(config=myData, logHandlers=None)
client.connect()
while True:
    name= "Smartbridge" #in area location
    #latitude=17.4225176 #longitude=78.5458842
    #out area location
    latitude=17.4219272
    longitude=78.5488783
    myData={'name': name, 'lat': latitude,'lon': longitude}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Data published to IBM IOT platform :",myData)
    time.sleep(5)
client.disconnect();
