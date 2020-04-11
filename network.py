import socket 
from threading import Thread 
from SocketServer import ThreadingMixIn 
import time
import threading
import json, sys
import logging
import sys
import reply_thread


with open('process_config.json') as config_file:    
    config = json.load(config_file)
selfDcId = sys.argv[1]

dcInfo= {'dc_name':selfDcId.upper()}


######################################## Main ################################################



ip, port = config["processes"][selfDcId][0], config["processes"][selfDcId][1]

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
tcpServer.bind((ip, port))

print 'Server ready to listen on (%s:%d)' %(ip, port)
while True: 
    tcpServer.listen(4) 
    (conn, (cliIP,cliPort)) = tcpServer.accept() 

    message = conn.recv(1024)
    print("message received: " + message)

    newReplyThread = reply_thread.DelayedReplyThread()
    newReplyThread.start()