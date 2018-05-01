#Test ESC with brushless motor
#MAKE SURE PROPELLERS ARE REMOVED, DANGEROUS OTHERWISE

import os
import time
os.system ("sudo pigpiod")
time.sleep(1)
import pigpio

ESC1=4  #Connect the ESC signal cable in the corresponding GPIO pin
ESC2=17
ESC3=18
ESC4=27

ESCS = [ESC1, ESC2, ESC3, ESC4]

pi = pigpio.pi();
pi.set_servo_pulsewidth(ESC, 0)

max_value = 2000
min_value = 700
print "For first time launch, select calibrate"
print "Type the exact word for the function you want"
print "calibrate OR manual OR control OR arm OR stop"

def manual_drive(): #You will use this function to program your ESC if required
    print "Enter a value between 0 and %d" % max_value
    while True:
        inp = raw_input()
        if inp == "stop":
            stop()
            break
		elif inp == "control":
			control()
			break
		elif inp == "arm":
			arm()
			break
        else:
            pi.set_servo_pulsewidth(ESC,inp)

def calibrate():   #Calibrate the ESC normally
    for ESC in ESCS:
    pi.set_servo_pulsewidth(ESC, 0)
    print("Disconnect the battery and press Enter")
    inp = raw_input()
    if inp == '':
        for ESC in ESCS:
            pi.set_servo_pulsewidth(ESC, max_value)
        print("Connect the battery NOW.. you will hear two beeps, then wait for a gradual falling tone then press Enter")
        inp = raw_input()
        if inp == '':
            for ESC in ESCS:
                pi.set_servo_pulsewidth(ESC, min_value)
                print "Special tone indicates running as intended"
                time.sleep(7)
                print "Waiting for motor calibration (1/2) ...."
                time.sleep (5)
                print "Waiting for motor calibration (2/2) ...."
                pi.set_servo_pulsewidth(ESC, 0)
                time.sleep(2)
                print "Arming ESC now..."
                pi.set_servo_pulsewidth(ESC, min_value)
                time.sleep(1)
                print "ESC on GPIO pin %d has been calibrated" % ESC

            print "Initializing control subsystem..."
            control()

def control():
    print "Starting the motor. Make sure it is calibrated and armed."
    time.sleep(1)
    speed = 1500    #should be between 700 - 2000. 1500 is standard 'stopped' speed
    print "Controls - a to decrease speed & d to increase speed OR q to decrease a lot of speed & e to increase a lot of speed"
    while True:
        for ESC in ESCS:
            pi.set_servo_pulsewidth(ESC, speed)
        inp = raw_input()

        if inp == "q":
            speed -= 100    # greatly decrementing speed
            print "speed = %d" % speed
        elif inp == "e":
            speed += 100    # greatly incrementing speed
            print "speed = %d" % speed
        elif inp == "d":
            speed += 10     # incrementing speed
            print "speed = %d" % speed
        elif inp == "a":
            speed -= 10     # decrementing speed
            print "speed = %d" % speed
        elif inp == "stop":
            stop()          #going for the stop function
            break
        elif inp == "manual":
            manual_drive()
            break
		elif inp == "arm":
			arm()
			break
        else:
            print "Unrecognized input. Valid inputs are a,q,d or e"

def arm(): #This is the arming procedure of an ESC
    print "Connect the battery and press Enter"
    inp = raw_input()
    if inp == '':
        for ESC in ESCS:
            pi.set_servo_pulsewidth(ESC, 0)
            time.sleep(1)
            pi.set_servo_pulsewidth(ESC, max_value)
            time.sleep(1)
            pi.set_servo_pulsewidth(ESC, min_value)
            time.sleep(1)
        control()

def stop(): #This will stop every action your Pi is performing, but will not disable PiGPIO library
    for ESC in ESCS:
        pi.set_servo_pulsewidth(ESC, 0)
    pi.stop()

running = True
while(running):
    inp = raw_input()
    inp = inp.lower()
    if inp == "manual":
        manual_drive()
    elif inp == "calibrate":
        calibrate()
    elif inp == "arm":
        arm()
    elif inp == "control":
        control()
    elif inp == "stop":
        running=False
        stop()
    else :
        print "Unrecognized input, try again."
