# -*- coding:UTF-8 -*-
import RPi.GPIO as GPIO
import time
import os
import threading

powerPin=7
resetPin=8
sparepowerPin=3
fanPin=5


GPIO.setmode(GPIO.BOARD)
GPIO.setup(sparepowerPin,GPIO.OUT)
GPIO.setup(powerPin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(resetPin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(fanPin,GPIO.OUT)

power_sate=0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        file = open("/sys/class/thermal/thermal_zone0/temp")
        temp = float(file.read()) / 1000
        file.close()
        temp="temp : %.1f" % temp
        print temp
        if temp>50:
            GPIO.output(fanPin, GPIO.LOW)
        if temp<45:
            GPIO.output(fanPin, GPIO.HIGH)

thread1 = myThread(1, "Thread-1", 1)
thread1.start()




thread1 = myThread(1, "Thread-1", 1)




while True:
    
    time.sleep(0.5)
    #pin7 is the power_key detect ponit ,if PIN7 is hight ,it is mean now is saft soft-shutdown
    '''
    检测Pin 7 powerPin
    开机程序运行后检测电源键位；
    状态0为未检测状态，如果电位为高电平系统判断为软关机模式，将状态设置为2
    如果电位为低电平将状态设置为1   
    '''
    if power_sate == 0:
        if GPIO.input(powerPin) :
            #open the spare mos
            GPIO.output(sparepowerPin,GPIO.LOW)
            print ("Switch mode=2:Software shutdown mode!")
            power_sate=2
            #将powerPin设置成下降沿中断
            #将resetPin设置成上升沿中断
            GPIO.add_event_detect(powerPin, GPIO.FALLING)
            GPIO.add_event_detect(resetPin, GPIO.RISING)


        if GPIO.input(powerPin) == False:
            power_sate = 1
            GPIO.output(sparepowerPin, GPIO.HIGH)
            print ("Switch mode=1:Harware shutdown mode!")



    if power_sate == 2:
        time.sleep(0.5)
        if GPIO.event_detected(powerPin):
            print ("The system will be shut down soon!")
            os.system("shutdown -h now")

        if GPIO.event_detected(resetPin):
            print ("The system will be reboot soon!")
            os.system("shutdown -r now")




