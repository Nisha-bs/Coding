#!/usr/bin/python3 

import posix_ipc 
import time

def main (): 
  mq = posix_ipc.MessageQueue ( "/ jey", posix_ipc.O_CREAT, max_messages = 5,max_message_size =1024  ) 
  while True : 
    mq.send ("Jeyendran K".encode()) 
    time.sleep ( 1 )

main ()

