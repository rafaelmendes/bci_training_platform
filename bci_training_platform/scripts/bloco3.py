#!/usr/bin/env python
from __future__ import division
import rospy
import numpy as np
import scipy.signal as sg
from std_msgs.msg import Float64MultiArray

num_channels=4
num_samples=250
frequency_of_sample=100
filter_order=100
f1_2=[8,30]
parametros = (4,250,250,100)
filter_vector = sg.firwin(filter_order,f1_2,pass_zero=False,window='blackman',nyq=frequency_of_sample/2) 
matrix_filtered = np.matrix([[0]*num_channels]*(num_samples + filter_order - 1)).T
#X_ft = np.matrix([])

msg_to_send = Float64MultiArray()

def filter_signal(matrix_to_be_filtered):
	matrix_to_be_filtered.shape=(num_channels,num_samples)
	for i in range(0,num_channels):
		matrix_filtered[i]=sg.convolve(matrix_to_be_filtered[i].A1,filter_vector,mode='full')
	return matrix_filtered

def callback(msg_received):
	X_ft = filter_signal(np.matrix(msg_received.data))
	msg_to_send.data=X_ft.A1
	pub.publish(msg_to_send)

def bloco3():
	global pub
	rospy.init_node('Filtro', anonymous=True)
	rospy.Subscriber('canal2',Float64MultiArray,callback,queue_size=1)
	pub=rospy.Publisher('canal3', Float64MultiArray, queue_size=1)
	rospy.spin()

bloco3()
	












