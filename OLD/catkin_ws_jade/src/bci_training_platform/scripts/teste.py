#!/usr/bin/env python
from __future__ import division
import scipy.signal as sg
import random
import rospy
import numpy as np
from threading import Thread as Th
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from std_msgs.msg import Float64
from std_msgs.msg import Float64MultiArray
fs=250
n_order=200
f1_2=[8,20]
b = sg.firwin(n_order,f1_2,pass_zero=False,window='blackman',nyq=fs/2)
dados=[]

tamanho_do_buffer = 1000
class meubuffer:           #classe para criacao do buffer
    def __init__(self,tamanho_max): #inicializazao do buffer com seu tamanho maximo como argumento
        self.max = tamanho_max
        self.data = []
    def append(self,x):    #adiciona array de elementos ao buffer, elemento unitario necessita de []
        self.data=np.hstack((self.data,x))
        if len(self.data) > self.max:
            self.data = np.delete(self.data,np.arange(0,len(x)))
    def get(self):         #retorna os elementos do buffer
        return self.data 
flag=0
def animate(i):
    #global dados
    global b,flag
    ax1.clear()
    ax1.set_ylim([-1, 1])
    if flag!=0:
        dados=sg.convolve(buffer.get(),b,mode='valid')
        ax1.plot(dados)
    flag=1
    

def plotsome():
    global fig, ax1
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    ani = animation.FuncAnimation(fig, animate, interval=400)
    plt.show()

def teste():
    rospy.init_node('teste', anonymous=True)
    fs=250
    t=0.0
    freq=2*np.pi*8
    rate = rospy.Rate(fs)
    while not rospy.is_shutdown():
        sinal = np.sin(freq*t)
        buffer.append([sinal])
	t=t+(1/fs)
        rate.sleep()

if __name__ == '__main__':
    buffer = meubuffer(tamanho_do_buffer)    #cria o buffer para as amostras recebidas
    t1 = Th(target=plotsome)
    t1.start()
    teste()









