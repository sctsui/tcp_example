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

def parseMessage(raw_message):
    s = raw_message.split(';')
    message = s[0]
    dest = s[1]
    return message, dest

######################################## Main ################################################



ip, port = config["processes"][selfDcId][0], config["processes"][selfDcId][1]

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
tcpServer.bind((ip, port))

print 'Server ready to listen on (%s:%d)' %(ip, port)
while True: 
    tcpServer.listen(4) 
    (conn, (cliIP,cliPort)) = tcpServer.accept() 

    raw_message = conn.recv(1024)
    message, dest_id = parseMessage(raw_message)
    print("message received in NW: " + message)
    newReplyThread = reply_thread.DelayedReplyThread(dest_id)
    newReplyThread.start()