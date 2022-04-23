import threading as thread
import random

# reader - writer synchronization problem
# https://codezup.com/python-program-reader-writer-problem-mutex/
# https://docs.python.org/3/library/threading.html#semaphore-objects

wrt = thread.Semaphore()        # used by writers
mutex = thread.Semaphore()      # used by readers
readCount = 0                   # keep trakc of how many processse/threads are currently read

# define writer function
def writer():
    while True:
        wrt.acquire()
        print("writer is writing!")     # writing is performed
        wrt.release()
        print()

# define reader function
def reader():
    while True:
        mutex.acquire()
        readCount += 1
        if readCount == 1:
            wrt.acquire()
        mutex.release()
        print("reader is reading")   #reading is performed
        mutex.acquire()
        readCount -= 1
        if readCount == 0:
            wrt.release()
        mutex.release()


