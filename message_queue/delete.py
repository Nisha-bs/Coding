#!/usr/bin/python3

import posix_ipc 
import time

mq = posix_ipc.MessageQueue ( "/ my_q01" , posix_ipc.O_CREAT)

while True:
    print(mq.receive()[0])
    time.sleep(1)


