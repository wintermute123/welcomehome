import RPi.GPIO as GPIO
import time
import os
import datetime

import mysql.connector

cnx = mysql.connector.connect(user='root', password='Marlboro123',
                              host='192.168.1.19',
                              database='raspiquarium')
cursor = cnx.cursor()





GPIO.setmode(GPIO.BCM)
PIR_PIN = 16
GPIO.setup(PIR_PIN, GPIO.IN)
def MOTION(PIR_PIN):
    print "Motion Detected!   "
    nowtime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    add_temp = ("insert into security"
                "(eventid, date,sensor,eventdata) "
                " values (%s, %s, %s, %s)")
    data_temp = ('',nowtime,'PiLights PIR 1','Motion Detected')
    
    cursor.execute(add_temp,data_temp)
    cnx.commit()
    print "PIR Module Test (CTRL+C to exit):"
    #gpio_pins = [7,4,2,3,22,23,25,5]
    gpio_pins = [4,23,27,22,6,13,26,24]
    for i in gpio_pins:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.LOW)
        
    for z in gpio_pins:
        GPIO.output(z, GPIO.HIGH)
        time.sleep(.2)
    for z in gpio_pins:
        GPIO.output(z, GPIO.LOW)
        time.sleep(.2)
    for z in gpio_pins:
        GPIO.output(z,GPIO.HIGH)
        time.sleep(.2)
    for z in gpio_pins:
        GPIO.output(z,GPIO.LOW)
        time.sleep(.2)

    for z in gpio_pins:
        GPIO.output(z,GPIO.HIGH)

    z=0
    for x in range(0, 99):
        GPIO.output(6,GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(6,GPIO.HIGH)
        time.sleep(0.1)
        
    time.sleep(10)
    for z in gpio_pins:
        GPIO.output(z, GPIO.LOW)
    #time.sleep(10)
    print "Ready"


    
try:
    GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
    #MOTION(17)
    while 1:
        time.sleep(10)
except KeyboardInterrupt:
    print " Quit"
GPIO.cleanup()
cursor.close()
cnx.close()

    
