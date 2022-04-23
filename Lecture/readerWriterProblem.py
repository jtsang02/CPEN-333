import threading as thread
import random

# reader - writer synchronization problem
# https://codezup.com/python-program-reader-writer-problem-mutex/
# https://docs.python.org/3/library/threading.html#semaphore-objects

wrt = thread.Semaphore()        # used by writers
mutex = thread.Semaphore()      # used by readers
readCount = 0                   # keep track of how many processse/threads are currently read
x = 0                           # shared memory

# define reader function
def reader():
        global readCount
        global x
        print ("reader is reading")
        mutex.acquire()
        readCount += 1
        print ("readCount value is: ", readCount)                  
        if (readCount == 1):
            wrt.acquire()
        mutex.release()
        print ("Shared data, x:" , x)   #reading is performed
        mutex.acquire()
        readCount -= 1
        print ("readCount value is: ", readCount)   
        if (readCount == 0):
            wrt.release()
        mutex.release()

# define writer function
def writer():
        global readCount
        global x
        wrt.acquire()
        print ("writer is writing")     # writing is performed
        x += 1                          # write on shared memory
        
        print ("writer is releasing the lock")
        wrt.release()

# main function
if __name__ == '__main__':
    for i in range(0, 10):
        randomNumber = random.randint(0, 100)   #Generate a Random number between 0 to 100
        if (randomNumber < 50):
            Thread1 = thread.Thread(target = reader)
            Thread1.start()
        else:
            Thread2 = thread.Thread(target = writer)
            Thread2.start()

Thread1.join()
Thread2.join()