#!/usr/bin/env python
from __future__ import division
import rospy
import numpy as np
import scipy.signal as sg
from std_msgs.msg import MultiArrayDimension

num_channels=4

num_samples=250

frequency_of_sample=250

filter_order=100

f1_2=[8,30]

filter_vector = sg.firwin(filter_order,f1_2,pass_zero=False,window='blackman',nyq=frequency_of_sample/2) 


parametros = (num_channels,num_samples,frequency_of_sample,filter_order,filter_vector)

print(parametros)


def bloco_control():

	rospy.init_node('bloco_control', anonymous=True)

	pub=rospy.Publisher('controle', String, queue_size=1)

	rate = rospy.Rate(3)

	while not rospy.is_shutdown():

		pub.publish(data=raw_input())

		rate.sleep()


bloco_control()
