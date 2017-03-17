

import time

def xchangemode():
    global x
    x=0

def ledon():
#	pwm.write(1)
    xchangemode()
    print "led turned on"

def ledoff():
    xchangemode()
    print "led turned off"
#	pwm.write(0)




def ldr_getvalues():
    global x
    x=1
    while x==1:
	time.sleep(0.3)
	print "ldr values"
#	while x==1:
#		val=light.value()
#		time.sleep(0.3)
#		print "ldr values"
#		if val<100:
#			ledon()
#		else :
#			ledoff()
