#gets user input, enter 1 to send to which process

import socket
import time
import asyncore
import json, sys
import process_thread

with open('process_config.json') as config_file:    
    config = json.load(config_file)

BUFFER_SIZE = 2000 
 
 
while True:
    pId = raw_input("Enter destination NW to send/ Enter 0 to exit.:")
    if pId == '0':
        break
    elif pId not in config["processes"]:
        print 'Invalid entry! Please enter a valid datacenter.'
        continue
    
    #messageToSend = raw_input("Enter message to send: ")
    
    newthread = process_thread.ProcessThread() 
    newthread.start()


    #ip, port = config["processes"][pId][0], config["processes"][pId][1]
    #reqMsg = 'Send message'+pId+','+messageToSend+','+json.dumps({'seqNo':0})

    #tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    #time.sleep(5)
    #tcpClient.connect((ip, port))
    #tcpClient.send(reqMsg)

    #data = tcpClient.recv(BUFFER_SIZE)
    #while not data:
    #    data = tcpClient.recv(BUFFER_SIZE)
    #print data

    #tcpClient.close() 