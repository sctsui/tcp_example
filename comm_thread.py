# this thread listens on a port and prints any messages it receives
import socket
import time
import threading
from threading import Thread 
import sys
import json

with open('process_config.json') as config_file:    
    config = json.load(config_file)

class CommThread(Thread): 

    def __init__(self,proc_id): 
	    Thread.__init__(self) 
            self.proc_id = proc_id

    def run(self): 
        print "running communication thread"
        pIp, pPort = config["processes"][self.proc_id][0], config["processes"][self.proc_id][1]
        tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
        tcpServer.bind((pIp, pPort))
        print 'Server ready to listen on (%s:%d)' %(pIp, pPort)
        self.printReceivedMsg(tcpServer)

    def printReceivedMsg(self,tcpServer):
        tcpServer.listen(1)
        while True:
            conn,addr = tcpServer.accept() 
            message = conn.recv(1024)
            print "message received: " + message
