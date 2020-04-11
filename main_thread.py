# 1 thread to handle user input, the other thread as TCP client to send message
import socket
import time
import asyncore
import json, sys
import comm_thread
from threading import Thread 

with open('process_config.json') as config_file:    
    config = json.load(config_file)

BUFFER_SIZE = 2000 
destPidQueue = []

class InputThread(Thread): 
    def __init__(self): 
	    Thread.__init__(self)

    def run(self): 
        global destPidQueue
        while True:
            pId = raw_input("Enter destination ID to send (P1, P2, P3)/ Enter 0 to exit.:")
            if pId == '0':
                break
            elif pId not in config["processes"]:
                print 'Invalid entry! Please enter a valid datacenter.'
                continue
            message = raw_input("Enter message to send:")
            destPidQueue.append((pId,message))

class ProcessThread(Thread): 
    def __init__(self): 
	    Thread.__init__(self)
    
    def run(self): 
        print "running process thread"
        while True:
            while destPidQueue:
                nw_ip, nw_port = config["processes"]["NW"][0], config["processes"]["NW"][1]
                destMsgTup = destPidQueue.pop(0)
                dest_id = destMsgTup[0]
                recvMsg = destMsgTup[1]
                print "global Pid in process thread = " + dest_id
                self.sendTcpMsg(nw_ip,nw_port, dest_id, recvMsg)

    def sendTcpMsg(self, ip, port, dest_id, msg):
        tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        time.sleep(5)
        tcpClient.connect((ip, port))
        tcpClient.send(msg + ";" + dest_id)
        logMsg = 'Sent message to: (%s, %d). Message is: %s' %(ip, port, msg)
        print(logMsg)
        
############ MAIN ############
myProcId = sys.argv[1]

newMainthread = InputThread()
newMainthread.start()

newProcthread = ProcessThread()
newProcthread.start()

newCommThread = comm_thread.CommThread(myProcId)
newCommThread.start()
