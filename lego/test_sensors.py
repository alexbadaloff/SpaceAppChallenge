#-*- coding:utf8 -*-
#!/usr/bin/env python

import nxt.locator
from nxt.sensor import *

b = nxt.locator.find_one_brick()

#print 'Touch:', Touch(b, PORT_1).get_sample()
#print 'Sound:', Sound(b, PORT_2).get_sample()
Light(b, PORT_4).set_illuminated(False)
while True :
	print ("Light", "get_sample", Light(b, PORT_4).get_sample())# Вывод на экран сообщения о состоянии датчика света? (2 состояния: активное и пассивное)
	print ("Light", "get_input_values", Light(b, PORT_4).get_input_values())
	print ("Light", "get_lightness", Light(b, PORT_4).get_lightness())

	print ('Touch:', 'get_sample', Touch(b, PORT_3).get_sample())

	print ('Ultrasonic:', Ultrasonic(b, PORT_1).get_sample())

	print ('Sound', 'get_sample', Sound(b, PORT_2).get_sample())
	
#	print ('Button', )


#Light=Light(b,PORT_N).get_sample()
#if Light = Active:
#	print ("'Light' is active")
#elif Light = Passive:
#	print ("'Light'" is passive)
#	else: 
#	Light is null # какая тут может быть ошибка? отсутствие соединения с датчиком? а еще? может, их отдельно обработать?
#	print ("Something bad")

