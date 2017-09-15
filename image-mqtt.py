import os
import time
import picamera
import paho.mqtt.publish as publish

TOPIC = os.environ['TOPIC']
BROKER = os.environ['BROKER']

with picamera.PiCamera() as camera:
    print ("Capture the image...")
    camera.resolution = (2592, 1944 )
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)
    camera.capture('image.jpg')

    print ("Publish the image to MQTT broker...")
    f= open("image.jpg")
    filecontent = f.read()
    byteArr = bytearray(filecontent)

    publish.single(TOPIC, byteArr, qos=1, hostname=BROKER)
