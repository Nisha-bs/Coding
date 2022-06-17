#!/usr/bin/python3

import time
import posix_ipc 
def main (): 
  mq = posix_ipc.MessageQueue ( "/ jey" , posix_ipc.O_CREAT,max_messages =2)
  while True : 
    data = mq.receive () 
    print(data[0].decode())
    time.sleep ( 1 ) 

main()
