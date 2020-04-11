# this thread sends "hello" to a destination process when run
import socket
import time
import threading
from threading import Thread 
import sys
import json
import main_thread

with open('process_config.json') as config_file:    
    config = json.load(config_file)

class ProcessThread(Thread): 

    #def __init__(self, dest_id): 
	#    Thread.__init__(self) 
    #        self.dest_id = dest_id
    
    def __init__(self): 
	    Thread.__init__(self)
    
    def run(self): 
        global main_thread.globalPid
        recvMsg = "hello"
        print "running process thread"
        nw_ip, nw_port = config["processes"]["NW"][0], config["processes"]["NW"][1]
        #self.sendTcpMsg(nw_ip,nw_port, self.dest_id, recvMsg)
        print "global Pid in process thread = " + main_thread.globalPid
        self.sendTcpMsg(nw_ip,nw_port, main_thread.globalPid, recvMsg)

    def sendTcpMsg(self, ip, port, dest_id, msg):
		tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		time.sleep(5)
		tcpClient.connect((ip, port))
		tcpClient.send(msg + ";" + self.dest_id)
		logMsg = 'Sent message to: (%s, %d). Message is: %s' %(ip, port, msg)
		print(logMsg)
