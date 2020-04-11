# this thread sends "hello" to a destination process when run
import socket
import time
import threading
from threading import Thread 
import sys
import json

with open('process_config.json') as config_file:    
    config = json.load(config_file)

class DelayedReplyThread(Thread): 

    def __init__(self): 
	    Thread.__init__(self) 

    def run(self): 
        recvMsg = "hello from nw"
        print "running delayed reply thread"
        dest_ip, dest_port = config["processes"]["P1"][0], config["processes"]["P1"][1] #todo replace p1 with dest id
        self.sendTcpMsg(dest_ip,dest_port, recvMsg)

    def sendTcpMsg(self, ip, port, msg):
		tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		time.sleep(5)
		tcpClient.connect((ip, port))
		tcpClient.send(msg)
		logMsg = 'Sent message to: (%s, %d). Message is: %s' %(ip, port, msg)
		print(logMsg)
