#!/usr/bin/env python
from __future__ import division
import rospy
import numpy as np
import scipy.signal as sg
from std_msgs.msg import Float64MultiArray

from threading import Thread as Th
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fs=100
n_order=100
f1_2=[8,30]
b = sg.firwin(n_order,f1_2,pass_zero=False,window='blackman',nyq=fs/2) 


dados=[]

def callback(dat):
    global dados
    dados = sg.convolve(dat.data,b,mode='valid')
    
def third():
    global dados
    rospy.init_node('third', anonymous=True)
    rospy.Subscriber('canal2', Float64MultiArray, callback,queue_size=1)
    pub3=rospy.Publisher('canal3', Float64MultiArray, queue_size=1)
    rate = rospy.Rate(1)
    k=1
    while not rospy.is_shutdown():
        #rospy.get_time()
        pub3.publish(data=dados)
        #print(k)
        #k=k+1
	rate.sleep()
    

if __name__ == '__main__':
    third()






