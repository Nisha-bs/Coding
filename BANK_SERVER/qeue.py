#!/usr/bin/env python3

import queue
import threading
class Pipeline(queue.Queue):

    def __init__(self):

        super().__init__(maxsize=10)


    def get_message(self, name):


        value = self.get()


        return value


    def set_message(self, value, name):


        self.put(value)





def producer(pipeline, event):


    while not event.is_set():

        message = random.randint(1, 101)


        pipeline.set_message(message, "Producer")




def consumer(pipeline, event):


    while not event.is_set() or not pipeline.empty():

        message = pipeline.get_message("Consumer")
    print(f"message : {message}")




if __name__ == "__main__":



    pipeline = Pipeline()

    event = threading.Event()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:

        executor.submit(producer, pipeline, event)

        executor.submit(consumer, pipeline, event)


        time.sleep(0.1)


        event.set()
