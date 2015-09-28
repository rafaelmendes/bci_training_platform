#!/usr/bin/env python
import rospy
import numpy as np
from std_msgs.msg import Float64
from std_msgs.msg import Float64MultiArray, Bool

tamanho_do_buffer = 1000     #define tamanho do buffer
class meubuffer:           #classe para criacao do buffer
    def __init__(self,tamanho_max): #inicializazao do buffer com seu tamanho maximo como argumento
        self.max = tamanho_max
        self.data = np.float64([])
    def append(self,x):    #adiciona array de elementos ao buffer, elemento unitario necessita de []
        self.data=np.hstack((self.data,x))
        if len(self.data) > self.max:
            self.data = np.delete(self.data,np.arange(0,len(x)))
    def get(self):         #retorna os elementos do buffer
        return self.data
    def len(self):
        return len(self.data) 

flag=0
contador=0
buffer2 = [ ]
def callback(data):        #callback do subscriber
    global buffer2,flag,pub2,contador
    buffer.append([data.data])
    contador=contador+1
    if flag==0 and contador==1000:
        flag=1
        contador=0
        buffer2 = buffer.get()
        pub2.publish(data=buffer2)
        flag=0
    
def second():
    global buffer2,flag1,pub2
    rospy.init_node('second', anonymous=True)
    rospy.Subscriber('canal1',Float64,callback,queue_size=1)
    pub=rospy.Publisher('controle1',Bool,queue_size=1)
    pub2=rospy.Publisher('canal2', Float64MultiArray,queue_size=1)
    rospy.spin()

if __name__ == '__main__':
    buffer = meubuffer(tamanho_do_buffer)    #cria o buffer para as amostras recebidas
    second()













